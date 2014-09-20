#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')

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

kwddict = {}
relist = []
for line in open("result"):
	line = line.strip()
	if line=='':
		kwddict.setdefault(searchquery,relist)
		relist = []
	else:
		(searchquery,rsline) = line.split('\t',1)
		relist.append(rsline)

Chn_punct=['。','，','’','！','？','、','：'] 
Eng_punct=['.',',','\'','!','?',',',':']
q_handle = ridrept_handle('special.data','suffix.data')
for line in open('orikey'):
	srchquery = line.strip()
	changedquery=srchquery
	for i in range(len(Chn_punct)):
		changedquery = changedquery.replace(Chn_punct[i],Eng_punct[i])
	changedquery = changedquery.strip(' ' ':' '.' ',' '\\' '!' '\'' '/' '-' '*' '?')
	changedquery = changedquery.lower()
	if len(changedquery.decode('utf-8'))>20:
		continue
	changedquery = q_handle.special_replace(changedquery)
	if changedquery in kwddict:
		for rs in kwddict[changedquery]:
			print srchquery+'\t'+rs
		print

