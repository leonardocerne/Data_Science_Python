# Exercício 2 - Reescreva o código abaixo, usando a função map(). O resultado final deve ser o mesmo!
#palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil.'.split()
#esultado = [[w.upper(), w.lower(), len(w)] for w in palavras]
#for i in resultado:
#   print (i)

def f(w):
    return [w.upper(), w.lower(), len(w)]
palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil.'.split()
resultado = list(map(f, palavras))
for i in resultado:
    print(i)
