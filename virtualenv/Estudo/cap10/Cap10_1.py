import pandas as pd
from pandas import DataFrame
import numpy as np
dados = {'Estado': ['Santa Catarina', 'Rio de Janeiro', 'Tocantins', 'Bahia', 'Minas Gerais'], 
         'Ano': [2004, 2005, 2006, 2007, 2008], 
         'Taxa Desemprego': [1.5, 1.7, 1.6, 2.4, 2.7]}
print(dados)

df = DataFrame(dados)
print(df.head())

df2 = DataFrame(dados, columns = ['Estado', 'Taxa Desemprego', 'Ano'])
print('\n', df2.head())

df3 = DataFrame(dados, columns= ['Estado', 'Taxa Desemprego', 'Taxa Crescimento', 'Ano'],
                 index = ['estado1', 'estado2', 'estado3', 'estado4', 'estado5'])
print('\n', df3)

#imprime somente os dados da coluna estado
print('\n', df3['Estado'])

#imprime somente os dados da linha com index estado3
print('\n', df3.filter(items= ['estado3'], axis = 0))

#analise estatistica dos dados
print('\n', df3.describe())

#retorna true se tem valor, false se não possui valor
print('\n', df2.isna())

#completa valores com numpy, aqui no caso vai completar com valores de 0 a 5 (nao incluindo 5)
df3['Taxa Crescimento'] = np.arange(5.)
print('\n', df3)

#slicing do df
print('\n', df3['estado2':'estado4'])

#slicing com condição
print('\n', df3[df3['Taxa Desemprego'] < 2])


dsa_df = pd.read_csv('Estudo/teste.csv')
print('\n', dsa_df.head(15))

#imprime valores estatisticos de uma coluna em especifico
print('\n', dsa_df.Valor_Venda.describe())

#cria novo dataframe com as linhas que obedecem a condição estabelecida
df4 = dsa_df.query('229 < Valor_Venda < 10000')

print('\n', df4.Valor_Venda.describe())

df5 = df4.query('Valor_Venda > 766')
print('\n', df5.head())

#filtro que retorna linhas em que a quantidade é um dos valores do vetor, e só imprime 10 valores
print('\n', dsa_df[dsa_df['Quantidade'].isin([5,7,9,11])][:10])

#continua no Cap10_2 porque a saída já está muito grande