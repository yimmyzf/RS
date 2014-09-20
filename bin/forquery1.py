import sys
import urllib

l=[]
for line in sys.stdin:
	line=line.strip('\n')
	if line=='':
		for i,q1 in enumerate(l):
			for q2 in l[i+1:]:
#				print urllib.quote(q1)+'\t'+urllib.quote(q2)
		   		print (q1)+'\t'+(q2) 	
		l=[]
	else:
		if line not in l:
			l.append(line)
