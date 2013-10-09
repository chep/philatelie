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
	s = Stamp(id = "pouet3", category="Test2", group="group", designer="designer3", engraver="engraver2", ownerNew = 1, ownerStamped = 2, issueDate = "1988-12-21")
	c.addStamp(s)
	s2 = Stamp(id = "pouet", category="Test2", group="group3", designer="designer", engraver="engraver", ownerNew = 1, issueDate = "2011-02-28")
	c.addStamp(s2)
	s3 = Stamp(id = "pouet2", category="Test", group="group2", designer="designer", engraver="engraver2", ownerStamped = 2, issueDate = "2001-08-28")
	c.addStamp(s3)
	s4 = Stamp(id = "pouet4", category="Test3", group="group", designer="designer3", engraver="engraver", ownerStamped = 5, issueDate = "2001-05-15")
	c.addStamp(s4)
	app = QtGui.QApplication(sys.argv)
	mw = MainWindowWidget(c)
	mw.show()
	app.exec_()

