# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
     def __init__(self, palavra):
          self.palavra = palavra.lower().strip()
          self.guesses = []
          self.num_erros = 0
          self.max_erros = len(board) - 1

	# Método para adivinhar a letra
     def guess(self, letra):
          letra = letra.lower()
          if letra in self.guesses:
               print("\nVoce já digitou essa letra!")
          elif letra in self.palavra:
               self.guesses.append(letra)
               print("\nParabens, voce acertou uma letra!")
          else:
               self.guesses.append(letra)
               self.num_erros += 1
               print(f"\nA letra {letra} não está na palavra")
	
	# Método para verificar se o jogo terminou
     def terminou(self):
          return self.num_erros >= self.max_erros or self.ganhou()
     
	# Método para verificar se o jogador venceu
     def ganhou(self):
          return all(letra in self.guesses for letra in self.palavra)
     
	# Método para não mostrar a letra no board
     def printa_escondido(self):
          return ' '.join([letra if letra in self.guesses else '_' for letra in self.palavra])
		
	# Método para checar o status do game e imprimir o board na tela
     def printa_status(self):
          print(board[self.num_erros])
          print("\nPalavra:", self.printa_escondido())
          print("Letras utilizadas:", ' '.join(self.guesses))
          print(f"Erros: {self.num_erros} de {self.max_erros} possiveis.\n")


# Função para retornar uma palavra aleatória
def palavra_aleatoria():
     lista = ["rama", "safira", "mirtilo", "nebulosa", "magnólia", "bumerangue", "caleidoscópio", "crisântemo", "prisma", "relíquia",
     "chaminé", "girassol", "abóbora", "ciclone", "trapézio", "escultura", "harpista", "labareda", "miragem", "lenhador",
     "pergaminho", "vitral", "azulejo", "serenata", "borboleta", "trompete", "sarcófago", "brisa", "coral",
     "tangerina", "lótus", "foguete", "bússola", "moinho", "pérola", "búfalo", "esmeralda", "caravela", "marfim", "farol",
     "cristal", "trovão", "ópera", "sinfonia", "orquídea", "oceano", "abismo", "iglu", "fantasma", "galáxia", "cantilena",
     "clarinete", "carrossel", "poltrona", "xícara", "labirinto", "ametista", "alicate", "pistache", "vulcão", "foice",
     "metrópole", "alfazema", "camaleão", "equação", "catapulta", "pergolado", "jazida", "picolé", "relâmpago", "aquarela",
     "estalactite", "holograma", "harpa", "destilado", "cacto", "riacho", "lilás", "violino", "compasso", "mirante", "véu",
     "fóssil", "esgrima", "telescópio", "alquimia", "espiral", "montanha", "relógio", "constelação", "espectro", "xilofone",
     "coruja", "arqueiro", "burburinho", "biblioteca", "Idrissa", "Tyler", "oss", "ossablessed", "euforia", "Marrocos",
     "pecador", "mafe", "nazismo", "andre", "jonas", "judas", "poker", "face", "didier"]
     return random.choice(lista)

# Função principal do jogo
def main():
     print("Bem vindo ao jogo da forca!")
     jogo = Hangman(palavra_aleatoria())
     while not jogo.terminou():
          jogo.printa_status()
          letra = input("\nDigite uma letra:").strip()
          if letra:
               jogo.guess(letra)
     
     jogo.printa_status()
     if jogo.ganhou():
          print("\nParabéns, você acertou a palavra")
     else:
          print(f"\nQue pena, a palavra era: {jogo.palavra}")

if __name__ == "__main__":
     main()

