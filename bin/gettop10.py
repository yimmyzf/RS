#!/usr/bin/env python

import sys
'''
input format
q1 q2 ...
q1 q3 ...
q1 q4 ...

q8 q9 ...
q8 q7 ...
'''

sum=0
for line in sys.stdin:
	line = line.strip()
	if line=='':
		sum=0
		print
	else:
		sum=sum+1
		if sum <= 10:
			print line
