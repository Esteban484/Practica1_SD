import socket

host = "172.17.37.152"
port = 1235

sock = socket.socket()

sock.connect((host, port))

datos = sock.recv(4096)
print (datos.decode('utf-8'))



while True:


  message = input("digita un mensaje: ")
  sock.send(message.encode('utf-8'))




  if message == "salir":
        print("Adios")
        
        sock.close()
        break
