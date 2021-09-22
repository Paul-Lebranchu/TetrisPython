#coding:utf-8
import socket
import threading

class ThreadForClient(threading.Thread): #Gestion de plusieurs clients
    def __init__(self, conn)
        threading.Thread.__init__(self)
        self.conn = conn

    def run(self):
        data = self.conn.recv(1024)
        data = data.decode("utf8")
        print(data)


#-----------------------------------------------------
host,port =('',5566)
#Création du socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host,port))
print("Le serveur est démarré")

while True:
    socket.listen(5)
    conn, address = socket.accept()
    print("Un client vien de se connecter")

    my_thread = ThreadForClient(conn)

    data = conn.recv(1024)
    data = data.decode("utf8")
    print(data)

conn.close()
socket.close()