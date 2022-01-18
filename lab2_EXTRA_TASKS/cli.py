import socket
from users import names, passwords
import os

name = 'daina'
passw = '000'

name = input('name: ')
while (name not in names) and (name != 'exit'):
    print('wrong name')
    name = input('name: ')

if name == 'exit':
    exit()

passw = input('password: ')
while (passw not in passwords) or (passwords.index(passw) != names.index(name)):
    print('wrong password')
    passw = input('password: ')

host, port = (input('input host and port: ').split())
port = int(port)

sock = socket.socket()

try:
    sock.connect((host, port))
    print('connected to server')
except:
    print('connection error')
    sock.connect(('localhost', 9090))
    print('connected to localhost, 9090')


while True:
    message = input()
    sock.send(message.encode())
    data = sock.recv(1024).decode()
    if 'EXIT' in data:
        sock.close()
        break
    print(data)

