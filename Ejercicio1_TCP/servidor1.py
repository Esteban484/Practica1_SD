from socket import *

#Declaracion de puertos y IP del servidor
HOST = ''
PORT = 1234
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)#Inicialización
tcpSerSock.bind(ADDR)
tcpSerSock.listen()# Puerto de escucha


while True:
    print('esperando conexion')#Esperando la conexión del cliente
    tcpCliSock, addr = tcpSerSock.accept()
    print('conectado desde:{}'.format(addr))

    while True:
        data = tcpCliSock.recv(BUFSIZ).decode()# Clientes aceptados
        if data:
                print('recibido: {}'.format(data.encode('utf-8')))
        else:
                print("Sin conexion de cliente")
                break
        mensaje = "Hola, te saluda el servidor"
        tcpCliSock.send(mensaje.encode())# Enviar mensaje hacia el cliente
    tcpCliSock.close()
tcpSerSock.close()