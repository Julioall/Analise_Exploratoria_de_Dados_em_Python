import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

# CARREGANDO OS DADOS
data_frame = pd.read_csv('dados/dataset.csv')
'''
#VERIFICANDO INTEGRIDADE DOS DADOS
#SHAPE
print(data_frame.shape)
#AMOSTRA DOS DADOS PRIMEIRAS LINHAS
print(data_frame.head())
#AMOSTRA DOS DADOS UTIMAS LINHAS
print(data_frame.tail())

#ANÁLISE EXPLORATÓRIA
print(data_frame.columns)
#VERIFICAR O TIPO DE DADO DE CADA COLUNA
print(data_frame.dtypes)
#RESUMO ESTATÍSTICO DA COLUNA COM O VALOR DE VENDA
print(data_frame['Valor_Venda'].describe())
#VERIFICANDO SE HÁ REGISTROS DUPLICADOS
data_frame[data_frame.duplicated()]

#VERIFICAR SE HÁ VALORES AUSENTES
print(data_frame.isnull().sum())
'''

# PERGUNTA DE NEGOCIO 1

'''
# Qual a cidade com maior valor de vendas de produtos da categoria 'Office Supplies'?
data_frame_p1 = data_frame[(data_frame.Categoria == 'Office Supplies')]
data_frame_p1_total = data_frame_p1.groupby('Cidade')['Valor_Venda'].sum()
cidade_maior_venda = data_frame_p1_total.idxmax()
print(
    f"A cidade com o maior valor de vendas de produtos da categoria 'Office Supplies' é: {cidade_maior_venda}")
'''

# PERGUNTA DE NEGOCIO 2
'''
# Qual o total de vendas por data do pedido
data_frame_p2 = data_frame.groupby('Data_Pedido')[
    'Valor_Venda'].sum()

# Mostrando dados tratados
print(data_frame_p2.head())

# Supondo que 'data_frame' seja o DataFrame que contém os dados

# Qual o total de vendas por data do pedido
data_frame_p2 = data_frame.groupby('Data_Pedido')[
    'Valor_Venda'].sum()

# Mostrando dados tratados
print(data_frame_p2.head())

# Ordenando as datas em ordem crescente
data_frame_p2 = data_frame_p2.sort_index()

# Criando o gráfico
plt.figure(figsize=(20, 6))
# Não é necessário especificar x e y
data_frame_p2.plot(color='green')
plt.title('TOTAL DE VENDAS POR DATA DO PEDIDO')
plt.xlabel('Data do Pedido')
plt.ylabel('Total de Vendas')
plt.tight_layout()
plt.show()
'''

# PERGUNTA DE NEGOCIO 3
'''
#Qual o total de vendas por estado?
data_frame_p3 = data_frame.groupby('Estado')['Valor_Venda'].sum().reset_index()

# Criando o gráfico de barras usando Seaborn
plt.figure(figsize=(16, 6))
sns.barplot(data=data_frame_p3, y='Valor_Venda', x='Estado')
plt.title('Vendas por Estado')
plt.xlabel('Estado')
plt.ylabel('Total de Vendas')
plt.xticks(rotation=80)
plt.tight_layout()
plt.show()
'''

# PERGUNTA DE NEGOCIO 4

# Quais são as 10 cidades com maior total de vendas?
'''
data_frame_p4 = data_frame.groupby('Cidade')['Valor_Venda'].sum().reset_index().sort_values(by='Valor_Venda',ascending=False).head(10)
print(data_frame_p4.head(10))
#Grafico
plt.figure(figsize=(16,6))
sns.set_palette("coolwarm")
sns.barplot(data= data_frame_p4,
            y='Valor_Venda',
            x='Cidade').set(title="As 10 cidades com maior total de vendas")
plt.show()
'''
# PERGUNTA DE NEGOCIO 5
# Qual segmento teve maior tota lde vendas?

'''data_frame_p5 = data_frame.groupby('Segmento')['Valor_Venda'].sum().reset_index().sort_values(by='Valor_Venda',
                                                                                              ascending=False)
def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return ' $ {v:d}'.format(v=val)
    return my_format
#Grafico
plt.figure(figsize=(16,6))
plt.pie(data_frame_p5['Valor_Venda'],
        labels=data_frame_p5['Segmento'],
        autopct= autopct_format(data_frame_p5['Valor_Venda']),
        startangle= 90)  

centre_circulo = plt.Circle((0,0),0.82, fc = 'white')
fig = plt.gcf()
fig.gca().add_artist(centre_circulo)

plt.annotate(text='Total de Vendas: '+'$ '+ str(int(sum(data_frame_p5['Valor_Venda']))), xy=(-0.25,0))
plt.title('Total de vendas por segmento')
plt.show()
'''

