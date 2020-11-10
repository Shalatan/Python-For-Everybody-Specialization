#http://py4e-data.dr-chuck.net/comments_1002502.html

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

total = 0
count = 0
tags = soup('span')
for tag in tags:
    count  = count + 1
    total = total + int(tag.string)
print("Count",count)
print("Sum",total)
