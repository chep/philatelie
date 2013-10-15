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

import os
import sqlite3

from stamp import *


CollectionVersion = "v0.1"


class Operation():
	equal = 0
	less = 1
	greater = 2
	between = 3

class Collection(object):
	def __init__(self, file = ".philatelie/collection.db"):
		if not os.path.exists(os.path.dirname(file)):
			os.makedirs(os.path.dirname(file))
		if not os.path.exists(os.path.dirname(file) + "/images"):
			os.makedirs(os.path.dirname(file) + "/images")
		self.connection = sqlite3.connect(file)
		self.checkTables()
		self.file = file

	def getDirectory(self):
		return os.path.dirname(self.file)

	def getImagesDirectory(self):
		return self.getDirectory() + "/images/"

	def checkTables(self):
		cur = self.connection.cursor()
		cur.execute("""SELECT name FROM sqlite_master WHERE type='table' """ +
		            """AND name='Version';""")
		if not cur.fetchone():
			cur.execute("""CREATE TABLE Version(number TEXT PRIMARY KEY);""")
			cur.execute("""INSERT INTO Version VALUES(?);""", (CollectionVersion,))
		else:
			cur.execute("""SELECT number FROM Version;""")
			res = cur.fetchone()
			if not res or res[0] != CollectionVersion:
				print "Invalid collection version: {0} instead of {1}. Exiting".format(res[0], CollectionVersion)
				exit()

		cur.execute("""SELECT name FROM sqlite_master WHERE type='table' """ +
		            """AND name='Category';""")
		if not cur.fetchone():
			cur.execute("""CREATE TABLE Category(name TEXT PRIMARY KEY);""")

		cur.execute("""SELECT name FROM sqlite_master WHERE type='table' """ +
		            """AND name='Designer';""")
		if not cur.fetchone():
			cur.execute("""CREATE TABLE Designer(name TEXT PRIMARY KEY);""")

		cur.execute("""SELECT name FROM sqlite_master WHERE type='table' """ +
		            """AND name='Group_';""")
		if not cur.fetchone():
			cur.execute("""CREATE TABLE Group_(name TEXT PRIMARY KEY);""")

		cur.execute("""SELECT name FROM sqlite_master WHERE type='table' """ +
		            """AND name='Engraver';""")
		if not cur.fetchone():
			cur.execute("""CREATE TABLE Engraver(name TEXT PRIMARY KEY);""")

		cur.execute("""SELECT name FROM sqlite_master WHERE type='table' """ +
		            """AND name='Stamp';""")
		if not cur.fetchone():
			cur.execute("CREATE TABLE Stamp(identifier TEXT PRIMARY KEY, " +
			            "title TEXT, impFormat TEXT, separationSize TEXT, " +
			            "shape TEXT, phosphoric TEXT, printing TEXT, " +
			            "color TEXT, value TEXT, separation TEXT, issue TEXT, " +
			            "quantity TEXT, designer TEXT REFERENCES Designer(name), " +
			            "engraver TEXT REFERENCES Engraver(name), layout TEXT, " +
			            "credit TEXT, philatelixNum TEXT, michelNum TEXT, " +
			            "issueDate DATE, withdrawal DATE, " +
			            "group_ TEXT REFERENCES Group_(name), " +
			            "category TEXT REFERENCES Category(name), image TEXT, " +
			            "description TEXT, comment TEXT, ownerNew INTEGER, " +
			            "ownerStamped INTEGER, ownerComment TEXT, " + 
			            "CONSTRAINT nbNotNull CHECK(ownerNew > 0 OR ownerStamped > 0));")
		self.connection.commit()


	def addStamp(self, stamp):
		cur = self.connection.cursor()

		cur.execute("""SELECT identifier FROM Stamp WHERE identifier = ?;""", (stamp.identifier,))
		if cur.fetchone():
			#TODO LOG
			return

		if stamp.category != "":
			cur.execute("""SELECT name FROM Category WHERE name = ?;""", (stamp.category,))
			rows = cur.fetchall()
			if len(rows) == 0:
				cur.execute("""INSERT INTO Category VALUES (?)""", (stamp.category,))

		if stamp.group != "":
			cur.execute("""SELECT name FROM Group_ WHERE name = ?;""", (stamp.group,))
			rows = cur.fetchall()
			if len(rows) == 0:
				cur.execute("""INSERT INTO Group_ VALUES (?)""", (stamp.group,))

		if stamp.designer != "":
			cur.execute("""SELECT name FROM Designer WHERE name = ?;""", (stamp.designer,))
			rows = cur.fetchall()
			if len(rows) == 0:
				cur.execute("""INSERT INTO Designer VALUES (?)""", (stamp.designer,))

		if stamp.engraver != "":
			cur.execute("""SELECT name FROM Engraver WHERE name = ?;""", (stamp.engraver,))
			rows = cur.fetchall()
			if len(rows) == 0:
				cur.execute("""INSERT INTO Engraver VALUES (?)""", (stamp.engraver,))

		cur.execute("""INSERT INTO Stamp VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""",
		            (stamp.identifier, stamp.title, stamp.impFormat, stamp.separationSize,
		             stamp.shape, stamp.phosphoric, stamp.printing, stamp.color,
		             stamp.value, stamp.separation, stamp.issue, stamp.quantity,
		             stamp.designer, stamp.engraver, stamp.layout, stamp.credit,
		             stamp.PhilatelixNum, stamp.MichelNum, stamp.issueDate,
		             stamp.withdrawal, stamp.group, stamp.category, stamp.image,
		             stamp.description, stamp.comment, stamp.ownerNew,
		             stamp.ownerStamped, stamp.ownerComment,))
		self.connection.commit()


	def delStamp(self, stamp):
		cur = self.connection.cursor()
		cur.execute("""DELETE FROM Stamp WHERE identifier = ?;""", (stamp.identifier,))
		self.connection.commit()

	def modifyStamp(self, newStamp):
		cur = self.connection.cursor()
		cur.execute("""UPDATE Stamp SET title = ?, """ + 
		            "impFormat = ?, separationSize = ?, " +
		            "shape = ?, phosphoric = ?, printing = ?, " +
		            "color  = ?, value = ?, separation = ?, issue = ?, " +
		            "quantity = ?, designer = ? , " +
		            "engraver = ? , layout = ?, " +
		            "credit = ?, philatelixNum = ?, michelNum = ?, " +
		            "issueDate = ?, withdrawal = ?, " +
		            "group_ = ? , " +
		            "category = ? , image = ?, " +
		            "description = ?, comment = ?, ownerNew = ?, " +
		            "ownerStamped = ?, ownerComment = ? " + 
		            "WHERE identifier = ?;",
		            (newStamp.title, newStamp.impFormat, newStamp.separationSize,
		             newStamp.shape, newStamp.phosphoric, newStamp.printing, newStamp.color,
		             newStamp.value, newStamp.separation, newStamp.issue, newStamp.quantity,
		             newStamp.designer, newStamp.engraver, newStamp.layout, newStamp.credit,
		             newStamp.PhilatelixNum, newStamp.MichelNum, newStamp.issueDate,
		             newStamp.withdrawal, newStamp.group, newStamp.category, newStamp.image,
		             newStamp.description, newStamp.comment, newStamp.ownerNew,
		             newStamp.ownerStamped, newStamp.ownerComment,newStamp.identifier))
		self.connection.commit()

	def getAllYears(self):
		cur = self.connection.cursor()
		cur.execute("""SELECT DISTINCT strftime('%Y', issueDate) AS year FROM Stamp ORDER BY year;""")
		rows = []
		for r in cur.fetchall():
			rows.append(r[0])
		return rows

	def getAllGroups(self):
		cur = self.connection.cursor()
		cur.execute("""SELECT DISTINCT group_ FROM Stamp ORDER BY group_;""")
		rows = []
		for r in cur.fetchall():
			rows.append(r[0])
		return rows

	def getAllCategories(self):
		cur = self.connection.cursor()
		cur.execute("""SELECT DISTINCT category FROM Stamp ORDER BY category;""")
		rows = []
		for r in cur.fetchall():
			rows.append(r[0])
		return rows

	def getAllDesigners(self):
		cur = self.connection.cursor()
		cur.execute("""SELECT DISTINCT designer FROM Stamp ORDER BY designer;""")
		rows = []
		for r in cur.fetchall():
			rows.append(r[0])
		return rows

	def getAllEngraver(self):
		cur = self.connection.cursor()
		cur.execute("""SELECT DISTINCT engraver FROM Stamp ORDER BY engraver;""")
		rows = []
		for r in cur.fetchall():
			rows.append(r[0])
		return rows

	def getStampsYear(self, year):
		cur = self.connection.cursor()
		cur.execute("""SELECT * FROM Stamp WHERE strftime('%Y', issueDate) = ?;""", (str(year),))
		result = cur.fetchall()
		return self.result2StampList(result)

	def getStampsGroup(self, group):
		cur = self.connection.cursor()
		cur.execute("""SELECT * FROM Stamp WHERE group_ = ?;""", (group,))
		result = cur.fetchall()
		return self.result2StampList(result)

	def getStampsCategory(self, category):
		cur = self.connection.cursor()
		cur.execute("""SELECT * FROM Stamp WHERE category = ?;""", (category,))
		result = cur.fetchall()
		return self.result2StampList(result)

	def getStampsDesigner(self, designer):
		cur = self.connection.cursor()
		cur.execute("""SELECT * FROM Stamp WHERE designer = ?;""", (designer,))
		result = cur.fetchall()
		return self.result2StampList(result)

	def getStampsEngraver(self, engraver):
		cur = self.connection.cursor()
		cur.execute("""SELECT * FROM Stamp WHERE engraver = ?;""", (engraver,))
		result = cur.fetchall()
		return self.result2StampList(result)

	def getStampIdentifier(self, id):
		cur = self.connection.cursor()
		cur.execute("""SELECT * FROM Stamp WHERE identifier = ?;""", (id,))
		result = cur.fetchone()
		if not result == None:
			identifier, title, \
			impFormat, separationSize, \
			shape, phosphoric, printing, \
			color, value, separation, issue, \
			quantity, designer, \
			engraver, layout, \
			credit, philatelixNum, michelNum, \
			issueDate, withdrawal, \
			group, category, image, \
			description, comment, ownerNew, \
			ownerStamped, ownerComment = result
			return Stamp(identifier, title,
			             impFormat, separationSize,
			             shape, phosphoric, printing,
			             color, value, separation, issue,
			             quantity, designer,
			             engraver, layout,
			             credit, philatelixNum, michelNum,
			             issueDate, withdrawal,
			             group, category, image,
			             description, comment, ownerNew,
			             ownerStamped, ownerComment)
		else:
			return None

	def getStampTitle(self, title):
		cur = self.connection.cursor()
		cur.execute("""SELECT * FROM Stamp WHERE title = ?;""", (unicode(title),))
		result = cur.fetchall()
		return self.result2StampList(result)

	def getStampFilters(self, operation = None, yearMin = None, yearMax = None,
	                    group = None, category = None, designer = None,
	                    engraver = None, keyword = None):
		where = False
		params = ()
		request = "SELECT * FROM Stamp "

		if operation == Operation.equal:
			operation = "="
		elif operation == Operation.less:
			operation = "<"
		else:
			operation = ">="

		if yearMin != None:
			request = request + "WHERE "
			where = True
			request = request + "strftime('%Y', issueDate) {op} ? ".format(op = operation)
			params = params + (str(yearMin),)

		if yearMax != None:
			if not where:
				request = request + "WHERE "
				where = True
			else:
				request = request + "AND "
			request = request + "strftime('%Y', issueDate) < ? "
			params = params + (str(yearMax),)

		if group != None:
			if not where:
				request = request + "WHERE "
				where = True
			else:
				request = request + "AND "
			request = request + "group_ = ? "
			params = params + (group,)

		if category != None:
			if not where:
				request = request + "WHERE "
				where = True
			else:
				request = request + "AND "
			request = request + "category = ? "
			params = params + (category,)

		if designer != None:
			if not where:
				request = request + "WHERE "
				where = True
			else:
				request = request + "AND "
			request = request + "designer = ? "
			params = params + (designer,)

		if engraver != None:
			if not where:
				request = request + "WHERE "
				where = True
			else:
				request = request + "AND "
			request = request + "engraver = ? "
			params = params + (engraver,)

		if keyword != None:
			if not where:
				request = request + "WHERE "
				where = True
			else:
				request = request + "AND "
			request = request + "title LIKE ? "
			params = params + ("%" + keyword + "%",)

		request = request + ";"
		cur = self.connection.cursor()
		cur.execute(request, params)
		result = cur.fetchall()
		return self.result2StampList(result)

	def result2StampList(self, result):
		list = []
		for identifier, title, \
		    impFormat, separationSize, \
		    shape, phosphoric, printing, \
		    color, value, separation, issue, \
		    quantity, designer, \
		    engraver, layout, \
		    credit, philatelixNum, michelNum, \
		    issueDate, withdrawal, \
		    group, category, image, \
		    description, comment, ownerNew, \
		    ownerStamped, ownerComment in result:
			s = Stamp(identifier, title,
			          impFormat, separationSize,
			          shape, phosphoric, printing,
			          color, value, separation, issue,
			          quantity, designer,
			          engraver, layout,
			          credit, philatelixNum, michelNum,
			          issueDate, withdrawal,
			          group, category, image,
			          description, comment, ownerNew,
			          ownerStamped, ownerComment)
			list.append(s)
		return list

