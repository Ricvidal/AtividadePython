#Problema 01 - Corrida de Fórmula 01
#Versão Original elaborada pelo professor Givanaldo Rocha
#Desenvolver uma aplicação para simular a dinâmica de uma corrida de Fórmula 1. Serão
#duas threads em que uma representa o carro de Felipe Massa e a outra representa o carro
#de Lewis Hamilton. As threads possuem as seguintes características:
#● Cada thread possui um loop com 65 interações (as voltas da pista).
#● A cada volta, a thread dorme durante um tempo aleatório entre 0 e 1 segundo,
#representando o tempo gasto para percorrer a volta.
#O programa deve aguardar as duas threads terminarem, representando a linha de chegada,
#e então informar quem venceu a corrida (dica: pesquisar o método join()).

import threading
import time

vencedor=['1º Lugar: ','','2º Lugar: ','']


def massa(deley):
    for i in range(66):
        if i==65:
            if vencedor[1]=='':
                vencedor[1]="Felipe Massa"
            elif vencedor[1]!='':
                 vencedor[3]="Felipe Massa"
        else:
            print("Felipe Massa está na volta: ",i)
            time.sleep(deley)

def hamilton(deley):
    for i in range(66):
        if i==65:
            if vencedor[1]=='':
                vencedor[1]="Lewis Hamilton"
            elif vencedor[1]!='':
                 vencedor[3]="Lewis Hamilton"
        else:
            print("Lewis Hamilton está na volta: ",i)
            time.sleep(deley)

print ('******************************************************************************************************************************')
print ('**************************** CORRIDA DE FÓRMULA 01- Felipe Massa e Lewis Hamilton*********************************************')
print ('******************************************************************************************************************************')
print("Iniciou a corrida!!!")
#for i in range(10):
t1=threading.Thread(target=massa,args=(1,))
t2=threading.Thread(target=hamilton,args=(1,))
t1.start()
t2.start()
t1.join()
t2.join()
print(f'{vencedor[0]}{vencedor[1]}')
print(f'{vencedor[2]}{vencedor[3]}')
print("Fim da corrida.")
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-JOSÉ RICARDO QUINTINO VIDAL - TSI-2019.1 - IFRN - PARNAMIRIM-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')