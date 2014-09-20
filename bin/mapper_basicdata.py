#!/usr/bin/env python
 
import sys
import re
import urllib

# this code is for formalize the initial log to basement

#the essential fields
essentials = ['time','word','uri', 'uid', 'baiduid', 'pu', 'ext', 'query', 'log_type']

pattern1=r'NOTICE: .*?\['
pattern2=r'word\[.*?\]'
pattern3=r'uri\[.*?\]'

'''
regexs = []
for fields in essentials[0:16] :
	regex = re.compile(r'%s\[.*?\]' % fields) 
	regexs.append(regex)
'''

# input comes from STDIN (standard input)
for line in sys.stdin:
	try:
		line = line.strip()
		essdict = {}.fromkeys(essentials,'')
		#time field
		m=re.match(pattern1,line)
		notice,time = m.group().split(': ',1)
		essdict['time'] = '20'+time[0:-2]	

		#word field
		m=re.search(pattern2,line)
		essdict['word']=line[m.start()+len('word')+1:m.end()-1]
		
		#search the uri
		m=re.search(pattern3,line)
		essdict['uri']=line[m.start()+len('uri')+1:m.end()-1]
		essdict['uri']=urllib.unquote(essdict['uri'])
		
		uricontent = essdict['uri']
		if uricontent:
			uridict = {}
			partContent = uricontent.split('&')
			for part in partContent:
				if part:
					kv = part.split('=')
					m=re.search(r'[_0-9a-z]+$',kv[0])
					kv[0] = kv[0][m.start():m.end()]
					uridict.setdefault(kv[0],kv[1])
#			essdict['query'] = uridict.pop('word','').decode('gbk').encode('utf-8')
			essdict['pu'] = uridict.pop('pu','')
			essdict['ext'] = uridict.pop('ext','')
			essdict['uid'] = uridict.pop('uid','')
			essdict['baiduid'] = uridict.pop('baiduid','')
		else:
			pass
		#for log_type
		judg1 = cmp(essdict['ext'],'appmobile')
		judg2 = re.match(r'aps',essdict['uid'])
		judg3 = re.search(r'osname@baiduappsearch',essdict['pu'])

		if (not judg1) or judg2 or judg3:
			essdict['log_type'] = 'client'
		else:
			essdict['log_type'] = 'msite'

		#union baiduid&time to one key for sorting:
		print "%s-%s\t%s\t%s" % (essdict['baiduid'],essdict['time'],essdict['word'],essdict['log_type'])

	except Exception,e:
		sys.stderr.write(str(e))
		continue
