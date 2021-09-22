#coding:utf-8
import socket

host, port =('localhost', 5566)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try: #Connexion au serveur
    socket.connect((host, port))
    print("Client connecté ! ")

    data = "Bienvenue sur le server ! "
    data = data.encode("utf8")
    socket.sendall(data)

except:#Server connexion écouhé
    print("Connexion au serveur écouée !")

finally:
    socket.close()



