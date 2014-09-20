#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

def load_file(filename):
	f = open(filename,'r')
	lines = map(lambda x:x.strip(),f.readlines())
	return lines


unsortedlist= load_file('re_forq')
sortedlist=sorted(unsortedlist)

for i in sortedlist:
	print i


