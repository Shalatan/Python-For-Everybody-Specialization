#http://py4e-data.dr-chuck.net/comments_1002504.xml

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
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
print('Retrieved',len(data),'charaters')
commentInfo = ET.fromstring(data)
lst = commentInfo.findall('comments/comment')
for item in lst:
    count = count + 1
    total = total + int(item.find('count').text)
print('Count:',count)
print('Sum:',total)
