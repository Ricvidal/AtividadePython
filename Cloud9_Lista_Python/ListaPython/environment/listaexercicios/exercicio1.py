# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,...
# e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).


mesAno= [
        '1-Janeiro',
        '2-Fevereiro',
        '3-Março',
        '4-Abril',
        '5-Maio',
        '6-Junho',
        '7-Julho',
        '8-Agosto',
        '9-Setembro',
        '10-Outubro',
        '11-Novembro',
        '12-Dezembro'
        ]
temperaturaDoMes=[]
temperaturasMediasMeses=[]
temperaturasMedias=[]
temperaturaMediaAnual = 0
temperaturas=0
#temperaturasAcimaDaMediaAnual=[]


print ('******************************************************************************************************************************')
print ('*********************************        CALCULA A TEMPERATURA MÉDIA ANUAL     ***********************************************')
print ('******************************************************************************************************************************')
print ('1-Janeiro, 2-Fevereiro, 3-Março, 4-Abril, 5-Maio, 6-Junho, 7-Julho, 8-Agosto, 9-Setembro, 10-Outubro, 11-Novembro, 12-Dezembro')
print ('******************************************************************************************************************************')

for mes in range(0, 12):
        print ('Para o mês: '+ mesAno[mes])
        temperaturasMediasMeses.append(mesAno[mes])
        temperaturasMediasMeses.append(int(input('Digite a temperatura média: ')))
        temperaturasMedias.append(temperaturasMediasMeses[:])
        temperaturasMediasMeses.clear()

for t in temperaturasMedias:
        temperaturas+=t[1]

temperaturaMediaAnual = int(temperaturas/12)

print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print ('A Temperatura média anual foi de: ', temperaturaMediaAnual,'º')
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-TEMPERATURA MÉDIA MENSAL ACIMA DA MÉDIA ANUAL=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

for tMaior in temperaturasMedias:
        if tMaior[1] > temperaturaMediaAnual:
                print (f'{tMaior[0]}: temperatura média: {tMaior[1]}º')

print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= =-=-=-=-=--==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= HISTÓRICO DA TEMPERATURA MÉDIA DOS MÊSES DO ANO =-=-=-=-=--==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

for m in temperaturasMedias:
       print (f'{m[0]} temperatura média: {m[1]}º')

print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= =-=-=-=-=--==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-JOSÉ RICARDO QUINTINO VIDAL - TSI2019.1 - IFRN - PARNAMIRIM =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= =-=-=-=-=--==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print ('FIM')



