#Problema 02 - Sistema de Votação Online
#Versão Original elaborada pelo professor Givanaldo Rocha
#Deseja-se implementar um sistema eletrônico de votação a partir de uma aplicação
#servidora e de aplicações clientes que se conectam através de sockets de rede, com as
#seguintes características:
#● A aplicação servidora, ao ser iniciada, solicita que o usuário entre com o número de
#candidatos e os respectivos códigos dos candidatos via console.
#● A aplicação servidora passa a aceitar conexões TCP na porta 1500
#● Quando uma aplicação cliente é iniciada, esta abre uma conexão com o servidor, via
#porta TCP 1500, recebe do servidor uma lista com os códigos dos candidatos.
#● A aplicação cliente passa a receber do usuário, via console de texto, o código do
#candidato a ser votado. Quando isto acontece, a aplicação cliente envia para o
#servidor, uma mensagem contendo um número inteiro representando o código do
#candidato que foi votado.
#● A aplicação servidora recebe a mensagem contendo o número do candidato e
#atualiza o resultado da votação e mostra no console .

import socket, threading


class ClienteThread(threading.Thread):
    def __init__(self,enderecoCliente, socketClient):
        threading.Thread.__init__(self)
        self.csocket=socketClient
        self.enderecoCliente=enderecoCliente
        print("Conexão recebida de ", enderecoCliente)
    
        escolha='Digite o código do candidato desejado!\n'
        self.csocket.send(escolha.encode())
    
        for c in codigoCandidato:
            mensagemRetorno=(f'{c[0]}º Candidato, Código: {c[1]}\n')
            self.csocket.send(mensagemRetorno.encode())    
    
    def run(self):
        mensagem=''
        contMensagem=0
        votoValido=False
        while True:
            dados=self.csocket.recv(1024)
            mensagem=dados.decode()
            
            if (not mensagem):
                break
            
            for v in codigoCandidato:
                if int(mensagem) == v[1]:
                    v[2]+=1
                    votoValido=True    
            if votoValido:
                print("O computador ", self.enderecoCliente, " votou no candidato de código: ",mensagem)    

            else:   print("O computador ", self.enderecoCliente, " digitou o seguinte voto inválido ",mensagem)
                
            for c in codigoCandidato:
                print (f'{c[0]}º Candidato, Código: {c[1]}, Voto {c[2]}')

        print("Cliente ", self.enderecoCliente, " Desconectado")
        print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print ('=-=-=-=-=-=-=-=-=-=-=-=-=-JOSÉ RICARDO QUINTINO VIDAL - TSI2019.1 - IFRN - PARNAMIRIM =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

        
candidatos=[]#lista auxiliar, que será usada para gerar a final
codigoCandidato=[]#lista de candidatos fiinal que será montada pelo usuário ao receber os códigos
numeroCandidatos=int(input("Entre com o número de candidatos a ser cadastrados: "))

#Cria a lista de candidato
for i in range(0,numeroCandidatos):
    print("Digite o código do ",(i+1),"º candidato:")
    candidatos.append(int((i+1))) #insere as pósições automaticamente
    candidatos.append(int(input('Código: '))) #recebe o código digitado pelo usuário 
    candidatos.append(int(0)) #preenche com voto zero assim que criado
    codigoCandidato.append(candidatos[:]) #faz uma cópia
    candidatos.clear() #limpa a lista para a próxima rodada caso necessário
    
print(codigoCandidato) #impressão bruta
for c in codigoCandidato:#impressão formatada da lista de candidato pronta
        print (f'{c[0]}º Candidato, Código: {c[1]}, Voto {c[2]}')

    
HOST='127.0.0.1' #Indica quem é o local host
PORT=1500
servidor=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
servidor.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
servidor.bind((HOST,PORT)) #liga o socket na porta e host especificado na tupla

print("Aguardando Conexões...")

while True:
    servidor.listen(1)
    clienteSocket,enderecoCliente=servidor.accept()
    thread_cliente=ClienteThread(enderecoCliente,clienteSocket)
    thread_cliente.start()