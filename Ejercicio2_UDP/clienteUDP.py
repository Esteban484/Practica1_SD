import socket
import sys

# Creacion del  socket UDP 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Direccion del servidor
server_address = ('172.17.37.156', 1247)
message = b'Este mensaje se envia al servidor.'

try:

    #Envio de informacion
    print('enviando {!r}'.format(message))
    sent = sock.sendto(message, server_address)

    # Recibiendo respuesta
    print('esperando respuesta')
    data, server = sock.recvfrom(4096)
    print('recibido {!r}'.format(data))

finally:
    print('cerrando socket')
    sock.close()