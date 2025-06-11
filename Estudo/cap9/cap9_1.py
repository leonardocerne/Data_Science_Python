import numpy as dsa
import os
import matplotlib.pyplot as plt
#array numpy
arr1 = dsa.array([10, 20, 30, 43, 213, 4,23, 5423,32444])
#imprime do indice 2 ao 4 (2,3)
print(arr1[2:4])
#imprime os indices do vetor de indices
inds = [1, 3, 5]
print("\n", arr1[inds])
#mascara para array
mask = (arr1 % 3 == 0)
print("\n", mask)
print("\n", arr1[mask])
#vaimultiplicando
print("\n", arr1.cumprod())
#faz array de 0 a 50 de 5 em 5
arr2 = dsa.arange(0,50,5)
print("\n", arr2)
#faz array com 20 0s
arr3 = dsa.zeros(20)
print("\n", arr3)
#faz matriz id com n=5
arr4 = dsa.eye(5)
print("\n", arr4)
#faz uma matriz diagonal com os valores do array
arr5 = dsa.diag(dsa.array([1,2,3,4]))
print("\n", arr5)
#array de valores booleanos
arr6 = dsa.array([True, False, False, True])
print("\n", arr6)
#array de strings
arr7 = dsa.array(["X", "y", "Vasco"])
print("\n", arr7)
#retorna um numero de valores igualmente distribuidos no 
# intervalo especificado
print("\n", dsa.linspace(0,100, 11))
# retorna uma sequência de números igualmente espaçados 
# em escala logarítmica dentro de um intervalo especificado
print("\n", dsa.logspace(0, 5, 10))
#criando matriz
arr8 = dsa.array([[1,2,3], [4,5,6]])
print("\n", arr8)
#criando uma matriz aenas com numerso 1
arr9 = dsa.ones((2,3))
print(arr9)
#lista de listas
lista = [[42,53,64], [123,22,3], [90,8,1]]
#cria matriz a partir de uma lista de listas
arr10 = dsa.matrix(lista)
print("\n", arr10)
#tamanho da matriz
print("\n", arr10.size)
#indexação da matriz
print("\n", arr10[2,1], arr10[0:2,2])
#alterando elemmento da matriz
arr10[1,0] = 100
#forçando tipo de dado
arr11 = dsa.array([1,2], dtype=dsa.float64)
print("\n", arr11)

#manipulando arquivos
filename = os.path.join('Estudo/dataset.csv')
arr12 = dsa.loadtxt(filename, delimiter = ',', usecols=(0,1,2,3), skiprows=1)
print("\n", arr12)
var1, var2 = dsa.loadtxt(filename, delimiter = ',', usecols = (0,1), skiprows = 1, unpack = True)
plt.plot(arr12, 'o', markersize = 6, color = 'red')
plt.show()

arr13 = dsa.array([15,23,63,44,33,122])
#media
print("\n",dsa.mean(arr13))
#desvio padrao
print("\n", dsa.std(arr13))
#variancia
print("\n", dsa.var(arr13))

#soma dos elementos do array
print("\n", dsa.sum(arr13))
#produto
print("\n", dsa.prod(arr13))
#somando dois arrays
arr14 = dsa.array([1,1,1])
arr15 = dsa.array([2,3,4])
arr16 = dsa.add(arr14, arr15)
print(arr16)
#multiplicando duas matrizes
arr17 = dsa.array([[2,2], [3,3]])
arr18 = dsa.array([[4,4], [5,5]])
arr19 = dsa.dot(arr17, arr18)
print("\n", arr19)
arr20 = arr17 @ arr18
print("\n", arr20)
