#Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um 
#levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se 
#encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
#Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número
#indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
#necessita da esfera;
#necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
#Quantidade de mouses: 100

#Situação                        Quantidade              Percentual
#1- necessita da esfera                  40                     40%
#2- necessita de limpeza                 30                     30%
#3- necessita troca do cabo ou conector  15                     15%
#4- quebrado ou inutilizado              15                     15%

mouseID=[
         'ID',0,
         '1- necessita de esfera',0,
         '2- necessita de limpeza',0,
         '3- necessita troca do cabo ou conector',0,
         '4- quebrado ou inutilizado',0
        ]


resposta=''
quantidade=0
finalizar=1


print ('******************************************************************************************************************************')
print ('******************************* RELATÓRIO DAS CONDIÇÕES DOS MOUSES DA SUCATA *************************************************')
print ('******************************************************************************************************************************')
print ('*************************** PARA CADASTRAR O MAUSE PREENCHA OS DADOS SOLICITADOS *********************************************')

print ('')
while finalizar!=0:
         
        #for mouse in range(0, 200):
        condicao=False
        mouseID[1]=input('Preencha o número de identificação do mouse: ')
        print ('')
        while condicao==False:  
                resposta=input('1- necessita de esfera? (S/N) ')
                print ('') 
                if resposta=='S':
                        mouseID[3]+=1
                        condicao=True
                elif resposta == 's':
                        mouseID[3]+=1
                        condicao=True
                elif resposta == 'n':
                        condicao=True
                elif resposta =='N':
                        condicao=True
                else:
                        print ('Caractere inválido! Tente novamente')
        condicao=False
        while condicao==False:
                resposta=input('2- necessita de limpeza? (S/N) ')
                print ('')
                if resposta=='S':
                        mouseID[5]+=1
                        condicao=True
                elif resposta == 's':
                        mouseID[5]+=1
                        condicao=True
                elif resposta == 'n':
                        condicao=True
                elif resposta =='N':
                        condicao=True
                else:
                        print ('Caractere inválido! Tente novamente')
        condicao=False
        while condicao==False:
                resposta=input('3- necessita troca do cabo ou conector? (S/N) ')
                print ('') 
                if resposta=='S':
                        mouseID[7]+=1
                        condicao=True
                elif resposta == 's':
                        mouseID[7]+=1
                        condicao=True
                elif resposta == 'n':
                        condicao=True
                elif resposta =='N':
                        condicao=True
                else:
                        print ('Caractere inválido! Tente novamente')
        condicao=False
        while condicao==False:
                resposta=input('4- quebrado ou inutilizado? (S/N) ')
                print ('') 
                if resposta=='S':
                        mouseID[9]+=1
                        condicao=True
                elif resposta == 's':
                        mouseID[9]+=1
                        condicao=True
                elif resposta == 'n':
                        condicao=True
                elif resposta =='N':
                        condicao=True
                else:
                        print ('Caractere inválido! Tente novamente')

        quantidade+=1

        print ('')
        finalizar=input('Digite o número ZERO "0" para encerrar! ')
        print ('') 
        if finalizar=='0':
                finalizar=0
        elif finalizar==0:
                finalizar=0
        else:
                finalizar=1

percentualEsfera=int((mouseID[3]/quantidade)*100)
percentualLimpeza=int((mouseID[5]/quantidade)*100)
percentualTroca=int((mouseID[7]/quantidade)*100)
percentualQuebrado=int((mouseID[9]/quantidade)*100)


print ('******************************************************************************************************************************')
print ('******************************* RELATÓRIO DAS CONDIÇÕES DOS MOUSES DA SUCATA *************************************************')
print ('******************************************************************************************************************************')
print ('Quantidade de mouse analisado: ',quantidade)
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print (f'Situação                               Quantidade                         Percentual')
print (f'{mouseID[2]:<40} {mouseID[3]:>8} {percentualEsfera:>33}%')
print (f'{mouseID[4]:<40} {mouseID[5]:>8} {percentualLimpeza:>33}%')
print (f'{mouseID[6]:<40} {mouseID[7]:>8} {percentualTroca:>33}%')
print (f'{mouseID[8]:<40} {mouseID[9]:>8} {percentualQuebrado:>33}%')
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-JOSÉ RICARDO QUINTINO VIDAL - TSI-2019.1 - IFRN - PARNAMIRIM-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print ('FIM')

