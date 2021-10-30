#Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste 
#conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

    #Valida e corrige número de telefone
    #Telefone: 461-0133
    #Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
    #Telefone corrigido sem formatação: 34610133
    #Telefone corrigido com formatação: 3461-0133


print ('******************************************************************************************************************************')
print ('******************************* VALIDA E CORRIGE NÚMERO DE TELEFONE *************************************************')
print ('******************************************************************************************************************************')
print ('')
numeroCorrigido=''
numeroFormatado=[]

numeroTelefone=input('Digite o número do telefone a ser validado: ')
print ('Telefone: ',numeroTelefone)
posicaoIfem=numeroTelefone.find('-')
#print(numeroPuro)
if posicaoIfem!=-1:
    print('Número com ífem.')
    if len(numeroTelefone)<9:
        print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
        numeroCorrigido='3'+numeroTelefone
        numeroSemIfem=numeroCorrigido[:4]+numeroCorrigido[5:9]
        print('Telefone corrigido sem formatação: ',numeroSemIfem )
        print('Telefone corrigido com formatação: ', numeroCorrigido)
    
else:
    print('Numero sem ífem.')
    if len(numeroTelefone)<8:
        print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
        numeroCorrigido='3'+numeroTelefone
        print('Telefone corrigido sem formatação: ', numeroCorrigido)
        numeroFormatado='3'+numeroTelefone[:3]+'-'+numeroTelefone[3:7]
        print('Telefone corrigido com formatação: ', numeroFormatado)    

print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-JOSÉ RICARDO QUINTINO VIDAL - TSI-2019.1 - IFRN - PARNAMIRIM-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print ('FIM')

    