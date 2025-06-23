import pandas as pd
import numpy as np
import sqlite3 as sql

# Criando um banco de dados SQL e inserindo valores do csv nele

# Conecta com o banco de dados (cria o arquivo se não existir)
conn = sql.connect('Praticando/QSWorldUniversityRankings/banco.db')
cursor = conn.cursor()

# Cria Tabela (Precisa ter mesmos índices que o CSV)
conn.execute('''
CREATE TABLE IF NOT EXISTS QSWorldUniversityRankings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    RANK_2025 INTEGER,
    RANK_2024 INTEGER,
    Institution_Name TEXT,
    Location TEXT,
    Region TEXT,
    SIZE TEXT,
    FOCUS TEXT,
    RES TEXT,
    STATUS TEXT,
    Academic_Reputation_Score REAL,
    Academic_Reputation_Rank TEXT,
    Employer_Reputation_Score REAL,
    Employer_Reputation_Rank TEXT,
    Faculty_Student_Score REAL,
    Faculty_Student_Rank INTEGER,
    Citations_per_Faculty_Score REAL,
    Citations_per_Faculty_Rank INTEGER,
    International_Faculty_Score REAL,
    International_Faculty_Rank INTEGER,
    International_Students_Score REAL,
    International_Students_Rank INTEGER,
    International_Research_Network_Score REAL,
    International_Research_Network_Rank INTEGER,
    Employment_Outcomes_Score REAL,
    Employment_Outcomes_Rank TEXT,
    Sustainability_Score REAL,
    Sustainability_Rank TEXT,
    Overall_Score REAL)
              ''')

dados = pd.read_csv('Praticando/QSWorldUniversityRankings/dados.csv')

# Insere linhas do DataFrame do Pandas no banco de dados
dados.to_sql('QSWorldUniversityRankings', conn, if_exists='append', index = False)

# Loop simples para verificar se os valores foram inseridos corretamente
for row in conn.execute('SELECT * FROM QSWorldUniversityRankings'):
    print(row)

# Criando um script SQL para poder migrar esse banco de dados para outro SGBD (MySQL por exemplo)
with open('Praticando/QSWorldUniversityRankings/dump.sql', 'w', encoding='utf-8') as f:
    for linha in conn.iterdump():
        f.write(f'{linha}\n')

# Fechando conexão
conn.close()