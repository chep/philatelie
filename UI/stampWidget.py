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

from widgets import stampWidget
from collectionStampWidget import *

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class AddWidget(QtGui.QDialog):
	def __init__(self):
		super(AddWidget, self).__init__()
		self.label1 = QtGui.QLabel(_translate("AddWidget", "Nb new:", None), self)
		self.label2 = QtGui.QLabel(_translate("AddWidget", "Nb stamped:", None), self)
		self.label3 = QtGui.QLabel(_translate("AddWidget", "Personal comment:", None), self)
		self.spinNew = QtGui.QSpinBox(self)
		self.spinNew.setMaximum(999999)
		self.spinStamped = QtGui.QSpinBox(self)
		self.spinStamped.setMaximum(999999)
		self.textComment = QtGui.QTextEdit(self)
		self.buttonOk = QtGui.QPushButton(_translate("AddWidget", "Ok", None), self)
		self.buttonCancel = QtGui.QPushButton(_translate("AddWidget", "Cancel", None), self)
		self.gridLayout = QtGui.QGridLayout(self)
		self.gridLayout.addWidget(self.label1, 0, 0)
		self.gridLayout.addWidget(self.label2, 1, 0)
		self.gridLayout.addWidget(self.label3, 2, 0)
		self.gridLayout.addWidget(self.spinNew, 0, 1)
		self.gridLayout.addWidget(self.spinStamped, 1, 1)
		self.gridLayout.addWidget(self.textComment, 2, 1)
		self.gridLayout.addWidget(self.buttonOk, 3, 0)
		self.gridLayout.addWidget(self.buttonCancel, 3, 1)

		self.buttonOk.clicked.connect(self.ok)
		self.buttonCancel.clicked.connect(self.cancel)

		self.return_ = 0
		self.new = 0
		self.stamped = 0
		self.comment = ""

	def ok(self):
		if self.spinNew.value() == 0 and self.spinStamped.value() == 0:
			msg = QtGui.QMessageBox(QtGui.QMessageBox.Critical,
									_translate("AddWidget", "Error", None),
									_translate("AddWidget", "You can't add 0 stamp", None))
			msg.exec_()
		else:
			self.new = self.spinNew.value()
			self.stamped = self.spinStamped.value()
			self.comment = unicode(self.textComment.toPlainText())
			self.return_ = 1
			self.close()

	def cancel(self):
		self.return_ = 0
		self.close()


class StampWidget(QtGui.QDialog, stampWidget.Ui_stampWidget):
	def __init__(self, stamp, collection, parent = None):
		super(StampWidget, self).__init__(parent)
		self.setupUi(self)

		self.collection = collection
		self.stamp = stamp

		self.labelName.setText(stamp.title)
		self.textBrowserDescription.setPlainText(stamp.description)
		self.textBrowserComment.setPlainText(stamp.comment)
		self.labelGroup.setText(stamp.group)
		self.labelCategory.setText(stamp.category)

		self.image = QtGui.QPixmap(stamp.image)

		self.labelDesigner.setText(stamp.designer)
		self.labelEngraver.setText(stamp.engraver)
		self.labelLayout.setText(stamp.layout)
		self.labelCredit.setText(stamp.credit)

		self.labelImpformat.setText(stamp.impFormat)
		self.labelSeparationSize.setText(stamp.separationSize)
		self.labelShape.setText(stamp.shape)
		self.labelPhosphoric.setText(stamp.phosphoric)
		self.labelPrinting.setText(stamp.printing)
		self.labelColor.setText(stamp.color)
		self.labelValue.setText(stamp.value)
		self.labelSeparation.setText(stamp.separation)
		self.labelIssue.setText(stamp.issue)
		self.labelQuantity.setText(stamp.quantity)

		self.labelPhilatelix.setText(stamp.PhilatelixNum)
		self.labelMichel.setText(stamp.MichelNum)
		self.labelDate.setText(stamp.issueDate)
		self.labelWithdrawal.setText(stamp.withdrawal)

		self.paintEvent = self.onPaint

		self.checkCollection()

		#Signals and slots
		self.pushButtonAdd.clicked.connect(self.add)
		self.listWidgetCollectionStamps.itemDoubleClicked.connect(self.openStamp)

	def onPaint(self, event):
		self.labelImage.setPixmap(self.image.scaled(self.labelImage.width() - 30,
		                                            self.labelImage.height() - 30,
		                                            QtCore.Qt.KeepAspectRatio))

	def add(self):
		aw = AddWidget()
		aw.exec_()
		if aw.return_:
			self.stamp.ownerNew = aw.new
			self.stamp.ownerStamped = aw.stamped
			self.stamp.ownerComment = aw.comment
			f = QtCore.QFile(self.collection.getImagesDirectory() + self.stamp.identifier + ".png")
			f.open(QtCore.QIODevice.WriteOnly)
			self.image.save(f, "PNG")
			self.stamp.image = self.collection.getImagesDirectory() + self.stamp.identifier + ".png"
			self.collection.addStamp(self.stamp)
			self.checkCollection()


	def checkCollection(self):
		self.listWidgetCollectionStamps.clear()
		s = self.collection.getStampIdentifier(self.stamp.identifier)
		if s == None:
			list = self.collection.getStampTitle(self.stamp.title)
			if len(list) == 0:
				self.labelCollectionResult.setText(_translate("stampwidget", "This stamp is not in your collection", None))
				self.listWidgetCollectionStamps.setVisible(False)
				self.labelDisplayNew.setVisible(False)
				self.labelNew.setVisible(False)
				self.labelDisplayStamped.setVisible(False)
				self.labelStamped.setVisible(False)
				self.pushButtonAdd.setEnabled(True)
			else:
				self.labelCollectionResult.setText(_translate("stampwidget", "This stamp is not in your collection but matches other ones (double click on the identifier to open):", None))
				self.listWidgetCollectionStamps.setVisible(True)
				for s2 in list:
					self.listWidgetCollectionStamps.addItem(s2.identifier)
				self.labelDisplayNew.setVisible(False)
				self.labelNew.setVisible(False)
				self.labelDisplayStamped.setVisible(False)
				self.labelStamped.setVisible(False)
				self.pushButtonAdd.setEnabled(True)
		else:
			self.labelCollectionResult.setText(_translate("stampwidget", "This stamp is already in your collection (double click on the identifier to open):", None))
			self.listWidgetCollectionStamps.setVisible(True)
			self.listWidgetCollectionStamps.addItem(s.identifier)
			self.labelDisplayNew.setVisible(True)
			self.labelNew.setVisible(True)
			self.labelNew.setText(str(s.ownerNew))
			self.labelDisplayStamped.setVisible(True)
			self.labelStamped.setVisible(True)
			self.labelStamped.setText(str(s.ownerStamped))
			self.pushButtonAdd.setEnabled(False)

	def openStamp(self, item):
		id = unicode(item.text())
		s = self.collection.getStampIdentifier(id)
		if s == None:
			msg = QtGui.QMessageBox(QtGui.QMessageBox.Critical,
									_translate("stampwidget", "Error", None),
									_translate("stampwidget", "Unable to find stamp in collection", None))
			msg.exec_()
		else:
			csw = CollectionStampWidget(s, self.collection)
			csw.exec_()
			self.checkCollection()
