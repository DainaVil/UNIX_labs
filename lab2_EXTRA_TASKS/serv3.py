import socket, os
import logging
from datetime import datetime
from scanner import get_free_ports

logging.basicConfig(filename='server.log')
log = logging.getLogger('echo')
log.setLevel(logging.DEBUG)
f = 0

sock = socket.socket()
shost, sport = 'localhost', 9090
try: 
    sock.bind((shost, sport))
    f = 1
except:
    ports = get_free_ports(shost)
    for p in ports:
        try:
            sock.bind((shost, p))
            sport = p
            print(sport)
            break
        except:
            pass

while True:
    sock.listen(1)
    print(f'listeting to {shost, sport}')
    log.info(f'listeting to {shost, sport}')
    conn, addr = sock.accept()
    print('connected ', addr)
    log.info(f' new connection {conn, addr} {datetime.now()}')
    while conn:
        try:
            data = conn.recv(1024).decode()
            log.info(f' new message {data} {datetime.now()}')
            if not data:
                break
            conn.send(data.upper().encode())
            if 'exit' in data.lower():
                addr = 0
                conn.close()
                log.info(f' disconnected {conn, addr} {datetime.now()}')
                break
        except KeyboardInterrupt as k:
            print(k)
            print("stop server")
            exit()
