import re
import requests
from PyQt4 import QtGui, QtCore

from widgets.webSearchWidget import *
from stampWidget import *
import plugins
from stamp import *

class WebSearchButton(QtGui.QPushButton):
	def __init__(self, parent, stampUrl, imgUrl, plugin):
		super(WebSearchButton, self).__init__(parent)
		self.stampUrl = stampUrl
		self.plugin = plugin
		pixmap = QtGui.QPixmap(imgUrl)
		self.setIcon(QtGui.QIcon(pixmap))
		self.setIconSize(pixmap.size())
		self.connect(self, QtCore.SIGNAL("clicked()"),
		             self, QtCore.SLOT("click()"))

	@QtCore.pyqtSlot()
	def click(self):
		stamp = self.plugin.getStamp(self.stampUrl)
		sw = StampWidget(stamp)
		sw.exec_()


class WebSearchWidget(QtGui.QDialog, Ui_webSearchWidget):
	startSearch = QtCore.pyqtSignal()

	def __init__(self, parent = None):
		super(WebSearchWidget, self).__init__(parent)
		self.setupUi(self)
		self.connect(self.pushButtonSearch, QtCore.SIGNAL("clicked()"),
		             self, QtCore.SLOT("searchSlot()"))
		self.connect(self.pushButtonClose, QtCore.SIGNAL("clicked()"),
		             self, QtCore.SLOT("close()"))
		self.connect(self.spinBoxPage, QtCore.SIGNAL("valueChanged(int)"),
		             self, QtCore.SLOT("spinBoxChange(int)"))
		self.connect(self, QtCore.SIGNAL("startSearch()"),
		             self, QtCore.SLOT("search()"))

		#plugin list
		self.plugins = dir(plugins)
		for i in reversed(range(len(self.plugins))):
			if re.match("__.*__", self.plugins[i]):
				self.plugins.pop(i)
		for i in self.plugins:
			self.comboBoxPlugin.addItem(i)
			#wikitimbres by default
			if i == "wikitimbres":
				self.comboBoxPlugin.setCurrentIndex(self.comboBoxPlugin.count() - 1)

	@QtCore.pyqtSlot()
	def searchSlot(self):
		self.clearResult()
		self.setButtonsEnabled(False)
		self.spinBoxPage.setValue(1)
		QtGui.QApplication.processEvents()
		self.startSearch.emit()

	def clearResult(self):
		for i in reversed(range(self.gridLayoutFound.count())):
			self.gridLayoutFound.itemAt(i).widget().setParent(None)

	def setButtonsEnabled(self, enabled):
		self.pushButtonClose.setEnabled(enabled)
		self.pushButtonSearch.setEnabled(enabled)

	@QtCore.pyqtSlot(int)
	def spinBoxChange(self, value):
		self.setButtonsEnabled(False)
		self.clearResult()
		QtGui.QApplication.processEvents()
		self.startSearch.emit()

	@QtCore.pyqtSlot()
	def search(self):
		self.clearResult()
		plugin = getattr(plugins, self.plugins[self.comboBoxPlugin.currentIndex()])

		stamps = []
		nbPages = 1
		try:
			nbPages = plugin.searchYear(self.lineEditYear.text(),
			                            self.spinBoxPage.value(), stamps)
		except:
			#TODO LOG
			pass

		#page number:
		self.labelNbPages.setText(" / " + str(nbPages))
		self.spinBoxPage.setMaximum(nbPages)

		count = 5
		for stamp in stamps:
			frame = QtGui.QFrame(self.scrollAreaFound)
			self.gridLayoutFound.addWidget(frame, count / 5, count % 5)
			count += 1

			layout = QtGui.QVBoxLayout()
			frame.setLayout(layout)

			#button:
			r = requests.get(stamp.imgUrl)
			image = "/tmp/stampImage" + str(count) + ".jpg"
			if r.status_code == 200:
				with open(image, 'w') as f:
					for chunk in r.iter_content():
						f.write(chunk)
			else:
				image = "imageDefault.jpg"
			button = WebSearchButton(self.scrollAreaFound, stamp.url, image, plugin)
			button.setMinimumHeight(200)
			button.setMaximumWidth(300)
			layout.addWidget(button)

			#title
			label = QtGui.QLabel(self.scrollAreaFound)
			label.setMaximumWidth(300)
			label.setWordWrap(True);
			label.setText(stamp.title)
			layout.addWidget(label)

		self.setButtonsEnabled(True)