import socket
import threading

host = ""
port = 7458
ThreadCount = 0
#Creacion del sockey
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Creando")
#Vinculacion del socket con el puerto
sock.bind((host, port))
sock.listen(1)
print ("socket escuchando en este momento")

#Se define una funcion para la recepcion de informacion cliente
def worker(*args):
    conn = args[0]
    addr = args[1]
    try:
        print('conexion con {}.'.format(addr))
        conn.send("server: Conectado".encode('UTF-8'))
        while True:
            datos = conn.recv(4096)
            if datos:
                print('recibido: {}'.format(datos.decode('utf-8')))

            else:
                print("Sin conexion de cliente")
                break
    finally:
        conn.close()
#Se comienzan a crear hilos con cada usuario que ingresa
while 1:
    conn, addr = sock.accept()
    threading.Thread(target=worker, args=(conn, addr)).start()
    ThreadCount += 1
    print('Numero de hilo: ' + str(ThreadCount))