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
from UI.mainWindowWidget import *
from plugins import wikitimbres
from collectionManagement.collection import *


if __name__=='__main__':
	c = Collection()
	# for i in range(30):
	# 	s = Stamp(id = "pouet" + str(i), title="pouet3", category="Test2", group="group" + str(i), designer="designer3", engraver="engraver2", ownerNew = 1, ownerStamped = 2, issueDate = "1988-12-21", description = "Plop")
	# 	c.addStamp(s)
	# s2 = Stamp(id = "pouet", title="pouet", category="Test2", group="group3", designer="designer", engraver="engraver", ownerNew = 1, issueDate = "2011-02-28", description = unicode(u"Description avec des accents: dédé, prêt, à l'heure"))
	# c.addStamp(s2)
	# s3 = Stamp(id = "pouet2", title="pouet2", category="Test", group="group2", designer="designer", engraver="engraver2", ownerStamped = 2, issueDate = "2001-08-28", description = "Whaou trop classe")
	# c.addStamp(s3)
	# s4 = Stamp(id = "pouet4", title="pouet4", category="Test3", group="group", designer="designer3", engraver="engraver", ownerStamped = 5, issueDate = "2001-05-15", image="/home/chep/Images/Megaman8bit.png", description = "Ceci n'est pas un megaman", withdrawal = "2002-02-13")
	# c.addStamp(s4)


	#QT
	app = QtGui.QApplication(sys.argv)
	locale = QtCore.QLocale.system().name()
	qtTranslator = QtCore.QTranslator()
	if qtTranslator.load("qt_" + locale):
		app.installTranslator(qtTranslator)
	appTranslator = QtCore.QTranslator()
	if appTranslator.load("philatelie_" + locale):
		app.installTranslator(appTranslator)
	mw = MainWindowWidget(c)
	mw.show()
	app.exec_()

