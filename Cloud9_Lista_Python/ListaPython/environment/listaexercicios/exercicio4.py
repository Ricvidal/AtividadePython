#Classe Macaco: Desenvolva uma classe Macaco, que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), 
#verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo 
#menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma 
#o outro. É possível criar um macaco canibal?

comendo = False
digerindo = False

class Macaco:
    
    def __init__(self, nome):
        self.nome=nome
        self.bucho='vazio'
    #comendo=False
    #digerindo=False
    
    
    def comer(self, alimento):
        self.bucho = alimento.nome
        return 'Comendo... ',self.bucho
        #else:
         #   return 'Macaco não comeu...'
        
    def verBucho(self):
        if self.bucho!='vazio':
            return 'Vendo o bucho: ',self.bucho
        else:
           return 'Bucho vazio'
    def digerir(self):
        if self.bucho!='vazio':
            return 'Digerindo... ',self.bucho
        else:
            return 'Não está digerindo porque não comeu ainda!'
        
class Alimento:
    def __init__(self, nome):
        self.nome=nome
    
print ('******************************************************************************************************************************')
print ('******************************************************* CLASSE MACACO ********************************************************')
print ('******************************************************************************************************************************')    

a1=Alimento('Banana')
print('Alimento: ',a1.nome)
a2=Alimento('Abacaxi')
print('Alimento: ',a2.nome)
a3=Alimento('Mamão')
print('Alimento: ',a3.nome)
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
m1=Macaco('Prego')
print('Nome do macaco: ',m1.nome)
print(m1.verBucho())
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
m2=Macaco('Babuíno')
print('Nome do macaco: ',m2.nome)
print(m2.verBucho())
print(m2.comer(a2))
print(m2.digerir())
print(m2.verBucho())
print(m2.comer(a3))
print(m2.digerir())
print(m2.verBucho())
print(m2.comer(a1))
print(m2.digerir())
print(m2.verBucho())
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Nome:',m1.nome)
print(m1.verBucho())
print(m1.comer(a1))
print(m1.digerir())
print(m1.verBucho())
print(m1.comer(a2))
print(m1.digerir())
print(m1.verBucho())
print(m1.comer(a3))
print(m1.digerir())
print(m1.verBucho())
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Nome: ',m1.nome)
print(m1.comer(m2))
print(m1.digerir())
print(m1.verBucho())
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-JOSÉ RICARDO QUINTINO VIDAL - TSI-2019.1 - IFRN - PARNAMIRIM-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print ('FIM')
