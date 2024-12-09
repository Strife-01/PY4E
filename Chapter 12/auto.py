import sys
sys.path.append('beautifulsoup4')
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
position_seeked = int(input('Position seeked: '))
repeat_times = int(input('Reapeat: ')) + 1

answer = ""

while repeat_times > 0 :
    count = 0
    print('Retreaving:', url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags :
        count += 1
        if count == position_seeked :
            repeat_times -= 1
            try : 
                answer = re.findall('known_by_(.*)?.html', url)[0]
                url = tag.get('href', None)
            except : quit()
            break            

print(answer)

