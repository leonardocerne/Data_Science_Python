# Exercício 7 - Usando a função filter(), encontre os valores que são comuns às duas listas abaixo.

a = [1,2,3,4,7,9]
b = [2,3,5,6,7,8]

resultado = list(filter(lambda x: x in set(a), b))
print(resultado)