from socket import socket


def loopsend(client: socket, binary_data: bytes, PACKET_LEN = 1024) -> None:

    for i in range(0, len(binary_data), PACKET_LEN):

        packet = binary_data[i : i + PACKET_LEN]

        client.sendall(packet)


def looprecv(connection: socket, PACKET_LEN = 1024) -> bytes:
    binary_data = b''

    while True:
        packet = connection.recv(PACKET_LEN)

        if not packet: break

        binary_data += packet

    return binary_data