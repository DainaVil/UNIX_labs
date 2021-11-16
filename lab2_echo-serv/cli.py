import socket

sock = socket.socket()
sock.connect(('localhost',9090))
while True:
    message = input()
    sock.send(message.encode())
    data = sock.recv(1024).decode()
    if 'EXIT' in data:
        sock.close()
        break
    print(data)

