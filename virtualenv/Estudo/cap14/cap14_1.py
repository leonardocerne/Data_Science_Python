import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

dados = pd.read_csv('Estudo/cap14/dataset.csv')

print('Esses são os dados que iremos trabalhar:\n', dados.head(10))

print('\nVerificando se o Data Frame que possuímos possui valores nulos:\n', dados.isnull().sum())

print('\nResumo estatístico geral:\n', dados.describe())

print('\nResumo estatístico específico\n', dados['valor_aluguel'].describe())

# Histograma de uma coluna específica
sns.histplot(data = dados,x = dados['valor_aluguel'], kde = True)
plt.show()

#O coeficiente de correlação é uma medida estatística que indica a força e a direção da relação linear entre duas variáveis numéricas. Ele varia entre -1 e 1, onde:
#Um coeficiente de correlação igual a 1 indica uma correlação linear perfeita positiva, ou seja, quando uma variável aumenta, a outra variável também aumenta na mesma proporção.
#Um coeficiente de correlação igual a -1 indica uma correlação linear perfeita negativa, ou seja, quando uma variável aumenta, a outra variável diminui na mesma proporção.
#Um coeficiente de correlação igual a 0 sugere que não há correlação linear entre as duas variáveis.
#O coeficiente de correlação mais comum é o de Pearson, que mede a correlação linear entre duas variáveis. 
#Existem outras medidas de correlação, como o coeficiente de correlação de Spearman, que avalia a relação monotônica entre duas variáveis, e o coeficiente de correlação de Kendall, que considera a concordância entre os rankings das variáveis.
print('\nCorrelação entre colunas:', dados.corr())

# Analisando relação entre a área por metros quadrados e o valor_aluguel
sns.scatterplot(data = dados, x = 'area_m2', y = 'valor_aluguel')
plt.show()



