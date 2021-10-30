import socket

host='127.0.0.1' #Endereço do servidor
port=1500 #Porta do servidor

cliSocket=socket.socket()
cliSocket.connect((host,port))

mensagem=input("Digite ENTER para iniciar!")
while mensagem!='q':
    cliSocket.send(mensagem.encode())
    dados=cliSocket.recv(1024).decode()
    print("Resposta Recebida do Servidor: \n"+dados)
    mensagem=input("Código do candidato desejado: ")
cliSocket.close()