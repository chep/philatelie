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


import re
import requests
from bs4 import BeautifulSoup

from stamp import *

#return stamp with information in url
def getStamp(url):
	content = requests.get(url)
	# if content.status_code == 200:
	# 	with open("/tmp/test2.html", 'w') as f:
	# 		for chunk in content.iter_content():
	# 			f.write(chunk)
	content.encoding = "utf-8"
	soup = BeautifulSoup(content.text)

	stamp = Stamp()
	stamp.title = soup.find("h1", class_="mx-title").string
	#remove "Timbre : "
	stamp.title = stamp.title[9:]

	temp = soup.find("strong", text = "Format d'imp")
	stamp.impFormat = " ".join(list(temp.next_elements)[1].split())

	temp = soup.find("strong", text = "Dents incluses")
	stamp.separationSize = " ".join(list(temp.next_elements)[1].split())

	temp = soup.find("strong", text = "Forme")
	stamp.shape = " ".join(list(temp.next_elements)[1].split())

	temp = soup.find("strong", text = "Phosphore")
	stamp.phosphoric = " ".join(list(temp.next_elements)[1].split())

	temp = soup.find("strong", text = "Impression")
	stamp.printing = " ".join(list(temp.next_elements)[1].split())

	temp = soup.find("strong", text = "Couleur")
	stamp.color = " ".join(list(temp.next_elements)[1].split())

	temp = soup.find("strong", text = "Valeur")
	stamp.value = " ".join(list(temp.next_elements)[1].split())

	temp = soup.find("strong", text = "Dentelure")
	stamp.separation = " ".join(list(temp.next_elements)[1].split())

	temp = soup.find("strong", text = "Emis en")
	stamp.issue = " ".join(list(temp.next_elements)[1].split())

	temp = soup.find("strong", text = [u"Quantité"])
	stamp.quantity = " ".join(list(temp.next_elements)[1].split())

	temp = soup.find("strong", text = "Dessinateur")
	stamp.designer = " ".join(list(temp.next_elements)[1].split())

	temp = soup.find("strong", text = "Graveur")
	stamp.engraver = " ".join(list(temp.next_elements)[1].split())

	temp = soup.find("strong", text = "Mise en page")
	stamp.layout = " ".join(list(temp.next_elements)[1].split())

	temp = soup.find("strong", text = "Mentions")
	stamp.credit = " ".join(list(temp.next_elements)[1].split())

	temp = soup.find("strong", text = "N° Philatelix")
	stamp.PhilatelixNum = " ".join(list(temp.next_elements)[1].split())

	temp = soup.find("strong", text = "N° Michel")
	stamp.MichelNum = " ".join(list(temp.next_elements)[1].split())

	temp = soup.find("strong", text = "Date d'émission")
	issueDate = " ".join(list(temp.next_elements)[1].split())
	if issueDate != "-":
		day, month, year =[y for y in issueDate.split("-")]
		stamp.issueDate = year + "-" + month + "-" + day

	temp = soup.find("strong", text = "Date de retrait")
	withdrawal = " ".join(list(temp.next_elements)[1].split())
	if withdrawal != "-":
		day, month, year =[y for y in withdrawal.split("-")]
		stamp.withdrawal = year + "-" + month + "-" + day

	temp = soup.find("dt", text = "Groupe")
	stamp.group = temp.next_sibling.next_sibling.string

	temp = soup.find("dt", text = "Catégorie")
#broken, html is wrong. This is an ugly fix
	stamp.category = temp.next_element.next_element.next_element.next_element

	image = soup.find("a", class_ = "mx-zoom")["href"]
	stamp.image = "/tmp/" + "TempStamp.jpg"
	r = requests.get(image)
	if r.status_code == 200:
		with open(stamp.image, 'wb') as f:
			for chunk in r.iter_content():
				f.write(chunk)

	stamp.identifier = " ".join(soup.find(text = re.compile("N\xb0WT")).split())

	temp = soup.find("dt", text = "Description")
	stamp.description = temp.next_sibling.next_sibling.string

	temp = soup.find("dt", text = "Commentaire")
	stamp.comment = temp.next_sibling.next_sibling.string

	return stamp

#fill stampList and return number of pages
def searchYear(year, page, stampList):
	if (page <= 1):
		content = requests.get("http://www.wikitimbres.fr/timbres/annee/" + str(year))
	else:
		content = requests.get("http://www.wikitimbres.fr/timbres/annee/"
		                       + str(year) + "/" + str(year) + "/" + str((page - 1) * 48))
	content.encoding = "utf-8"
	soup = BeautifulSoup(content.text)

	#stamps
	for tag in soup.find_all("div", class_ = "show_tooltip"):
		stampList.append(FoundStamp(tag["title"],
		                            tag.find("a")["href"],
		                            tag.find("img")["src"]))
	#pages
	nbPages = 1
	tag = soup.find("div", class_ = "pagination pagination-centered")
	pageList = tag.find_all("a")
	ok = False
	for link in reversed(pageList):
		#if we find ">>" it is the last page
		if link.contents == [u'>>']:
			nbPages = (int(link["href"].split("/")[-1]) / 48) + 1
			break;
		#if we find "#" we are on the last page
		if link["href"] == "#":
			nbPages = int(link.string)
			break;
		#If not, we must ignore ">" and find the last number
		if link.contents != [u'>']:
			nbPages = (int(link["href"].split("/")[-1]) / 48) + 1
			break;
	return nbPages


def getImage():
	return "plugins/wikitimbres.jpg"

def getLink():
	return """<a href="http://www.wikitimbres.fr">http://www.wikitimbres.fr</a>"""
