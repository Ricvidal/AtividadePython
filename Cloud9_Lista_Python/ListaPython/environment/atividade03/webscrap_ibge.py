#permite fazer uma requisição http que em seguida será utilizado para extriar o html da página
import requests

#permite extrair informações do html utilizando seletores html/css. 
from bs4 import BeautifulSoup

#Permite a limpagem dos dados para serem utilizados como npumeros ou para a finalidade desejada
import pandas as pd

#1-acessado pelo google.colab para gerar o arquivo csv e salvar na pasta do google drive
#2-foi comentado para não dar erro se executado fora do colab
#3-precisa ser montado para funcionar
#from google.colab import drive

#função para realizar o webscraping
def scrap_state_info(state: str) -> dict: 

        """
        retorna informações dos estados brasileiros
        :param state: nome do estado
        :returns state_direct: Dicionários com indicadores do estado  
        """
        print(f'Picking {state} info...')
        
        #variável state_url recebe a url que se deseja fazer a extração dos dados brutos, recebe o UF do estado na variável {state}
        state_url = f'https://www.ibge.gov.br/cidades-e-estados/{state}.html'
        
        #faz a requisição passando a variável com a URL desejada
        page=requests.get(state_url)
        
        #parseia o html da página para que possa ser usado os seletores html/css para extração
        soup = BeautifulSoup(page.content, 'html.parser')
        
        #selecionando todas as classes '.indicador' para pegar a label e os value de cada classe
        indicadors = soup.select('.indicador')
        
        #percorrendo a lista aplicando seletores e guardando em uma variável do tipo dicionário
        state_dict = {
            ind.select('.ind-label')[0].text: ind.select('.ind-value')[0].text 
            for ind in indicadors
        }
        
        #criando uma chave chamada Estado para receber o UF de cada estado
        state_dict['Estado'] = state
        
        #retona
        return state_dict

#lista com todas as UFs para ser passada para a função de extração dos dados de cada estado
states = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']
#states = ['AC']
#executando a função de extração dos dados para cada estado constante da lista 'states'
states_data = [scrap_state_info(state) for state in states]


#passando a lista pronta para o panda
df = pd.DataFrame(states_data)

#mostra os dados extraídos de forma bruta, mostra as primeiras linhas da tabela
#print(df.head())
#informação importantes dos dados extraídos
#df.info()

#fazendo uma cópia como boas práticas antes de tratar dos dados
states_df = df.copy()

#mudando o nome das colunas
states_df.columns = ['governador','capital','gentilico','area','população','densidade','matrícula-no-ensino-fundamental','idh','receita-realizada','despesas-empenhadas','rendimento-mensal-per-capita','total-de-veiculos','estado']

#organizando as colunas por dados de texto e numéricos resposctivamente
states_df = states_df[['estado','governador','capital','gentilico','area','população','densidade','matrícula-no-ensino-fundamental','idh','receita-realizada','despesas-empenhadas','rendimento-mensal-per-capita','total-de-veiculos']]

#fazendo o split dos dados retirando caracteres indesejados
states_df = states_df.replace({
    '\.':'',
    ',':'.',
    '\[\d+\]':'',
    ' hab/km²':'',
    ' km²':'',
    ' pessoas':'',
    ' matrículas':'',
    'R\$.*':'',
    ' veículos':''
}, regex=True)

#separando as colunas numéricas
colunas_numericas = ['area','população','densidade','matrícula-no-ensino-fundamental','idh','receita-realizada','despesas-empenhadas','rendimento-mensal-per-capita','total-de-veiculos']

#aplica a função split do panda que tira espaços nas bordas de uma string
states_df[colunas_numericas] = states_df[colunas_numericas].apply(lambda x: x.str.strip())

#usa a função do panda para converter em números
states_df[colunas_numericas] = states_df[colunas_numericas].apply(pd.to_numeric)
print(states_df.head())
#1 usar com o google colabe após ser montado para exportar o arquivo .csv
#2 cira o arquivo .csv com o tratamento feito e coloca dentro da pasta do google drive escolhida
#states_df.to_csv('/content/drive/MyDrive/Webscraping_Ibge/ibge_estados.csv')