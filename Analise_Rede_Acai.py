
import pandas as pd
import plotly.express as px
#from fpdf import FPDF

print("Carregando Planilha...")

dados = pd.read_excel ("./AnaliseDados/vendas.xlsx")
print("Planilha Carregada")


print("Gerando dados...")
print(dados.head()) #Primeiras linhas
dados.tail() #Ultimas linhas
dados.shape #Quantidade de linhas e colunas
dados.info() #Gera informações
dados.describe() #Gera estatisticas
dados['loja'] #Chama coluna Loja
dados.loja #Caso não tenha espaços no nome da coluna
dados['loja'].unique() #Retorna valores unicos
dados['loja'].value_counts() #retorna total de veze que aparece cada loja
dados['loja'].value_counts(normalize=True) #Retorna valore relativo

#Criando PDF
#pdf = FPDF()
#pdf.add_page()
#pdf.set_font("arial")

#Agrupando Dados
print("Agrupando Dados...")
dados.groupby('loja').preco.sum()
dados.groupby('loja').preco.mean()

#Gerando graficos
print("Gerando Gráficos...")
px.histogram(dados, x="loja", color="regiao", text_auto=True) #Grafico simples

#Multiplos gráficos
colunas=['loja', 'cidade', 'estado', 'tamanho', 'local_consumo']

for coluna in colunas:
    fig = px.histogram(dados, x=coluna, y='preco', color='forma_pagamento', text_auto=True)
    fig.show() 

#pdf.output("Teste.pdf")

print("Tudo pronto!")
