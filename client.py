# client

import psutil
import jsonpickle
import socket

IP = "127.0.0.1"
PORT = 12345
PACKET_LEN = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))

data = jsonpickle.encode({'processes': list(psutil.process_iter())}).encode()


for i in range(0, len(data), PACKET_LEN):
    packet = data[i : i + PACKET_LEN]
    client.sendall(packet)

print('sent all')

client.close()