import random
from os import system, name

def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def imprime_erros(listaerros):
    print("Letras erradas:", end= ' ')
    for i in listaerros:
        print(f"{i}", end=' ')
    print()

def imprime(lista):
    print("___\n| |\n|\n|", end=' ')
    for i in lista:
        print(f"{i}", end=' ')
    print()

def game():
    limpa_tela()
    lista_de_palavras = ["vasco", "botafogo", "banana", "portugal", "escritorio", "caderno"]
    palavra = random.choice(lista_de_palavras)
    listapalavra = list(palavra.strip())
    listaresposta = ['_'] * len(listapalavra)
    listaerros = []
    print("Tente acertar essa palavra:")
    imprime(listaresposta)
    while listaresposta != listapalavra:
        x = input("\nDigite uma letra: ").lower()
        if x in set(listapalavra):
            for i in range(len(listaresposta)):
                if listapalavra[i] == x:
                    listaresposta[i] = x
        else:
            print(f"A letra {x} nao esta na palavra")
            listaerros.append(x)
            if(len(listaerros) == 5):
                break
        imprime_erros(listaerros)
        imprime(listaresposta)

    if listaresposta != listapalavra:
        print(f"Que pena, voce perdeu, a palavra certa era {palavra}")
    else:
        print(f"Parabens, voce acertou a palavra {palavra} com {len(listaerros)} erros")

        

game()
