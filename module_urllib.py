# allows you to access the internet
import urllib.request
import urllib.parse # parse values to our POST request

'''GET'''
#x = urllib.request.urlopen("https://www.google.com")
#print(x.read())

'''POST to search word 'basic' at url:https://pythonprogramming.net'''

#x = urllib.request.urlopen("https://pythonprogramming.net/search/?q=basic")
#print(x.read())'''

'''OR'''
url = 'http://pythonprogramming.net' # base url
values = {'s':'basic',               # dictionary
          'submit':'search'}
data = urllib.parse.urlencode(values)# we encoded from website data that we wanna POST in
data = data.encode('utf-8')          # puts data in bites
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)  # visit the url
respData = resp.read()              #
print(respData)



'''Websites with forbidden access -> use their API'''

try:
    y = urllib.request.urlopen('https://www.google.com/search?q=test') # q= query
    print(y.read())
except Exception as e:
    print(str(e))


try:
    url2 = 'https://www.google.com/search?q=test'
    headers = {} #headers=data you're sending everytime you're visiting a site: who you are,your IP,browser,OS
    headers['User-Agent'] =  'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'#Web-Agent=type of browser
    req2 = urllib.request.Request(url2,headers=headers)
    resp2 = urllib.request.urlopen(req2)
    respData2 = resp2.read()
    saveFile = open('module_urllib_withHeaders.txt','w')
    saveFile.write(str(respData2))
    saveFile.close()
except Exception as e:
    print(str(e))
