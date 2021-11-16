import socket, os

sock = socket.socket()
sock.bind(('',9090))

while True:
    sock.listen(1)
    print('socket is listening')
    conn, addr = sock.accept()
    print('connected ', addr)
    while conn:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            conn.send(data.upper().encode())
            if 'exit' in data.lower():
                addr = 0
                conn.close()
                break
        except:
            pass
