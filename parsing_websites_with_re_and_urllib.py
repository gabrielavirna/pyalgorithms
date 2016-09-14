import urllib.request
import urllib.parse
import re

url = 'http://pythonprogramming.net'
values = {'s':'basics',
          'submit':'search'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()

#print(respData)

'''I wanna parse everything between paragraph tags : <p> content content content </p>'''
paragraphs = re.findall(r'<p>(.*?)</p>',str(respData)) # any char, 0 or more repetitions, match 0 or 1 repetition

for eachP in paragraphs:
    print(eachP)

