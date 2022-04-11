import socket

msgFromClient       = "Hola Esteban desde cliente UDP"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("172.17.36.74", 12456)
bufferSize          = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPClientSocket.sendto(bytesToSend, serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Recibido {}".format(msgFromServer[0])
print(msg)