# PERGUNTA DE NEGOCIO 6
# Qual o total de vendas por segmento e por ano?
'''
print(data_frame.dtypes.head())
# Convertendo a Coluna Data Pedido para formato datetime64
data_frame['Data_Pedido'] = pd.to_datetime(
    data_frame['Data_Pedido'], dayfirst=True)
print(data_frame.dtypes.head())
data_frame['Ano'] = data_frame['Data_Pedido'].dt.year  # Criando uma coluna ano
print(data_frame.head())
data_frame_p6 = data_frame.groupby(['Ano', 'Segmento'])['Valor_Venda'].sum()
print(data_frame_p6)
'''
# PERGUNTA DE NEGOCIO 7
'''Os gestores da empresa estão considerando conceder diferentes faixas de descontos e gostariam de fazer uma
simulação na regra abaixo:
Se o Valor_Venda for maior que 1000 recebe 15% de desconto.
Se o Valor_Venda for menor que 1000 recebe 10% de deconto.
Quantas vendas recebiriam 15% de desconto?
'''
"""
data_frame['Desconto'] = np.where(data_frame['Valor_Venda']> 1000, 0.15, 0.10)#Se valor venda for maior que 1000 coluna desconto recebe 0.15 se não recebe 0.10
print(data_frame['Desconto'].value_counts())
print("Total de vendas que receberam 15% de desconto: 457")


data_frame_p5 = data_frame['Desconto']desc_15 = 0
for i in data_frame_p5: 
    if i == 0.15: 
        desc_15+=1
print(f"Total de vendas que receberam 15% de desconto: {desc_15}") 
"""

# PERGUNTA DE NEGOCIO 8

'''#Considere que a empresa decida conceder o desconto de 15% do item anterior. Qual seria a media do valor de venda antes e depois do desconto?

#Criando coluna de desconto
data_frame['Desconto'] = np.where(data_frame['Valor_Venda']> 1000, 0.15, 0.10)#Se valor venda for maior que 1000 coluna desconto recebe 0.15 se não recebe 0.10
#Criando coluna Valor_Venda_Desconto desconto
data_frame['Valor_Venda_Desconto'] = data_frame['Valor_Venda']  - data_frame['Valor_Venda'] * data_frame['Desconto']


#Filtrando valores
media_antes_desconto = data_frame.loc[data_frame['Desconto'] == 0.15, 'Valor_Venda']
#Calculando Média
media_antes_desconto = media_antes_desconto.mean()
#Filtrando valores
media_depois_desconto = data_frame.loc[data_frame['Desconto'] == 0.15, 'Valor_Venda_Desconto']
#Calculando média
media_depois_desconto = media_depois_desconto.mean()

print(f'Média de vendas antes do desconto: R${media_antes_desconto:.2f}\nMédia de vendas depois do desconto de 15%: R${media_depois_desconto:.2f}')
'''
# PERGUNTA DE NEGOCIO 9

#Qual a média de vendas por segmento, por ano e por mês?

data_frame['Data_Pedido'] = pd.to_datetime(data_frame['Data_Pedido'], dayfirst=True)

print(data_frame.dtypes.head())

data_frame["Mes"] = data_frame['Data_Pedido'].dt.month
data_frame["Ano"] = data_frame['Data_Pedido'].dt.year
print(data_frame.head())

data_frame_p9 = data_frame.groupby(['Ano','Mes','Segmento'])['Valor_Venda'].agg([np.sum, np.mean, np.median])#A função agg te da a possibilidade de usar varias funções estraindo a soma, média e mediana.and
print(data_frame_p9.head())

anos = data_frame_p9.index.get_level_values(0)
meses = data_frame_p9.index.get_level_values(1)
segmentos = data_frame_p9.index.get_level_values(2)
# Resetar o índice para facilitar a manipulação dos dados
data_frame_p9 = data_frame_p9.reset_index()
#Grafico
'''
plt.figure(figsize=(12,6))
sns.set()#Limpar formatação
fig1 = sns.relplot(kind = 'line',
                   data= data_frame_p9,
                   y='mean',
                   x=meses,
                   hue=segmentos,
                   col=anos,
                   col_wrap=4)
plt.tight_layout()
plt.show()
'''
'''# Gráfico de linhas
plt.figure(figsize=(12,6))
sns.set()

# Usar lineplot para um gráfico de linha simples
sns.lineplot(data=data_frame_p9, x='Mes', y='mean', hue='Segmento', style='Ano', markers=True)

plt.tight_layout()
plt.show()'''
'''# Definir uma paleta de cores para cada ano
palette = sns.color_palette("husl", n_colors=data_frame_p9['Ano'].nunique())

# Criar gráficos horizontais separados para cada ano
g = sns.catplot(
    data=data_frame_p9,
    x='mean',
    y='Segmento',
    hue='Segmento',
    kind='bar',
    height=5,
    aspect=2,
    dodge=False,  # Isso evita que as barras do mesmo segmento sejam separadas
    palette=palette
)

g.set_axis_labels("Média de Vendas", "Segmento")
g.set_titles("Ano {col_name}")
g.tight_layout()

plt.show()'''
# PERGUNTA DE NEGOCIO 10
