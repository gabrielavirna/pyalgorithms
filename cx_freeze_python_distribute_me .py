#get cx_Freeze: http://cx-freeze.sourceforge.net/
#Here, we'll use the urllib + re tutorial where we parsed Pythonprogramming.net

import urllib.request
import urllib.parse
import re
import time


url = 'http://pythonprogramming.net'
values = {'s' : 'basics',
          'submit' : 'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8') # data should be bytes
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))

for eachParagraph in paragraphs:
    print(eachParagraph)

time.sleep(15)