import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

dados = pd.read_csv('Estudo/cap14/dataset.csv')

# Regressão Linear

# Queremos modelar a relação entre uma variável dependente
# e uma ou mais variáveis independentes

# No StatsModels temos a função OLS(y,X) para ajustar um modelo de regressão linear
# Recebe dois parâmetros, y é a variável dependente, e X são as variáveis independentes

# Exemplo:

y = dados['valor_aluguel']
X = dados['area_m2']

# O statsmodels requer a adição de uma constante à variável independente
X = sm.add_constant(X)

# Criando o modelo
modelo = sm.OLS(y,X)
# Treinamento do modelo
resultado = modelo.fit()

# Resultados
print(resultado.summary())

# Interpretando os resultados:

# R^2: interpreta quão bem o modelo se ajusta aos dados, entre 0 e 1
# 0: não é útil, 1: Perfeito

# Mostrando nossos resultados em um gráfico
plt.figure(figsize = (12,8))
plt.xlabel('area_m2', size = 16)
plt.ylabel('valor_aluguel', size = 16)
plt.plot(X['area_m2'], y, "o", label = 'Dados Reais')
plt.plot(X['area_m2'], resultado.fittedvalues, "r-", label = "Linha de Regressão (Previsões do Modelo)")
plt.legend(loc = "best")
plt.show()