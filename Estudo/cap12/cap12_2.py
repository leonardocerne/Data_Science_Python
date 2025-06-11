import sqlite3
import pandas as pd

#conecta ao banco de dados
con = sqlite3.connect('Estudo/cap12/cap12_dsa.db')
cursor = con.cursor()

#seleciona todas as linhas e colunas da tabela e bota num dataframe
cursor.execute('SELECT * FROM tb_vendas_dsa')
dados = cursor.fetchall()
df = pd.DataFrame(dados, columns=['ID_Pedido',
                                  'ID_Cliente',
                                  'Nome_Produto',
                                  'Valor_Unitario',
                                  'Unidades_Vendidas',
                                  'Custo'])
#fecha o cursor e conexão porque não precisamos mais
cursor.close()
con.close()

#calcula a média de unidades vendidas
media_unidades_vendidas = df['Unidades_Vendidas'].mean()
print(media_unidades_vendidas)

#calcula a média de unidades vendidas por produto
media_unidades_vendidas_por_produto = df.groupby('Nome_Produto')['Unidades_Vendidas'].mean()
print('\n', media_unidades_vendidas_por_produto.head(10))

#calcula a média de unidades vendidas por produto se o valor unitario for maior que 199
media_unidades_valor_maior_199 = df[df['Valor_Unitario'] > 199].groupby('Nome_Produto')['Unidades_Vendidas'].mean()
print('\n', media_unidades_valor_maior_199)

#calcula a média de unidades vendidas por produto se o valor unitário for maior que 199 
#e se a média de unidades vendidas for maior do que 10
media_unidades_maior_10 = df[df['Valor_Unitario'] > 199].groupby('Nome_Produto').filter(lambda x: x['Unidades_Vendidas'].mean() > 10)
print('\n', media_unidades_maior_10)

#sintaxe sql da consulta acima:
#query5 = """SELECT Nome_Produto, AVG(Unidades_Vendidas) 
#            FROM tb_vendas_dsa 
#            WHERE Valor_Unitario > 199 
#            GROUP BY Nome_Produto 
#            HAVING AVG(Unidades_Vendidas) > 10"""
