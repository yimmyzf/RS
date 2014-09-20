#!/usr/bin/env python

import sys
import linecache
import random

kwddict = {}
relist = []
for line in open("middleout"):
	line = line.strip()
	if line=='':
		kwddict.setdefault(searchquery,relist)
		relist = []
	else:
		tmplist = line.split('\t')
		searchquery = tmplist[0]
		relist.append(tmplist[1])
	
tmpsum = 0

def fillto(rslist,sum,keyquery,relative):
	for rsq in rslist:
		i = 0
		if rsq in kwddict: 
			tmplist = kwddict[rsq]
			tmplistlen = len(tmplist)
			while sum < 10 and i<tmplistlen:
				if (tmplist[i] in rslist) or tmplist[i]==keyquery:
					i = i+1	
					continue
				else:
					print keyquery+'\t'+tmplist[i]+'\t'+relative+'\t'+relative+'\t'+relative
					sum = sum + 1
					rslist.append(tmplist[i])
					i = i+1
		else:
			pass
		if sum>=10:
			break
			
	while sum < 10:
		randnum = random.randint(1,100)#random a number between 1 and 100 
		randquery = linecache.getline("top.tmp", randnum)#get the query
		randquery = randquery.strip()
		if randquery not in rslist:
			print keyquery+'\t'+randquery+'\t'+relative+'\t'+relative+'\t'+relative
			sum = sum+1
		else: 
			pass
rslist=[]
for line in sys.stdin:
	line = line.strip()
	if line == '':
		if tmpsum != 10:
			fillto(rslist,tmpsum,keyquery,relative)
		else:
			pass
		print
		rslist=[]
		tmpsum = 0
	else:
		tmpsum = tmpsum + 1
		rsquery=line.split('\t')[1]
		keyquery = line.split('\t')[0]
		relative = line.split('\t')[4]
		rslist.append(rsquery)
		print line
		
