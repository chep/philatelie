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

from widgets import collectionStampWidget


class CollectionStampWidget(QtGui.QDialog, collectionStampWidget.Ui_collectionStampWidget):
	def __init__(self, stamp, collection, parent = None):
		super(CollectionStampWidget, self).__init__(parent)
		self.setupUi(self)

		self.stamp = stamp
		self.collection = collection

		self.updateWidgets()

		self.paintEvent = self.onPaint

		self.connect(self.pushButtonModify, QtCore.SIGNAL("clicked()"),
		             self, QtCore.SLOT("clickModify()"))
		self.connect(self.pushButtonValidate, QtCore.SIGNAL("clicked()"),
		             self, QtCore.SLOT("clickValidate()"))
		self.connect(self.pushButtonCancel, QtCore.SIGNAL("clicked()"),
		             self, QtCore.SLOT("clickCancel()"))
		self.connect(self.checkBoxWithdrawal, QtCore.SIGNAL("stateChanged(int)"),
		             self, QtCore.SLOT("checkBoxChanged(int)"))
		self.setAllEnabled(False)


	def updateWidgets(self):
		self.lineEditName.setText(self.stamp.title)
		self.textEditDescription.setText(self.stamp.description)
		self.textEditComment.setText(self.stamp.comment)
		self.lineEditGroup.setText(self.stamp.group)
		self.lineEditCategory.setText(self.stamp.category)

		self.image = QtGui.QPixmap(self.stamp.image)

		self.lineEditDesigner.setText(self.stamp.designer)
		self.lineEditEngraver.setText(self.stamp.engraver)
		self.lineEditLayout.setText(self.stamp.layout)
		self.lineEditCredit.setText(self.stamp.credit)

		self.lineEditImpFormat.setText(self.stamp.impFormat)
		self.lineEditSeparationSize.setText(self.stamp.separationSize)
		self.lineEditShape.setText(self.stamp.shape)
		self.lineEditPhosphoric.setText(self.stamp.phosphoric)
		self.lineEditPrinting.setText(self.stamp.printing)
		self.lineEditColor.setText(self.stamp.color)
		self.lineEditValue.setText(self.stamp.value)
		self.lineEditSeparation.setText(self.stamp.separation)
		self.lineEditIssue.setText(self.stamp.issue)
		self.lineEditQuantity.setText(self.stamp.quantity)

		self.lineEditPhilatelix.setText(self.stamp.PhilatelixNum)
		self.lineEditMichel.setText(self.stamp.MichelNum)
		try:
			self.dateEditIssue.setDate(QtCore.QDate.fromString(self.stamp.issueDate, "yyyy-MM-dd"))
		except:
			pass
		try:
			date = QtCore.QDate.fromString(self.stamp.withdrawal, "yyyy-MM-dd")
			if date.isValid():
				self.dateEditWithdrawal.setVisible(True)
				self.dateEditWithdrawal.setDate(date)
				self.checkBoxWithdrawal.setCheckState(QtCore.Qt.Checked)
			else:
				raise 0
		except:
			self.dateEditWithdrawal.setVisible(False)
			self.checkBoxWithdrawal.setCheckState(QtCore.Qt.Unchecked)

		self.textEditOwnerComment.setText(self.stamp.ownerComment)
		self.spinBoxNbNew.setValue(self.stamp.ownerNew)
		self.spinBoxNbStamped.setValue(self.stamp.ownerStamped)

	def updateStamp(self):
		self.stamp.title  = unicode(self.lineEditName.text())
		self.stamp.description  = unicode(self.textEditDescription.toPlainText())
		self.stamp.comment  = unicode(self.textEditComment.toPlainText())
		self.stamp.group  = unicode(self.lineEditGroup.text())
		self.stamp.category  = unicode(self.lineEditCategory.text())

		self.stamp.designer  = unicode(self.lineEditDesigner.text())
		self.stamp.engraver  = unicode(self.lineEditEngraver.text())
		self.stamp.layout  = unicode(self.lineEditLayout.text())
		self.stamp.credit  = unicode(self.lineEditCredit.text())

		self.stamp.impFormat  = unicode(self.lineEditImpFormat.text())
		self.stamp.separationSize  = unicode(self.lineEditSeparationSize.text())
		self.stamp.shape  = unicode(self.lineEditShape.text())
		self.stamp.phosphoric  = unicode(self.lineEditPhosphoric.text())
		self.stamp.printing  = unicode(self.lineEditPrinting.text())
		self.stamp.color  = unicode(self.lineEditColor.text())
		self.stamp.value  = unicode(self.lineEditValue.text())
		self.stamp.separation  = unicode(self.lineEditSeparation.text())
		self.stamp.issue  = unicode(self.lineEditIssue.text())
		self.stamp.quantity  = unicode(self.lineEditQuantity.text())

		self.stamp.PhilatelixNum  = unicode(self.lineEditPhilatelix.text())
		self.stamp.MichelNum  = unicode(self.lineEditMichel.text())

		self.stamp.issueDate  = unicode(self.dateEditIssue.date().toString("yyyy-MM-dd"))
		if self.checkBoxWithdrawal.checkState():
			self.stamp.withdrawal  = unicode(self.dateEditWithdrawal.date().toString("yyyy-MM-dd"))
		else:
			self.stamp.withdrawal = None

		self.stamp.ownerComment  = unicode(self.textEditOwnerComment.toPlainText())
		self.stamp.ownerNew = self.spinBoxNbNew.value()
		self.stamp.ownerStamped = self.spinBoxNbStamped.value()


	def onPaint(self, event):
		self.labelImage.setPixmap(self.image.scaled(self.labelImage.width() - 30,
		                                            self.labelImage.height() - 30,
		                                            QtCore.Qt.KeepAspectRatio))

	def setAllEnabled(self, e):
		self.lineEditName.setReadOnly(not e)
		self.textEditDescription.setReadOnly(not e)
		self.textEditComment.setReadOnly(not e)
		self.lineEditGroup.setReadOnly(not e)
		self.lineEditCategory.setReadOnly(not e)
		self.lineEditDesigner.setReadOnly(not e)
		self.lineEditEngraver.setReadOnly(not e)
		self.lineEditLayout.setReadOnly(not e)
		self.lineEditCredit.setReadOnly(not e)
		self.lineEditImpFormat.setReadOnly(not e)
		self.lineEditSeparationSize.setReadOnly(not e)
		self.lineEditShape.setReadOnly(not e)
		self.lineEditPhosphoric.setReadOnly(not e)
		self.lineEditPrinting.setReadOnly(not e)
		self.lineEditColor.setReadOnly(not e)
		self.lineEditValue.setReadOnly(not e)
		self.lineEditSeparation.setReadOnly(not e)
		self.lineEditIssue.setReadOnly(not e)
		self.lineEditQuantity.setReadOnly(not e)
		self.lineEditPhilatelix.setReadOnly(not e)
		self.lineEditMichel.setReadOnly(not e)
		self.dateEditIssue.setReadOnly(not e)
		self.checkBoxWithdrawal.setEnabled(e)
		self.dateEditWithdrawal.setReadOnly(not e)
		self.textEditOwnerComment.setReadOnly(not e)
		self.spinBoxNbNew.setReadOnly(not e)
		self.spinBoxNbStamped.setReadOnly(not e)
		self.pushButtonImage.setEnabled(e)



	@QtCore.pyqtSlot()
	def clickModify(self):
		self.pushButtonModify.setEnabled(False)
		self.pushButtonValidate.setEnabled(True)
		self.pushButtonCancel.setEnabled(True)
		self.setAllEnabled(True)

	@QtCore.pyqtSlot()
	def clickValidate(self):
		self.pushButtonModify.setEnabled(True)
		self.pushButtonValidate.setEnabled(False)
		self.pushButtonCancel.setEnabled(False)
		self.setAllEnabled(False)
		self.updateStamp()
		self.collection.modifyStamp(self.stamp)

	@QtCore.pyqtSlot()
	def clickCancel(self):
		self.pushButtonModify.setEnabled(True)
		self.pushButtonValidate.setEnabled(False)
		self.pushButtonCancel.setEnabled(False)
		self.setAllEnabled(False)
		self.updateWidgets()

	@QtCore.pyqtSlot(int)
	def checkBoxChanged(self, state):
		if state == QtCore.Qt.Unchecked:
			self.dateEditWithdrawal.setVisible(False)
		else:
			self.dateEditWithdrawal.setVisible(True)
