import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('172.17.37.156', 1247)
message = b'Este mensaje se envia al servidor.'

try:

    # Send data
    print('enviando {!r}'.format(message))
    sent = sock.sendto(message, server_address)

    # Receive response
    print('esperando respuesta')
    data, server = sock.recvfrom(4096)
    print('recibido {!r}'.format(data))

finally:
    print('cerrando socket')
    sock.close()
