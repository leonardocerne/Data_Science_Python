import pandas as pd
from pandas import DataFrame
import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

data = load_iris()
df = pd.DataFrame(data['data'], columns=data['feature_names'])
df['species'] = data['target']
print(df.head())
# Para criar um gráfico de linhas com todas as variáveis do dataframe, basta fazer isso:
df.plot()

# Que tal um scatter plot com duas variáveis? 
df.plot.scatter(x = 'sepal length (cm)', y = 'sepal width (cm)')

# E mesmo gráficos mais complexos, como um gráfico de área, pode ser criado:
columns = ['sepal length (cm)', 'petal length (cm)', 'petal width (cm)', 'sepal width (cm)']
df[columns].plot.area()

# Calculamos a média das colunas agrupando pela coluna species e criamos um gráfico de barras com o resultado
df.groupby('species').mean().plot.bar()

# Ou então, fazemos a contagem de classes da coluna species e plotamos em um gráfico de pizza
df.groupby('species').count().plot.pie(y = 'sepal length (cm)')
plt.show()