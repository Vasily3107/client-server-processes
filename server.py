# server

import jsonpickle
import socket

IP = "127.0.0.1"
PORT = 12345
PACKET_LEN = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(1)

conn, addr = server.accept()

data = b''
while True:
    packet = conn.recv(PACKET_LEN)
    if not packet: break
    data += packet

data = jsonpickle.decode(data)

processes = data['processes']

for i, proc in enumerate(processes):
    print(f'{i:0>4}: {proc}')

conn.close()
server.close()