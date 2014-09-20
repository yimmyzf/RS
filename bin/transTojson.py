#!/usr/bin/env python

import sys
import json

json.encoder.FLOAT_REPR = lambda x: format(x, '.5f')

tmpdict=dict(query="",weight="")
a=""
for line in sys.stdin:
	try:
		line = line.strip()
		if line == '':
			a=a.strip(',')
			print query+'\t{"value": ['+a+']}'
			a=""
		else:
			(query,rs,times,total,weight)=line.split('\t')
			tmpdict["query"]=rs
			tmpdict["weight"]=float(weight)
			encodedjson = json.dumps(tmpdict,ensure_ascii=False)
			a=a+','+encodedjson
#			jsonlist.append(encodedjson)
#			print jsonlist
	except Exception,e:
		sys.stdout.write(str(e))
		continue	
