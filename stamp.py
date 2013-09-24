#!/bin/python2


# "http://www.wikitimbres.fr/timbres/8906/1913-centenaire-du-premier-saut-en-parachute-dadolphe-pegoud")
#content = requests.get("http://www.wikitimbres.fr/timbres/3752/2011-30e-anniversaire-de-la-mise-en-service-du-tgv")


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
