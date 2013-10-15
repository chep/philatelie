# -*- coding: utf-8 -*-

# Copyright (C) 2013 Cédric Chépied

# Author: Cédric Chépied (cedric.chepied@gmail.com)
# Maintainer: Cédric Chépied

# This file is part of Philatelie.

# Philatelie is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Philatelie is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Philatelie.  If not, see <http://www.gnu.org/licenses/>.


from PyQt4 import QtGui, QtCore

from widgets.mainWindow import *
from webSearchWidget import *
from collectionStampWidget import *
from collectionManagement.collection import *

filterYear = 0
filterGroup = 1
filterCategory = 2
filterDesigner = 3
filterEngraver = 4
filterError = 5

class StampButton(QtGui.QPushButton):
	def __init__(self, parent, stamp, collection):
		super(StampButton, self).__init__(parent)
		pixmap = QtGui.QPixmap(stamp.image).scaled(100, 100,
		                                           QtCore.Qt.KeepAspectRatio)
		self.setIcon(QtGui.QIcon(pixmap))
		self.setIconSize(pixmap.size())
		self.setFlat(True)
		self.stamp = stamp
		self.collection = collection
		self.clicked.connect(self.click)

	@QtCore.pyqtSlot()
	def click(self):
		sw = CollectionStampWidget(self.stamp, self.collection)
		sw.exec_()


class StampFrame(QtGui.QFrame):
	def __init__(self, stamp, collection, parent = None):
		super(StampFrame, self).__init__()
		self.layout = QtGui.QVBoxLayout()
		self.setLayout(self.layout)
		button = StampButton(self, stamp, collection)
		self.layout.addWidget(button)
		title = QtGui.QLabel(stamp.title, self)
		title.setWordWrap(True)
		self.layout.addWidget(title)
		desc = QtGui.QLabel(stamp.description, self)
		desc.setWordWrap(True)
		self.layout.addWidget(desc)
#		self.setFrameShape(QtGui.QFrame.Box)
		self.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)

class MainWindowWidget(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self, collection, parent = None):
		super(MainWindowWidget, self).__init__()
		self.setupUi(self)
		self.splitter.setStretchFactor(1,1)
		self.collection = collection

		self.spinBoxYearMax.setVisible(False)
		self.spinBoxYearMin.setVisible(False)
		self.labelYear.setVisible(False)

		self.updateFilters()

		self.actionSearchWeb.triggered.connect(self.webSearch)
		self.comboBoxYear.currentIndexChanged.connect(self.yearChanged)
		self.pushButtonApply.clicked.connect(self.applyFilters)
		self.pushButtonReset.clicked.connect(self.resetFilters)


	def yearChanged(self, index):
		if index == 0:
			self.spinBoxYearMax.setVisible(False)
			self.spinBoxYearMin.setVisible(False)
			self.labelYear.setVisible(False)
		elif index == 4:
			self.spinBoxYearMin.setVisible(True)
			self.spinBoxYearMax.setVisible(True)
			self.labelYear.setVisible(True)
		else:
			self.spinBoxYearMin.setVisible(True)
			self.spinBoxYearMax.setVisible(False)
			self.labelYear.setVisible(False)

	def updateFilters(self):
		list = self.collection.getAllCategories()
		for c in list:
			self.comboBoxCategory.addItem(c)
		list = self.collection.getAllGroups()
		for c in list:
			self.comboBoxGroup.addItem(c)
		list = self.collection.getAllDesigners()
		for c in list:
			self.comboBoxDesigner.addItem(c)
		list = self.collection.getAllEngraver()
		for c in list:
			self.comboBoxEngraver.addItem(c)

	def resetFilters(self):
		for i in reversed(range(self.gridLayoutDisplay.count())):
	 		self.gridLayoutDisplay.itemAt(i).widget().setParent(None)
		self.comboBoxYear.setCurrentIndex(0)
		self.comboBoxGroup.setCurrentIndex(0)
		self.comboBoxCategory.setCurrentIndex(0)
		self.comboBoxDesigner.setCurrentIndex(0)
		self.comboBoxEngraver.setCurrentIndex(0)
		self.lineEditKeyword.setText("")

	def applyFilters(self):
		operation = None
		index = self.comboBoxYear.currentIndex()
		if index == 1:
			operation = Operation.equal
		elif index == 2:
			operation = Operation.less
		elif index == 3:
			operation = Operation.greater
		elif index == 4:
			operation = Operation.between

		ymin = None
		if self.spinBoxYearMin.isVisible():
			ymin = self.spinBoxYearMin.value()

		ymax = None
		if self.spinBoxYearMax.isVisible():
			ymax = self.spinBoxYearMax.value()

		g = unicode(self.comboBoxGroup.currentText())
		i = self.comboBoxGroup.currentIndex()
		if i == 0:
			g = None

		cat = unicode(self.comboBoxCategory.currentText())
		i = self.comboBoxCategory.currentIndex()
		if i == 0:
			cat = None

		d = unicode(self.comboBoxDesigner.currentText())
		i = self.comboBoxDesigner.currentIndex()
		if i == 0:
			d = None

		e = unicode(self.comboBoxEngraver.currentText())
		i = self.comboBoxEngraver.currentIndex()
		if i == 0:
			e = None

		kw = unicode(self.lineEditKeyword.text())
		if kw == "":
			kw = None

		list = self.collection.getStampFilters(operation = operation, yearMin = ymin, yearMax = ymax,
		                                       group = g, category = cat,
		                                       designer = d, engraver = e, keyword = kw)

	 	for i in reversed(range(self.gridLayoutDisplay.count())):
	 		self.gridLayoutDisplay.itemAt(i).widget().setParent(None)
		row = 0
		col = 0
		for stamp in list:
			frame = StampFrame(stamp, self.collection, self.frameDisplay)
			self.gridLayoutDisplay.addWidget(frame, row, col,
			                                 QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
			col = (col + 1) % 5
			if col == 0:
				row = row + 1

		#empty widgets for alignement
		empty = QtGui.QWidget()
		empty2 = QtGui.QWidget()
		empty.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
		empty2.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
		self.gridLayoutDisplay.addWidget(empty, 0, 5)
		self.gridLayoutDisplay.addWidget(empty2, row + 1, 0)


	def webSearch(self):
		w = WebSearchWidget(self.collection)
		w.exec_()
		self.resetFilters()
