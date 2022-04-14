import socket

host = "172.17.37.152"
port = 1235

#Creacion del socket
sock = socket.socket()

#Conexion de socket con el puerto y la ip
sock.connect((host, port))

datos = sock.recv(4096)
print (datos.decode('utf-8'))


#While infinito para poder enviar mensajes ilimtados
while True:

#Envio de mensajes al servidor
  message = input("digita un mensaje: ")
  sock.send(message.encode('utf-8'))



  #Salir del while para finalizar conexion
  if message == "salir":
        print("Adios")
        
        sock.close()
        break