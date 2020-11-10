#http://py4e-data.dr-chuck.net/known_by_Ryden.html

import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore ssl certificate error/for https sites
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

count = int(input('Enter count:'))
position = int(input('Enter position:'))

tags = soup('a')
for i in range(count):
    newUrl = tags[position-1].get('href')
    print('Retrieving:',newUrl)
    a = newUrl.find('by_')
    b = newUrl.find('.html')
    html = urllib.request.urlopen(newUrl,context=ctx).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
print(newUrl[(a+3):b])
