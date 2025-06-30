import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import os

ARQUIVO = 'Praticando/Teste/dados_regressao.csv'

# Função para carregar dados do arquivo, se existir
def carregar_dados():
    if os.path.exists(ARQUIVO):
        df = pd.read_csv(ARQUIVO)
        X = df['X'].values.reshape(-1, 1)
        y = df['Y'].values
        print(f"Carregados {len(df)} pontos do arquivo '{ARQUIVO}'.")
        return X.tolist(), y.tolist()
    else:
        print(f"Nenhum arquivo encontrado. Começando com dados vazios.")
        return [], []

# Função para salvar dados no arquivo
def salvar_dados(X_data, y_data):
    df = pd.DataFrame({'X': [x[0] for x in X_data], 'Y': y_data})
    df.to_csv(ARQUIVO, index=False)
    print(f"Dados salvos no arquivo '{ARQUIVO}'.")

# Função para inserir dado e ajustar modelo a cada 10 pontos
def inserir_dado(x, y, X_data, y_data, model):
    X_data.append(x)
    y_data.append(y)
    if len(X_data) % 10 == 0:
        X_train = np.array(X_data)
        y_train = np.array(y_data)
        model.fit(X_train, y_train)
        print(f"\nModelo ajustado com {len(X_data)} pontos.")
    if len(X_data) >= 10:
        pred = model.predict([x])
        return pred[0]
    else:
        return None

# Função para plotar
def plotar_regressao(X_data, y_data, model):
    X = np.array(X_data).reshape(-1)
    y = np.array(y_data)
    plt.scatter(X, y, color='blue', label='Dados reais')
    X_range = np.linspace(X.min(), X.max(), 100)
    y_pred = model.predict(X_range.reshape(-1,1))
    plt.plot(X_range, y_pred, color='red', label='Linha de regressão')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Regressão Linear')
    plt.legend()
    plt.show()

def main():
    X_data, y_data = carregar_dados()
    model = LinearRegression()
    
    # Se já tem 10+ pontos, treina o modelo antes de iniciar
    if len(X_data) >= 10:
        model.fit(np.array(X_data), np.array(y_data))
        print(f"Modelo treinado com dados existentes ({len(X_data)} pontos).")
    
    print("Digite seus dados para regressão linear. Para sair, digite 'sair'.")
    
    while True:
        entrada_x = input("\nDigite o valor de X (ex: 5.2): ")
        if entrada_x.lower() == 'sair':
            break
        entrada_y = input("Digite o valor de Y (ex: 10.5): ")
        if entrada_y.lower() == 'sair':
            break
        try:
            x_val = [float(entrada_x)]
            y_val = float(entrada_y)
        except ValueError:
            print("Valor inválido! Tente novamente.")
            continue
        
        pred = inserir_dado(x_val, y_val, X_data, y_data, model)
        if pred is not None:
            print(f"Previsão do modelo para X={x_val[0]}: {pred:.3f}")
        else:
            print("Ainda não há dados suficientes para treinar o modelo (mínimo 10 pontos).")
    
    print("\nEncerrado.")
    salvar_dados(X_data, y_data)
    
    if len(X_data) >= 10:
        plotar_regressao(X_data, y_data, model)
    else:
        print("Não há dados suficientes para plotar (mínimo 10).")

if __name__ == "__main__":
    main()
