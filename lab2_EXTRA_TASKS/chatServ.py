import socket
import threading
import queue

def recieve_data(sock,recv_packets):
    while True:
        data, addr = sock.recvfrom(1024)
        recv_packets.put((data, addr))
        print (data, addr)

def run_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serv = '127.0.0.1' , 5555
    sock.bind(serv)
    print(f'Starting server on {serv[0]}')
    print(f'Start listening {serv[1]}')

    clients = set()
    recv_packets = queue.Queue()

    threading.Thread(target=recieve_data, args = (sock, recv_packets)).start()   

    while True:
        while not recv_packets.empty():
            
            data, addr = recv_packets.get()
            data = data.decode('utf-8')
            
            if  addr not in clients: 
                clients.add(addr)

            if '/exit' in data.lower():
                clients.remove(addr)
                continue

            for c in clients:
                if c != addr:
                    sock.sendto(data.encode('utf-8'), c)

    sock.close()

run_server()
