#!/bin/python2
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

