#!/usr/bin/env python
#! -*- coding:utf-8 -*-

import sys
import re
#reload(sys)
#sys.setdefaultencoding('utf-8')

def load_file(filename):
	f = open(filename,'r')
	lines = map(lambda x:x.strip(),f.readlines())
	return lines

class ridrept_handle(object):

	def __init__(self,specialfile,suffixfile):
		self.speciallist = load_file(specialfile)
		self.suffixlist = load_file(suffixfile)

	def special_replace(self,query):
		for suf in self.suffixlist:
			if query.endswith(suf):
				for spe in self.speciallist:
					if query == spe + suf:
						return spe
		return query

Chn_punct=['。','，','’','！','？','、','：']		
Eng_punct=['.',',','\'','!','?',',',':']
q_handle = ridrept_handle('special.data','suffix.data')
for line in sys.stdin:
	try:
		line = line.strip()
		for i in range(len(Chn_punct)):
			line = line.replace(Chn_punct[i],Eng_punct[i])
		query = line.strip(' ' ':' '.' ',' '\\' '!' '\'' '/' '-' '*' '?')
		query = query.lower()
		if len(query.decode('utf-8'))>10 and len(query)>20:
			continue
		query = q_handle.special_replace(query)
		print query
	except Exception,e:
		sys.stdout.write(str(e))
		print query
		continue

