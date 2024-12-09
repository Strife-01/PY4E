import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
URL = input('Enter URL - ')
IP_SOCKET = URL.split('/')[2]
PORT = input('Enter PORT - ')
try :
    mysock.connect((IP_SOCKET, int(PORT)))
except :
    print('Invalid URL...')
    quit()
cmd = ('GET ' + URL + ' HTTP/1.0\r\n\r\n').encode()
mysock.send(cmd)

count = 0
while True :
    data = mysock.recv(3000)
    if len(data) < 1 : break
    count += len(data)
    if count <= 3000 : print(data.decode(), end='')

print('Retreaved', count, 'characters')
