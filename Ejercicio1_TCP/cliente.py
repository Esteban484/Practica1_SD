#print("Holamundo")
import socket
HOST="172.17.36.74"
PORT=14256
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall(b"Hola Esteban desde el cliente")
    data=s.recv(1024)
    print(f"recibido {data!r}")
