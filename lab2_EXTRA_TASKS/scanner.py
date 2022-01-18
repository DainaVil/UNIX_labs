import socket, threading, sys

def get_free_ports(ip):
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

    max = 10000

    for i in range(max):
        t1 = threading.Thread(target=scan_port, args=(ip, i))
        t1.start()

    return ports

