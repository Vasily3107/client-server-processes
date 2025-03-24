# client

from binary_io_loops import loopsend
import psutil
import jsonpickle
import socket

IP = "127.0.0.1"
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))

data = jsonpickle.encode({'processes': list(psutil.process_iter())}).encode()

loopsend(client, data)

print('sent all')

client.close()