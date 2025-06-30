# Exercício 3 - Calcule a matriz transposta da matriz abaixo.
# Caso não saiba o que é matriz transposta, visite este link: https://pt.wikipedia.org/wiki/Matriz_transposta
# Matriz transposta é um conceito fundamental na construção de redes neurais artificiais, base de sistemas de IA.


def matriz_transposta(matriz):
    resposta = []
    numlinhas = len(matriz)
    numcolunas = len(matriz[0])
    for i in range(numcolunas):
        novo = []
        for j in range(numlinhas):
            novo.append(matriz[j][i])
        resposta.append(novo)
    return resposta

matrix = [[1,2], [3,4], [5,6], [7,8]]
r = matriz_transposta(matrix)
print(r)
