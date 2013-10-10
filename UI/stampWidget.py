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

class StampWidget(QtGui.QDialog, stampWidget.Ui_stampWidget):
	def __init__(self, stamp, parent = None):
		super(StampWidget, self).__init__(parent)
		self.setupUi(self)

		self.labelName.setText(stamp.title)
		self.labelDescription.setText(stamp.description)
		self.labelComment.setText(stamp.comment)
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

		self.resizeEvent = self.onResize
		self.paintEvent = self.onPaint


	def onResize(self, event):
		self.labelImage.setPixmap(self.image.scaled(self.labelImage.width(),
		                                            self.labelImage.height(),
		                                            QtCore.Qt.KeepAspectRatio))

	def onPaint(self, event):
		self.labelImage.setPixmap(self.image.scaled(self.labelImage.width(),
		                                            self.labelImage.height(),
		                                            QtCore.Qt.KeepAspectRatio))
