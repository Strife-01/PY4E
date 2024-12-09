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

while True :
    data = mysock.recv(512)
    if len(data) < 1 : break
    print(data.decode(), end='')
