import socket, os


sock = socket.socket()
sock.bind(('',8080))
sock.listen(1)
conn, addr = sock.accept()

print('connected ', addr)

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    conn.send(data.upper().encode())
    if 'exit' in data.lower():
        conn.close()
        os._exit(0)
