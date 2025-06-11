import random
import numpy as np
import pandas as pd
import matplotlib as mat
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import seaborn as sea

dados = pd.read_csv("Estudo/cap11/tips.csv")
print(dados.head())

# O método joinplot cria plot de 2 variáveis com gráficos bivariados e univariados
sea.jointplot(data = dados, x = "total_bill", y = "tip", kind = 'reg')
plt.show()

# O método lmplot() cria plot com dados e modelos de regressão
sea.lmplot(data = dados, x = "total_bill", y = "tip", col = "smoker")
plt.show()

df = pd.DataFrame()
df['idade'] = random.sample(range(20,100), 30)
df['peso'] = random.sample(range(55, 150), 30)
print(df.head())

# lmplot
sea.lmplot(data = df, x = "idade", y = "peso", fit_reg = True)
plt.show()

# kdeplot
sea.kdeplot(df.idade)
plt.show()

# Valores randômicos
np.random.seed(42)
n = 1000
pct_smokers = 0.2

# Variáveis
flag_fumante = np.random.rand(n) < pct_smokers
idade = np.random.normal(40, 10, n)
altura = np.random.normal(170, 10, n)
peso = np.random.normal(70, 10, n)

# Dataframe
dados = pd.DataFrame({'altura': altura, 'peso': peso, 'flag_fumante': flag_fumante})

# Cria os dados para a variável flag_fumante
dados['flag_fumante'] = dados['flag_fumante'].map({True: 'Fumante', False: 'Não Fumante'})
# Style
sea.set(style = "ticks")

# lmplot
sea.lmplot(x = 'altura', 
           y = 'peso', 
           data = dados, 
           hue = 'flag_fumante', 
           palette = ['tab:blue', 'tab:orange'], 
           height = 7)

# Labels e título
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.title('Relação Entre Altura e Peso de Fumantes e Não Fumantes')

# Remove as bordas
sea.despine()

# Show
plt.show()