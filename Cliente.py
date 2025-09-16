from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

def receber(sock):
    while True:
        dados = sock.recv(1024)
        if not dados:
            break
        print("\n[Servidor]:", dados.decode())

def enviar(sock):
    while True:
        msg = input()
        sock.sendall(msg.encode())

print("Conectando ao servidor...")
socket_cliente = socket(AF_INET, SOCK_STREAM)
socket_cliente.connect(("localhost", 8080))
print("Conectado ao servidor!")

Thread(target=receber, args=(socket_cliente,)).start()
Thread(target=enviar, args=(socket_cliente,)).start()