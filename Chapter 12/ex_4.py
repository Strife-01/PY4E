import sys
sys.path.append('beautifulsoup4')
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = 0

sum_num = 0
tags = soup('span')
for tag in tags :
    try :
        sum_num += int(tag.contents[0])
    except : continue

print(sum_num)
