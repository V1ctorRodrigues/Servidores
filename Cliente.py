from socket import socket, AF_INET, SOCK_STREAM

print("Criando o socket do cliente")
socket_cliente = socket(AF_INET, SOCK_STREAM)

print("Conectando ao servidor")
socket_cliente.connect(('localhost', 8080))

print("Conexão com o servidor estabelecida")
while True:
    msg = input("Digite uma mensagem")
    socket_cliente.sendall(msg.encode())
    print("Mensagem enviada")