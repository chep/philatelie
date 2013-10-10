from PyQt4 import QtGui, QtCore

from widgets.mainWindow import *
from webSearchWidget import *
from collectionStampWidget import *

filterYear = 0
filterGroup = 1
filterCategory = 2
filterDesigner = 3
filterEngraver = 4
filterError = 5

class StampButton(QtGui.QPushButton):
	def __init__(self, parent, stamp):
		super(StampButton, self).__init__(parent)
		pixmap = QtGui.QPixmap(stamp.image).scaled(100, 100,
		                                           QtCore.Qt.KeepAspectRatio)
		self.setIcon(QtGui.QIcon(pixmap))
		self.setIconSize(pixmap.size())
		self.setFlat(True)
		self.stamp = stamp
		self.connect(self, QtCore.SIGNAL("clicked()"),
		             self, QtCore.SLOT("click()"))

	@QtCore.pyqtSlot()
	def click(self):
		sw = CollectionStampWidget(self.stamp)
		sw.exec_()


class StampFrame(QtGui.QFrame):
	def __init__(self, stamp, parent = None):
		super(StampFrame, self).__init__()
		self.layout = QtGui.QVBoxLayout()
		self.setLayout(self.layout)
		button = StampButton(self, stamp)
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
		self.updateFilterList()
		self.connect(self.comboBoxFilter, QtCore.SIGNAL("currentIndexChanged(int)"),
		             self, QtCore.SLOT("updateFilterList(int)"))
		self.connect(self.listWidgetFilter, QtCore.SIGNAL("currentRowChanged(int)"),
		             self, QtCore.SLOT("updateStampList(int)"))
		self.connect(self.actionSearchWeb, QtCore.SIGNAL("triggered()"),
		             self, QtCore.SLOT("webSearch()"))

	def index2Filter(self, index):
		if index == 0:
			return filterYear
		#group
		elif index == 1:
			return filterGroup
		#category
		elif index == 2:
			return filterCategory
		#Designer
		elif index == 3:
			return filterDesigner
		#Engraver
		elif index == 4:
			return filterEngraver
		else:
			return filterError


	@QtCore.pyqtSlot(int)
	def updateFilterList(self, index = 0):
		self.listWidgetFilter.clear()
		list = []
		filter = self.index2Filter(index)
		#year
		if filter == filterYear:
			list = self.collection.getAllYears()
		#group
		elif filter == filterGroup:
			list = self.collection.getAllGroups()
		#category
		elif filter == filterCategory:
			list = self.collection.getAllCategories()
		#Designer
		elif filter == filterDesigner:
			list = self.collection.getAllDesigners()
		#Engraver
		elif filter == filterEngraver:
			list = self.collection.getAllEngraver()

		for l in list:
			self.listWidgetFilter.addItem(l)


	@QtCore.pyqtSlot(int)
	def updateStampList(self, row):
		for i in reversed(range(self.gridLayoutDisplay.count())):
			self.gridLayoutDisplay.itemAt(i).widget().setParent(None)
		if row < 0:
			return
		text = self.listWidgetFilter.item(row).text()
		filter = self.index2Filter(self.comboBoxFilter.currentIndex())

		list = []
		#year
		if filter == filterYear:
			list = self.collection.getStampsYear(text)
		#group
		elif filter == filterGroup:
			list = self.collection.getStampsGroup(text)
		#category
		elif filter == filterCategory:
			list = self.collection.getStampsCategory(text)
		#Designer
		elif filter == filterDesigner:
			list = self.collection.getStampsDesigner(text)
		#Engraver
		elif filter == filterEngraver:
			list = self.collection.getStampsEngraver(text)

		row = 0
		col = 0
		for stamp in list:
			frame = StampFrame(stamp, self.frameDisplay)
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


	@QtCore.pyqtSlot()
	def webSearch(self):
		w = WebSearchWidget()
		w.exec_()
