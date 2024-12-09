import urllib.request, urllib.parse, urllib.error

URL = input('Enter URL - ')
fhand = urllib.request.urlopen(URL)

count = 0

while True :
    data = fhand.read(3000)
    if len(data) < 1 : break
    if len(data) <= 3000 : print(data.decode())
    count += len(data)

fhand.close()
print(count)
