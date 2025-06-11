import pandas as pd
from pandas import DataFrame
import numpy as np


dsa_df = pd.read_csv('Estudo/teste.csv')

#retorna dataframe com duas condições e as duas tem que ser verdadeiras
print(dsa_df[(dsa_df.Segmento == 'Home Office') & (dsa_df.Regiao == 'South')].head())

#retorna dataframe com duas condições e uma das duas tem que ser verdadeira
print('\n', dsa_df[(dsa_df.Segmento == 'Home Office') | (dsa_df.Regiao == 'South')].tail())

#verifica quantidade de valores NA em cada coluna
print('\n', dsa_df.isna().sum())
#acha moda da quantidade, preenche todos valores NA com a moda
moda = dsa_df['Quantidade'].value_counts().index[0]
dsa_df['Quantidade'].fillna(value=moda, inplace=True)
print('\n', dsa_df.isna().sum())

#group by agrupa as linhas com base nas combinações dadas e calcula a média de cada grupo
print('\n', dsa_df[['Segmento', 'Regiao', 'Valor_Venda']].groupby(['Segmento', 'Regiao']).mean())

#agg retorna agregação multipla, calcula certos valores para cada grupo
print('\n', dsa_df[['Segmento', 'Regiao', 'Valor_Venda']].groupby(['Segmento', 'Regiao']).agg(['mean', 'std', 'count']))

#filtra o dataframe pela coluna segmento com valores que iniciam com 'Con'
print('\n', dsa_df[dsa_df.Segmento.str.startswith('Con')].head())

#igual o de cima mas filtra por valores que terminam com 'mer'
print('\n', dsa_df[dsa_df.Segmento.str.endswith('mer')].head())

#pega o ano do ID_Pedido
print('\n', dsa_df['ID_Pedido'].head())
print('\n', dsa_df['ID_Pedido'].str.split('-').str[1])

#criamos uma nova coluna com a extração do ano do ID_Pedido
dsa_df['Ano'] = dsa_df['ID_Pedido'].str.split('-').str[1]
print('\n', dsa_df.head())

print('\n', dsa_df['Data_Pedido'].head(3))
#Vamos remover os dígitos 2 e 0 à esquerda do valor da variável 'Data_Pedido'
print('\n', dsa_df['Data_Pedido'].str.lstrip('20').head())
#como nao usamos inplace = true, não alteramos a memória de fato, só imprimimos formatado

#Replace de caracteres em strings
dsa_df['ID_Cliente'] = dsa_df['ID_Cliente'].str.replace('CG', 'AX')

print(dsa_df.head())

#concatenando strings
dsa_df['Pedido_Segmento'] = dsa_df['ID_Pedido'].str.cat(dsa_df['Segmento'], sep='-')
print('\n', dsa_df.head())

#continuamos no Cap10_3