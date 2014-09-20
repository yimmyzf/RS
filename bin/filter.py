#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def singleWordFilter(str):
	try:
		utf8_l=len(str.decode('utf-8'))
		if utf8_l==1:
			return True
		else:
			return False
	except:
		return None
	
	
class commonFilter:

	def __init__(self):
		self.keywords = []

	def add(self,keyword):
		if not isinstance(keyword,unicode):
			keyword = keyword.decode('utf-8')
		keyword = keyword.lower()
		self.keywords.append(keyword)

	def parse(self,path):
		with open(path) as f:
			for keyword in f:
				self.add(keyword.strip())

	def filter(self,message):
		if not isinstance(message,unicode):
			message = message.decode('utf-8')
		message = message.lower()
		for word in self.keywords:
			if word in message:
				return True
			else:
				continue
		return False

class accuFilter:
	
	def __init__(self):
		self.keywords = set([])

	def add(self,keyword):
		if not isinstance(keyword,unicode):
			keyword = keyword.decode('utf-8')
		keyword = keyword.lower()
		self.keywords.add(keyword)	
	def parse(self,path):
		for keyword in open(path):
			self.add(keyword.strip())
	
	def filter(self,message):
		if not isinstance(message,unicode):
			message = message.decode('utf-8')
		message = message.lower()
		if message in self.keywords:
			return True
		else:
			return False	

if __name__ == "__main__":

	ft1 = accuFilter()
	ft2 = commonFilter()
	ft3 = commonFilter()
	ft1.parse("sexavoid_precise")
	ft2.parse("sexavoid_common")
	ft3.parse("blackword.txt")
	with open("out1") as f1:
		for line in f1:
			line = line.strip()
			if line=='':
				print
			else:
				attr = line.split('\t')
				if singleWordFilter(attr[1]) or ft1.filter(attr[1]):
					pass
				else:
					if ft2.filter(attr[1]) or ft3.filter(attr[1]):
						pass
					else:
						print line
				
