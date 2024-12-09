import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET

serviceurl = 'http://py4e-data.dr-chuck.net/comments_1899226.xml'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = serviceurl
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
# print(data.decode())
tree = ET.fromstring(data)

counts = tree.findall('.//count')
summ = 0
for count in counts :
    try : summ += int(count.text)
    except : continue

print(summ)
