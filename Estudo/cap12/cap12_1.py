import sqlite3
import pandas as pd

con = sqlite3.connect('Estudo/cap12/cap12_dsa.db')
cursor = con.cursor()

sql_query = """SELECT name FROM sqlite_master WHERE type = 'table';"""
cursor.execute(sql_query)
print(cursor.fetchall())

query1 = 'SELECT * FROM tb_vendas_dsa'
cursor.execute(query1)
nomes_colunas = [description[0] for description in cursor.description]
print(nomes_colunas)
print(cursor.fetchall())

query2 = 'SELECT AVG(Unidades_Vendidas) FROM tb_vendas_dsa'
cursor.execute(query2)
print(cursor.fetchall())