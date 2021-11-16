import socket
import threading
import os

def recieve_data():
    while True:
        data, addr = sock.recvfrom(1024)
        print (data.decode('utf-8'))

serv = '127.1.0.0', 1200

name = input("Your name: ")
print('write /exit to exit chat ')
if name == '':
        name = 'Guest' + str(random.randint(1000,9999))
        print('Your name is: ' + name)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('', 0))

sock.sendto((name+' connected to server').encode('utf-8'), serv)

threading.Thread(target = recieve_data).start()

while True:
    data = input()
    if '/exit' in data.lower():
        sock.sendto(('[' + name + ']: disconnected').encode('utf-8'), serv)
        sock.close()
        os._exit(1)
        break
    sock.sendto(('[' + name + ']: '+ data).encode('utf-8'), serv)
    
