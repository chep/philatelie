from PyQt4 import QtGui, QtCore

from widgets import collectionStampWidget


class CollectionStampWidget(QtGui.QDialog, collectionStampWidget.Ui_collectionStampWidget):
	def __init__(self, stamp, parent = None):
		super(CollectionStampWidget, self).__init__(parent)
		self.setupUi(self)

		self.stamp = stamp

		self.lineEditName.setText(stamp.title)
		self.textEditDescription.setText(stamp.description)
		self.textEditComment.setText(stamp.comment)
		self.lineEditGroup.setText(stamp.group)
		self.lineEditCategory.setText(stamp.category)

		self.image = QtGui.QPixmap(stamp.image)

		self.lineEditDesigner.setText(stamp.designer)
		self.lineEditEngraver.setText(stamp.engraver)
		self.lineEditLayout.setText(stamp.layout)
		self.lineEditCredit.setText(stamp.credit)

		self.lineEditImpFormat.setText(stamp.impFormat)
		self.lineEditSeparationSize.setText(stamp.separationSize)
		self.lineEditShape.setText(stamp.shape)
		self.lineEditPhosphoric.setText(stamp.phosphoric)
		self.lineEditPrinting.setText(stamp.printing)
		self.lineEditColor.setText(stamp.color)
		self.lineEditValue.setText(stamp.value)
		self.lineEditSeparation.setText(stamp.separation)
		self.lineEditIssue.setText(stamp.issue)
		self.lineEditQuantity.setText(stamp.quantity)

		self.lineEditPhilatelix.setText(stamp.PhilatelixNum)
		self.lineEditMichel.setText(stamp.MichelNum)
		self.lineEditIssueDate.setText(stamp.issueDate)
		self.lineEditWithdrawalDate.setText(stamp.withdrawal)

		self.textEditOwnerComment.setText(stamp.ownerComment)
		self.spinBoxNbNew.setValue(stamp.ownerNew)
		self.spinBoxNbStamped.setValue(stamp.ownerStamped)

		self.resizeEvent = self.onResize
		self.paintEvent = self.onPaint

		self.connect(self.pushButtonModify, QtCore.SIGNAL("clicked()"),
		             self, QtCore.SLOT("clickModify()"))
		self.connect(self.pushButtonValidate, QtCore.SIGNAL("clicked()"),
		             self, QtCore.SLOT("clickValidate()"))
		self.connect(self.pushButtonCancel, QtCore.SIGNAL("clicked()"),
		             self, QtCore.SLOT("clickCancel()"))



	def onResize(self, event):
		self.labelImage.setPixmap(self.image.scaled(self.labelImage.width(),
		                                            self.labelImage.height(),
		                                            QtCore.Qt.KeepAspectRatio))

	def onPaint(self, event):
		self.labelImage.setPixmap(self.image.scaled(self.labelImage.width(),
		                                            self.labelImage.height(),
		                                            QtCore.Qt.KeepAspectRatio))

	def setAllEnabled(self, e):
		self.lineEditName.setEnabled(e)
		self.textEditDescription.setEnabled(e)
		self.textEditComment.setEnabled(e)
		self.lineEditGroup.setEnabled(e)
		self.lineEditCategory.setEnabled(e)
		self.lineEditDesigner.setEnabled(e)
		self.lineEditEngraver.setEnabled(e)
		self.lineEditLayout.setEnabled(e)
		self.lineEditCredit.setEnabled(e)
		self.lineEditImpFormat.setEnabled(e)
		self.lineEditSeparationSize.setEnabled(e)
		self.lineEditShape.setEnabled(e)
		self.lineEditPhosphoric.setEnabled(e)
		self.lineEditPrinting.setEnabled(e)
		self.lineEditColor.setEnabled(e)
		self.lineEditValue.setEnabled(e)
		self.lineEditSeparation.setEnabled(e)
		self.lineEditIssue.setEnabled(e)
		self.lineEditQuantity.setEnabled(e)
		self.lineEditPhilatelix.setEnabled(e)
		self.lineEditMichel.setEnabled(e)
		self.lineEditIssueDate.setEnabled(e)
		self.lineEditWithdrawalDate.setEnabled(e)
		self.textEditOwnerComment.setEnabled(e)
		self.spinBoxNbNew.setEnabled(e)
		self.spinBoxNbStamped.setEnabled(e)



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

	@QtCore.pyqtSlot()
	def clickCancel(self):
		self.pushButtonModify.setEnabled(True)
		self.pushButtonValidate.setEnabled(False)
		self.pushButtonCancel.setEnabled(False)
		self.setAllEnabled(False)
