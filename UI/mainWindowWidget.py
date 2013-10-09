from PyQt4 import QtGui, QtCore

from widgets.mainWindow import *

class MainWindowWidget(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self, collection, parent = None):
		super(MainWindowWidget, self).__init__()
		self.setupUi(self)
		self.splitter.setStretchFactor(1,1)
		self.collection = collection
		self.updateFilterList()
		self.connect(self.comboBoxFilter, QtCore.SIGNAL("currentIndexChanged(int)"),
		             self, QtCore.SLOT("updateFilterList(int)"))


	@QtCore.pyqtSlot(int)
	def updateFilterList(self, index = 0):
		self.listWidgetFilter.clear()
		#year
		if index == 0:
			list = self.collection.getAllYears()
			for l in list:
				self.listWidgetFilter.addItem(l)
			return
		#group
		if index == 1:
			list = self.collection.getAllGroups()
			for l in list:
				self.listWidgetFilter.addItem(l)
			return
		#category
		if index == 2:
			list = self.collection.getAllCategories()
			for l in list:
				self.listWidgetFilter.addItem(l)
			return
		#Designer
		if index == 3:
			list = self.collection.getAllDesigners()
			for l in list:
				self.listWidgetFilter.addItem(l)
			return
		#Engraver
		if index == 4:
			list = self.collection.getAllEngraver()
			for l in list:
				self.listWidgetFilter.addItem(l)
			return
