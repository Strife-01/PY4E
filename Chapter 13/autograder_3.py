import urllib.request, urllib.parse, urllib.error
import ssl
import json

url = input('Enter URL: ')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
js = json.loads(data)

count = 0
for comment in js['comments'] :
    try : count += int(comment['count'])
    except : continue

print(count)