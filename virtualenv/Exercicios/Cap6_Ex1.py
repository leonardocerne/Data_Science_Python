# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.

def cubo(list):
    for x in list:
        print(x**2)

list = []
for i in range(3):
    x = int(input("Digite um numero"))
    list.append(x)
cubo(list)
