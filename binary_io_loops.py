PACKET_LEN = 1024


def loopsend(client, data) -> None:
    for i in range(0, len(data), PACKET_LEN):

        packet = data[i : i + PACKET_LEN]

        client.sendall(packet)


def looprecv(connection) -> bytes:
    data = b''

    while True:
        packet = connection.recv(PACKET_LEN)

        if not packet: break

        data += packet

    return data