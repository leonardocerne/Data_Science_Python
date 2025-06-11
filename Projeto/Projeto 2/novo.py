import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def autopct_format(values): 
    def my_format(pct): 
        total = sum(values) 
        val = int(round(pct * total / 100.0))
        return f' $ {val:d}'
    return my_format

# Lendo o CSV
dados = pd.DataFrame(pd.read_csv('Projeto/Projeto 2/dataset.csv'))
dados['Data_Pedido'] = pd.to_datetime(dados['Data_Pedido'], format='%d/%m/%Y')
dados['Ano'] = dados['Data_Pedido'].dt.year
dados['Mes'] = dados['Data_Pedido'].dt.month

# Loop interativo
while True:
    print("\nEscolha uma opção:")
    print("1 - Cidade com Maior Valor de Venda (Office Supplies)")
    print("2 - Total de Vendas por Data do Pedido (Gráfico de Barras)")
    print("3 - Total de Vendas por Estado (Gráfico de Barras)")
    print("4 - Top 10 Cidades com Maior Total de Vendas (Gráfico de Barras)")
    print("5 - Segmento com Maior Total de Vendas (Gráfico de Pizza)")
    print("6 - Total de Vendas por Segmento e Ano")
    print("7 - Simulação de Descontos (15% >1000, senão 10%)")
    print("8 - Média de Venda Antes/Depois do Desconto de 15%")
    print("9 - Média de Vendas por Segmento, Ano e Mês (Gráfico de Linhas)")
    print("10 - Total de Vendas por Categoria/SubCategoria (Top 12 SubCategorias)")
    print("11 - Imprimir DataFrame")
    print("0 - Sair")

    escolha = input("Digite o número da pergunta: ")

    if escolha == '1':
        resposta1 = dados[dados['Categoria'] == 'Office Supplies'].groupby('Cidade')['Valor_Venda'].sum().idxmax()
        print("Resposta:", resposta1)

    elif escolha == '2':
        resposta2 = dados.groupby(dados['Data_Pedido'].dt.to_period('M'))['Valor_Venda'].sum()
        resposta2.index = resposta2.index.astype(str)
        plt.figure(figsize=(13,6))
        plt.bar(resposta2.index, resposta2.values)
        plt.title("Total de Vendas por Mês")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    elif escolha == '3':
        resposta3 = dados.groupby('Estado')['Valor_Venda'].sum()
        plt.figure(figsize=(13,6))
        plt.bar(resposta3.index, resposta3.values)
        plt.title("Total de Vendas por Estado")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    elif escolha == '4':
        resposta4 = dados.groupby('Cidade')['Valor_Venda'].sum().sort_values(ascending=False).head(10)
        plt.figure(figsize=(7,6))
        plt.bar(resposta4.index, resposta4.values)
        plt.title("Top 10 Cidades com Maior Total de Vendas")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    elif escolha == '5':
        resposta5 = dados.groupby('Segmento')['Valor_Venda'].sum()
        plt.figure(figsize=(8,8))
        plt.pie(resposta5.values, labels=resposta5.index, autopct=autopct_format(resposta5.values))
        plt.title("Total de Vendas por Segmento")
        plt.show()

    elif escolha == '6':
        resposta6 = dados.groupby(['Segmento', 'Ano'])['Valor_Venda'].sum()
        print(resposta6)

    elif escolha == '7':
        dados['Desconto'] = np.where(dados['Valor_Venda'] > 1000, 0.15, 0.10)
        resposta7 = dados['Desconto'].value_counts()
        print("Distribuição de Descontos Aplicados:")
        print(resposta7)

    elif escolha == '8':
        media_antes = dados['Valor_Venda'].mean()
        dados['Valor_Venda'] = np.where(dados['Desconto'] == 0.15, dados['Valor_Venda'] * 0.85, dados['Valor_Venda'])
        media_depois = dados['Valor_Venda'].mean()
        print("Média Antes do Desconto de 15%:", media_antes)
        print("Média Depois:", media_depois)

    elif escolha == '9':
        media_segmento = dados.groupby(['Segmento', 'Ano', 'Mes'])['Valor_Venda'].mean().reset_index()
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=media_segmento, x='Mes', y='Valor_Venda', hue='Segmento', style='Ano', markers=True, dashes=False)
        plt.title('Média de Vendas por Segmento - Por Ano e Mês')
        plt.xticks(range(1, 13))
        plt.tight_layout()
        plt.show()

    elif escolha == '10':
        total_cat_sub = dados.groupby(['Categoria', 'SubCategoria'])['Valor_Venda'].sum().reset_index()
        top12 = total_cat_sub.sort_values(by='Valor_Venda', ascending=False).head(12)
        plt.figure(figsize=(14, 6))
        sns.barplot(data=top12, x='SubCategoria', y='Valor_Venda', hue='Categoria')
        plt.title("Total de Vendas por Categoria e SubCategoria (Top 12)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    elif escolha == '11':
        n = int(input("Digite quantas linhas deseja mostrar:"))
        print(dados.head(n))

    elif escolha == '0':
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")