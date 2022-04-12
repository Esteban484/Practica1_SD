import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('', 1247)
print('Levantando servidor por el {} puerto {}'.format(*server_address))
sock.bind(server_address)

while True:
    print('\nEsperando recibir mensaje')
    data, address = sock.recvfrom(4096)

    print('reenviando {} bytes a {}'.format(
        len(data), address))
    print(data)

    if data:
        sent = sock.sendto(data, address)
        print('enviando  {} bytes de vuelta {}'.format(
            sent, address))
