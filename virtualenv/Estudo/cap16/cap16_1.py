# Problema de negócio: Usando dados históricos das vendas ao longo de 2023
# seria possível prever o total de vendas em Janeiro/2024?

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

dados = pd.read_csv('Estudo/cap16/dataset.csv')

print('\nDados que possuímos:\n', dados.head(), '\n', dados.tail())

# Processando dados
dados['Data'] = pd.to_datetime(dados['Data'])

# Convertendo o dataframe em uma série temporal
serie_temporal = dados.set_index('Data')['Total_Vendas']

# Fornecendo frequencia da série temporal
serie_temporal = serie_temporal.asfreq('D')

# Criando gráfico da série temporal
plt.figure(figsize=(12, 6))
plt.plot(serie_temporal)
plt.xlabel('Data')
plt.ylabel('Vendas')
plt.title('Serie temporal de Vendas')
plt.grid(True)
plt.show()

# Suavização Exponencial:
# suavização exponencial é uma técnica de análise e previsão de séries temporais
# que aplica médias ponderadas aos dados históricos, onde os pesos diminuem exponencialmente à medida que
# os dados ficam mais antigos

# Criando modelo
modelo = SimpleExpSmoothing(serie_temporal)

# Treinamento do modelo
modelo_ajustado = modelo.fit(smoothing_level = 0.2)

# Extraindo os valores previstos pelo modelo
suavizacao_exponencial = modelo_ajustado.fittedvalues

# Grafico dos valores reais x valores previstos
plt.figure(figsize = (12,6))
plt.plot(serie_temporal, label = 'Valores Reais')
plt.plot(suavizacao_exponencial, label = 'Valores Previstos', linestyle = '--')
plt.xlabel('Data')
plt.ylabel('Vendas')
plt.title('Modelo de Suavização Exponencial')
plt.legend()
plt.show()

# Fazendo previsoes
previsoes = modelo_ajustado.forecast(steps = 1)
print('\nPrevisao do Total de Vendas para Janeiro/2024:', round(previsoes.iloc[0], 4))
