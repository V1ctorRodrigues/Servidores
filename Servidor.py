from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

def conversar_cliente(sock_cliente, end_cliente):
    print(f'Conexão recebida de {end_cliente}')

    print('Recebendo dados do cliente')
    while True:
        dados = sock_cliente.recv(1024)
        print(f'Dados recebidos do cliente {end_cliente}: {dados.decode()}')

print('Criando um socket TCP')
socket_servidor = socket(AF_INET, SOCK_STREAM)

print('Identificando em qual porta o servidor vai escutar')
socket_servidor.bind(('0.0.0.0', 8080))

print('Colocando o servidor em modo de escuta')
socket_servidor.listen()

print('Servidor escutando na porta 8080')
while True:
    print('Aguardando conexão de um cliente')
    socket_cliente, endereco_cliente = socket_servidor.accept()

    thread = Thread(target=conversar_cliente, args=(socket_cliente, endereco_cliente))

    thread.start()
