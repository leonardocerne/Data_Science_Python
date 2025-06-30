import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Importando os dados
dados = pd.read_csv('Estudo/cap15/dataset.csv')

print('Colunas:\n', dados.columns)

print('\nExemplo dos dados:\n', dados.head())

# Verificando se há valores ausentes
print('\nValores ausentes:\n', dados.isnull().sum())

# Verificando correlação
print('\nCorrelação:\n', dados.corr())

# Resumo estatístico do dataset
print('\nResumo estatístico:\n', dados.describe())

# Nossa variável preditora será a 'horas_estudo_mes'
# Histograma da variável preditora
sns.histplot(data = dados, x = 'horas_estudo_mes', kde = True)
plt.show()

# Preparando a variável de entrada X
X = np.array(dados['horas_estudo_mes'])
X = X.reshape(-1,1)

# Preparando a variável alvo
y = dados['salario']

# Gráfico de dispersão entre X e y
plt.scatter(X, y, color = "blue", label = "Dados Reais Históricos")
plt.xlabel("Horas de Estudo")
plt.ylabel("Salario")
plt.legend()
plt.show()

# Dividir dados em treinamento e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)

# Criando o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(X_treino, y_treino)

# Visualizando a reta de regressão linear e os dados reais usados no treinamento
plt.scatter(X,y, color = "blue", label = "Dados Reais Históricos")
plt.plot(X, modelo.predict(X), color = "red", label = "Reta de Regressão")
plt.xlabel("Horas de Estudo")
plt.ylabel("Salario")
plt.legend()
plt.show()

# Avaliando modelo
score = modelo.score(X_teste, y_teste)
print(f"Coeficiente R^2: {score:.2f}")

# Usando o modelo para prever salários

horas_estudo_novo = np.array([[48]])
salario_previsto = modelo.predict(horas_estudo_novo)
print(f"\nSe voce estudar cerca de ", horas_estudo_novo, " horas por mês, seu salário pode ser igual a ", salario_previsto)

# O modelo achou dois coeficientes w0 e w1 para achar um y_novo a partir de y_novo = w0 + w1 * X
# ou seja, se fizermos na mão o mesmo cálculo mas com os coeficientes

salario = modelo.intercept_ + (modelo.coef_ * horas_estudo_novo)
print("\nSalario: ", salario)

# Podemos prever para arrays inteiros
arrayhoras = np.array([[73], [28], [65]])
salarios_previstos = modelo.predict(arrayhoras)
print("\nArray de Horas:\n", arrayhoras, "\n\nPrevisões:\n", salarios_previstos)
