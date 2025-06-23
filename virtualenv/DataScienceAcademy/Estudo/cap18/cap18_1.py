import random
import  plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime


dados = pd.read_csv('Estudo/Cap18/dataset.csv')

# Imprimindo dados
print('Dados:\n', dados.head())

# Candlestick para mostrar gráfico financeiro
fig = go.Figure(data = [go.Candlestick(x = dados['Date'],
                open = dados['AAPL.Open'],
                high = dados['AAPL.High'],
                low = dados['AAPL.Low'],
                close = dados['AAPL.Close'])])
fig.show()

# Vamos trabalhar com a cotação de fechamento da ação da Apple
precos = dados['AAPL.Close'].values

# Configuração do Algoritmo Q-Learning
print('\n Definindo os Hiperparâmetros do Q-Learning..')
num_episodios = 1000
alfa = 0.1
gama = 0.99
epsilon = 0.1

# Configuração do ambiente de negociação
print('\nConfigurando o Ambiente de Negociação...')
acoes = ['comprar', 'vender', 'manter']
saldo_inicial = 1000
num_acoes_inicial = 0

# Funcao para executar uma ação e retornar a recompensa e o próximo estado

def executar_acao(estado, acao, saldo, num_acoes, preco):
    #Acao de comprar
    if acao == 0:
        if saldo >= preco:
            num_acoes += 1
            saldo -= preco
        
    #acao de vender
    elif acao == 1:
        if num_acoes > 0:
            num_acoes -= 1
            saldo += preco
        
    #define o lucro
    lucro = saldo + num_acoes * preco - saldo_inicial

    return (saldo, num_acoes, lucro)


# Inicializando tabela Q
print('\nInicializando a Tabela Q...')
q_tabela = np.zeros((len(precos), len(acoes)))

# Treinamento
print('\nINICIANDO TREINAMENTO...\n')
for _ in range(num_episodios):
    #define o saldo
    saldo = saldo_inicial
    #define o número de ações
    num_acoes = num_acoes_inicial

    #LOOP
    for i, preco in enumerate(precos[:-1]):
        estado = i
        # Escolher a ação usando a política epsilon-greedy
        if np.random.random() < epsilon:
            acao = random.choice(range(len(acoes)))
        else:
            acao = np.argmax(q_tabela[estado])
        
        # Executar a ação e obter a recompensa e o próximo estado
        saldo, num_acoes, lucro = executar_acao(estado, acao, saldo, num_acoes, preco)
        prox_estado = i + 1
        # Atualizando a tabela Q
        q_tabela[estado][acao] += alfa * (lucro + gama * np.max(q_tabela[prox_estado]) - q_tabela[estado][acao])
print('\nFINALIZANDO TREINAMENTO')

# Valores iniciais para testar o agente
saldo = saldo_inicial
num_acoes = num_acoes_inicial

print('\nExecutando o Agente...')
for i, preco in enumerate(precos[:-1]):
    estado = i
    acao = np.argmax(q_tabela[estado])
    saldo, num_acoes, _ = executar_acao(estado, acao, saldo, num_acoes, preco)
print('\nExecução Concluída')

print('\nNúmero de ações:', num_acoes)
print('Preço:', precos[-1])

# Vendendo todas as ações no último preço
saldo += num_acoes * precos[-1]
lucro = saldo - saldo_inicial
lucro_final = round(lucro, 2)
print('\nComeçamos a Negociação com Saldo Inicial de 1000 e Tivemos Lucro de:', lucro_final)



