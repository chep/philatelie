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


class Stamp(object):
	def __init__(self, id = " ", title = "-", impFormat = "-",
	             separationSize = "-", shape = "-", phosphoric = "-",
	             printing = "-", color = "-", value = "-", separation = "-",
	             issue = "-", quantity = "-", designer = "-", engraver = "-",
	             layout = "-", credit = "-", PhilatelixNum = "-",
	             MichelNum = "-", issueDate = "-", withdrawal = "-",
	             group = "-", category = "-", image = "imageDefault.jpg",
	             description = "-", comment = "-", ownerNew = 0,
	             ownerStamped = 0, ownerComment = ""):
		self.identifier = id
		self.title = title
		self.impFormat = impFormat
		self.separationSize = separationSize
		self.shape = shape
		self.phosphoric = phosphoric
		self.printing = printing
		self.color = color
		self.value = value
		self.separation = separation
		self.issue = issue
		self.quantity = quantity
		self.designer = designer
		self.engraver = engraver
		self.layout = layout
		self.credit = credit
		self.PhilatelixNum = PhilatelixNum
		self.MichelNum = MichelNum
		self.issueDate = issueDate
		self.withdrawal = withdrawal
		self.group = group
		self.category = category
		self.image = "imageDefault.jpg"
		self.description = description
		self.comment = comment
		self.ownerNew = ownerNew
		self.ownerStamped = ownerStamped
		self.ownerComment = ownerComment

class FoundStamp(object):
	def __init__(self, title, url, imgUrl):
		self.title = title
		self.url = url
		self.imgUrl = imgUrl
