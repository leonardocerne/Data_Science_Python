import sqlite3 as sql
import pandas as pd

conn = sql.connect('Praticando/QSWorldUniversityRankings/banco.db')

for row in conn.execute('SELECT RANK_2025, RANK_2024, Institution_Name FROM QSWorldUniversityRankings WHERE id BETWEEN 1 AND 30'):
    print(row)

conn.close()