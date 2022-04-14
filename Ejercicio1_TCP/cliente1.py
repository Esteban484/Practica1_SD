# -*- coding:utf-8 -*-
from socket import *

#Declaracion de puertos y IP del servidor
HOST = '172.17.37.156'
PORT = 7589
BUFSIZ = 1024
#Direccion a a la que se realizar la conexion junto con su puerto
ADDR = (HOST, PORT)

#Creacion del socket tcp
tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    #envio de mensaje para el servidor
    sdata = input('> ')
    #Envio de mensaje para el servidor
    tcpCliSock.send(sdata.encode('utf-8'))
    if not sdata:
        break
    tcpCliSock.send(sdata.encode())

    #Recepción de mensaje de parte del servidor
    rdata = tcpCliSock.recv(BUFSIZ).decode()
    if not rdata:
        break
    print(rdata)
tcpCliSock.close()