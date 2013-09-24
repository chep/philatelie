#!/bin/python2

from PyQt4 import QtGui, QtCore
import sys

from stamp import *
from UI.stampWidget import *
from UI.webSearchWidget import *
from plugins import wikitimbres

class MainWindow(QtGui.QMainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		#s = Stamp()
		#wikitimbres.getStamp("http://www.wikitimbres.fr/timbres/8906/1913-centenaire-du-premier-saut-en-parachute-dadolphe-pegoud",
		#					 s)
		#self.stampWidget = StampWidget(self, s)
		self.webSearchWidget = WebSearchWidget(self)
		self.setCentralWidget(self.webSearchWidget)


if __name__=='__main__':
	app = QtGui.QApplication(sys.argv)
	mw = WebSearchWidget()
	mw.show()
	app.exec_()

