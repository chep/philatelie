from PyQt4 import QtGui, QtCore

from widgets import stampWidget

class StampWidget(QtGui.QDialog, stampWidget.Ui_stampWidget):
	def __init__(self, stamp, parent = None):
		super(StampWidget, self).__init__(parent)
		self.setupUi(self)
		self.connect(self.pushButtonClose, QtCore.SIGNAL("clicked()"),
		             self, QtCore.SLOT("close()"))

		self.labelName.setText(stamp.title)
		self.labelDescription.setText(stamp.description)
		self.labelComment.setText(stamp.comment)

		self.labelImage.setPixmap(QtGui.QPixmap(stamp.image))

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
