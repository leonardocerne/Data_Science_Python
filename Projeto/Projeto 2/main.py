import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def autopct_format(values): 
    def my_format(pct): 
        total = sum(values) 
        val = int(round(pct * total / 100.0))
        return ' $ {v:d}'.format(v = val)
    return my_format


# Lendo arquivo.csv e botando em um DataFrame do pandas
dados = pd.DataFrame(pd.read_csv('Projeto/Projeto 2/dataset.csv'))

print('Dados que possuímos:')
print(dados.head(10), '\n')


# PERGUNTA 1

print('Pergunta 1: Qual Cidade com Maior Valor de Venda de Produtos da Categoria Office Supplies?')
# Filtramos somente as linhas que a categoria == office supplies, depois agrupamos as cidades pela soma dos valores de venda associados, e retornamos o 'ID' da maior soma
resposta1 = dados[dados['Categoria'] == 'Office Supplies'].groupby('Cidade')['Valor_Venda'].sum().idxmax()
print("Resposta: ", resposta1, '\n')


# PERGUNTA 2

print('Pergunta 2: Qual o Total de Vendas Por Data do Pedido? Demonstre o resultado através de um gráfico de barras.')
# Agrupamos as datas pelo total das vendas, e por mês pois como temos muitas datas, fica difícil a visualização do gráfico
dados['Data_Pedido'] = pd.to_datetime(dados['Data_Pedido'], format = '%d/%m/%Y')
resposta2 = dados.groupby(dados['Data_Pedido'].dt.to_period('M'))['Valor_Venda'].sum()
resposta2.index = resposta2.index.astype(str)

#formatação do gráfico
plt.figure(figsize=(13,6))
plt.bar(resposta2.index, resposta2.values, label = 'Total de Vendas por Mês')
plt.xlabel('Mês')
plt.ylabel('Total de Vendas')
plt.title('Total de Vendas por Mês')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()


# PERGUNTA 3

print('\nPergunta 3: Qual o Total de Vendas por Estado? Demonstre o resultado através de um gráfico de barras')
# Agrupamos os estados pelo total de vendas
resposta3 = dados.groupby('Estado')['Valor_Venda'].sum()

#formatação do gráfico
plt.figure(figsize=(13,6))
plt.bar(resposta3.index, resposta3.values, label = 'Total de Vendas por Estado')
plt.xlabel('Estado')
plt.ylabel('Total de Vendas')
plt.title('Total de Vendas por Estado')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()


# PERGUNTA 4

print('\nPergunta 4: Quais São as 10 Cidades com Maior Total de Vendas? Demonstre o resultado através de um gráfico de barras.')
# Agrupamos as cidades pelo total de vendas, ordenamos decrescentemente e selecionamos as primeiras 10 linhas
resposta4 = dados.groupby('Cidade')['Valor_Venda'].sum().sort_values(ascending=False).head(10)

#formatação do gráfico
plt.figure(figsize=(7,6))
plt.bar(resposta4.index, resposta4.values, label = '10 Cidades Com Maior Total de Vendas')
plt.xlabel('Cidade')
plt.ylabel('Total de Vendas')
plt.title('10 Cidades Com Maior Total de Vendas')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()


# PERGUNTA 5

print('\nPergunta 5: Qual segmento teve o Maior Total de Vendas? Demonstre o resultado através de um gráfico de pizza.')
# Agrupamos os segmentos pelo total de vendas e plotamos num gráfico de pizza
resposta5 = dados.groupby('Segmento')['Valor_Venda'].sum()

#formatação do gráfico
plt.figure(figsize=(8,8))
plt.pie(resposta5.values, labels=resposta5.index, autopct = autopct_format(resposta5.values))
plt.title('Total de Vendas Por Segmento')
plt.show()


# PERGUNTA 6

print('\nPergunta 6: Qual o total de vendas por segmento e por ano?')
# Criamos coluna Ano para facilitar
dados['Ano'] = dados['Data_Pedido'].dt.year
# Agrupamos em relação ao segmento e ao ano, pelo total de vendas
resposta6 = dados.groupby(['Segmento', 'Ano'])['Valor_Venda'].sum()
print('\n', resposta6)


# PERGUNTA 7

print('\nPergunta 7:Os gestores da empresa estão considerando conceder diferentes faixas de descontos e gostariam de fazer uma simulação com base na regra abaixo:- ' \
'Se o Valor_Venda for maior que 1000 recebe 15% de desconto.'
'- Se o Valor_Venda for menor que 1000 recebe 10% de desconto.')
# Cria coluna desconto usando condição da questão
dados['Desconto'] = np.where(dados['Valor_Venda'] >1000, 0.15, 0.10)
print('\n', dados.head(10))
print('\nQuantas vendas receberiam 15% de desconto')
resposta7 = dados['Desconto'].value_counts()
print('\n', resposta7)


# PERGUNTA 8
print('\nPergunta 8:Considere Que a Empresa Decida Conceder o Desconto de 15% do Item Anterior. Qual Seria a Média do Valor de Venda Antes e Depois do Desconto?')
print('Valores Antigos:\n', dados[dados['Desconto'] == 0.15].head(10))
print('\nMédia Antes:', dados['Valor_Venda'].mean())
dados['Valor_Venda'] = np.where(dados['Desconto'] == 0.15, dados['Valor_Venda'] * 0.85, dados['Valor_Venda'])
print('Novos Valores:\n', dados[dados['Desconto'] == 0.15].head(10))
print('\nMédia Nova:', dados['Valor_Venda'].mean())


# PERGUNTA 9
print('\nPergunta 9:Qual o Média de Vendas Por Segmento, Por Ano e Por Mês? Demonstre o resultado em um gráfico de linhas')
dados['Mes'] = dados['Data_Pedido'].dt.month
media_segmento = dados.groupby(['Segmento', 'Ano', 'Mes'])['Valor_Venda'].mean()
# Garante que media_segmento seja um DataFrame (não uma Series com índice MultiIndex)
media_segmento = media_segmento.reset_index()

# Cria o gráfico de linhas
plt.figure(figsize=(12, 6))
sns.lineplot(data=media_segmento, x='Mes', y='Valor_Venda', hue='Segmento', style='Ano', markers=True, dashes=False)

# Títulos e rótulos
plt.title('Média de Vendas por Segmento - Por Ano e Mês')
plt.xlabel('Mês')
plt.ylabel('Média de Valor de Venda')
plt.xticks(range(1, 13))  # Garante que todos os meses apareçam no eixo x
plt.legend(title='Segmento / Ano', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


# PERGUNTA 10
print('\nPergunta 10:Qual o Total de Vendas Por Categoria e SubCategoria, Considerando Somente as Top 12 SubCategorias? Demonstre tudo em um único gráfico')
total_cat_sub = dados.groupby(['Categoria', 'SubCategoria'])['Valor_Venda'].sum()
print('\n', total_cat_sub)

# Garante que seja um DataFrame e não uma Series com índice MultiIndex
total_cat_sub = total_cat_sub.reset_index()

# Ordena por categoria e valor de venda (opcional, para melhor visual)
top12 = total_cat_sub.sort_values(by=['Valor_Venda'], ascending=False).head(12)

# Cria o gráfico
plt.figure(figsize=(14, 6))
sns.barplot(data=total_cat_sub, x='SubCategoria', y='Valor_Venda', hue='Categoria')

# Títulos e ajustes
plt.title('Total de Vendas por Categoria e SubCategoria')
plt.xlabel('SubCategoria')
plt.ylabel('Valor Total de Vendas')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Categoria', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

plt.show()