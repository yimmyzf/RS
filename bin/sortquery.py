#!/usr/bin/env python

import sys

line=sys.stdin.readline().strip()
oldval,oldkeycpl=line.split(' ',1)
oldkey1,oldkey2=oldkeycpl.split('\t')
tmpdict={oldkeycpl:oldval}
sum=int(oldval)
for line in sys.stdin:
	line=line.strip()
	newval,newkeycpl=line.split(' ',1)
	newkey1,newkey2=newkeycpl.split('\t')

	if oldkey1==newkey1:
		if newkeycpl in tmpdict:
			tmpdict[newkeycpl] = int(newval)+ tmpdict[newkeycpl]
		else:
			tmpdict.setdefault(newkeycpl,int(newval))
		sum=sum+int(newval)
	else:
		if sum >= 20:
#			for key in tmpdict:
#				tmpdict[key]=float(tmpdict[key])/float(sum)
			sortedtuple=sorted(tmpdict.items(),key=lambda d:d[1],reverse=True)
			for i in range(len(sortedtuple)):
				weight=float(sortedtuple[i][1])/float(sum)
				print sortedtuple[i][0]+'\t'+str(sortedtuple[i][1])+'\t'+str(sum)+ '\t'+str(round(weight,5))
#			print str(sum)
			print
		else:
			pass
		sum=int(newval)
		oldkey1=newkey1
		tmpdict={newkeycpl:int(newval)}

