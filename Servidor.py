from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

def receber(sock):
    while True:
        dados = sock.recv(1024)
        if not dados:
            break
        print("\n[Cliente]:", dados.decode())

def enviar(sock):
    while True:
        msg = input()
        sock.sendall(msg.encode())

print("Servidor iniciando...")
socket_servidor = socket(AF_INET, SOCK_STREAM)
socket_servidor.bind(("0.0.0.0", 8080))
socket_servidor.listen(1)

print("Aguardando conexão...")
sock_cliente, end_cliente = socket_servidor.accept()
print("Cliente conectado:", end_cliente)

Thread(target=receber, args=(sock_cliente,)).start()
Thread(target=enviar, args=(sock_cliente,)).start()