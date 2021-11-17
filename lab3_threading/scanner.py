import socket, threading, sys

ports = []

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        sock.connect((ip, port))
        ports.append(port)
        sock.close()
    except:
        return 0
        

ip = input('Enter IP: ')

part = 0
max = 10000
step = max // 40

for i in range(max):
    t1 = threading.Thread(target=scan_port, args=(ip, i))
    t1.start()

    if i > part:
        sys.stdout.write('.')
        sys.stdout.flush()
        part += step

sys.stdout.write(']\n')
print('scanning done')

if ports: 
    ports.sort()
    for port in range(len(ports)):
        print(f'Port {ports[port]} is free')
else:
    print('NO free ports')

