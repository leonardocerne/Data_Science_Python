# Praticando a análise de dados a partir do dataset QS World University Rankings 2025 provido do Kaggle

# Importando bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Lendo os dados e botando em um Data Frame do Pandas
dados = pd.read_csv('Praticando/QSWorldUniversityRankings/dados.csv', encoding='latin1')

print('(linhas, colunas)\n', dados.shape)

# Imprimindo primeiras linhas do DF para visualizarmos os dados que possuímos inicialmente
print("Dados:\n", dados.head())

# Imprimindo colunas, quantos itens não nulos e o tipo delas
print('\nInformações básicas do DF\n')
print('\n', dados.info())

# Imprimindo resumo estatístico
print('\nResumo Estatístico:\n', dados.describe())

# Imprimindo quantidade de valores faltantes em cada coluna
print('\nValores Faltantes:\n')
print(dados.isnull().sum())

# Exemplo 1: imprimindo ranking de 2025 e 2025 de todas as universidades dos estados unidos, e mostrando quantas posições cada instituição ganhou/perdeu
exemplo1 = dados[dados['Location'] == 'United States'].copy()
exemplo1['RANK_2024'] = pd.to_numeric(exemplo1['RANK_2024'], errors='coerce')
exemplo1['RANK_2025'] = pd.to_numeric(exemplo1['RANK_2025'], errors='coerce')
exemplo1['Gain'] = exemplo1['RANK_2025'] - exemplo1['RANK_2024']
exemplo1 = exemplo1.sort_values('Gain', ascending=True).head(20)
colors = exemplo1['Gain'].apply(lambda x: 'green' if x < 0 else 'red')
print('\n\n', exemplo1[['RANK_2025', 'RANK_2024','Gain','Institution_Name', 'Location']].head(20))
# Plot
plt.figure(figsize=(14, 8))
bars = plt.barh(exemplo1['Institution_Name'], exemplo1['Gain'], color=colors)

# Anota o valor de Gain ao lado de cada barra
for bar in bars:
    width = bar.get_width()
    plt.text(width + 0.5 if width >= 0 else width - 1.5,
             bar.get_y() + bar.get_height() / 2,
             f'{int(width)}', va='center', ha='left' if width >= 0 else 'right')

plt.title('Variação de Rank (2024 → 2025) das Universidades dos EUA')
plt.xlabel('Posições Ganhas (+) ou Perdidas (–)')
plt.ylabel('Instituição')
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()