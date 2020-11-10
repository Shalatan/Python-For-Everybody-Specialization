#http://py4e-data.dr-chuck.net/comments_1002505.json

import urllib.request, urllib.parse, urllib.error
import json
import ssl

#ignore ssl certificate error/for https sites
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Location: ')
print('Retrieving:',url)
data = urllib.request.urlopen(url,context=ctx).read()

count = 0
total = 0
jsonData = json.loads(data)

print('Retrieved',len(data),'charaters')

for item in jsonData['comments']:
    count = count + 1
    total = total + int(item['count'])
print('Count:',count)
print('Sum:',total)
