#!/usr/bin/env python
##!./python/bin/python
import sys
import string
try:
	oldline=sys.stdin.readline().strip()
	baiduid,other=oldline.split('-',1)
	oldfields=other.split('\t')
	oldfields.insert(0,baiduid)
	#time1=datetime.datetime.strptime(oldfields[1],'%Y-%m-%d %H:%M:%S')
	time1 =string.atoi(oldfields[1][17:19])+60*string.atoi(oldfields[1][14:16])+3600*string.atoi(oldfields[1][11:13])
	flag1 = 0
	flag2 = 0
except Exception,e:
	sys.stderr.write(str(e))

for line in sys.stdin:
	try:
		newline=line.strip()
		baiduid,other=newline.split('-',1)
		newfields = other.split('\t')
		newfields.insert(0,baiduid)
#		time2=datetime.datetime.strptime(newfields[1],'%Y-%m-%d %H:%M:%S')
		time2 =string.atoi(newfields[1][17:19])+60*string.atoi(newfields[1][14:16])+3600*string.atoi(newfields[1][11:13])
		if cmp(oldfields[0],newfields[0]):
			flag1=0
		else:
			#time2=datetime.datetime.strptime(newfields[1],'%Y-%m-%d %H:%M:%S')
			#delta = (time2-time1).seconds
			if (time2-time1)>1800:
				#print oldline+('\n')
				flag1=0
			else:
				#print oldline
				flag1=1
#flag2=1
		if flag1 == 1 or flag2 == 1:
			print "%s\t%s\t%s\t%s" % (oldfields[0],oldfields[1],oldfields[2],oldfields[3])
		if flag1==0 and flag2==1:
			print 
		flag2=flag1
		oldline=newline
		oldfields=newfields
		time1=time2
	except Exception,e:
		sys.stderr.write(str(e))
		continue
