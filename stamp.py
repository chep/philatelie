#!/bin/python2

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


class Stamp(object):
	def __init__(self):
		self.identifier = ""
		self.title = " "
		self.impFormat = " "
		self.separationSize = " "
		self.shape = " "
		self.phosphoric = " "
		self.printing = " "
		self.color = " "
		self.value = " "
		self.separation = " "
		self.issue = " "
		self.quantity = " "
		self.designer = " "
		self.engraver = " "
		self.layout = " "
		self.credit = " "
		self.PhilatelixNum = " "
		self.MichelNum = " "
		self.issueDate = " "
		self.withdrawal = " "
		self.group = " "
		self.category = " "
		self.image = "imageDefault.jpg"
		self.description = " "
		self.comment = " "

class FoundStamp(object):
	def __init__(self, title, url, imgUrl):
		self.title = title
		self.url = url
		self.imgUrl = imgUrl
