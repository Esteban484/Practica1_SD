import socket
import sys

# Creacion del socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Vincular el socket con el puerto
server_address = ('', 1247)
print('Levantando servidor por el {} puerto {}'.format(*server_address))
sock.bind(server_address)

while True:
    #Recepcion de informacion desde cliente
    print('\nEsperando recibir mensaje')
    data, address = sock.recvfrom(4096)
    #Enviando respuesta al cliente
    print('reenviando {} bytes a {}'.format(
        len(data), address))
    print(data)
    #Envio de informacion de respaldo
    if data:
        sent = sock.sendto(data, address)
        print('enviando  {} bytes de vuelta {}'.format(
            sent, address))
