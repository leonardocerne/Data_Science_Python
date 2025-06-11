# Criar notebook para análise de convergência: raiz simples, dupla e tripla
import nbformat as nbf
from pathlib import Path

nb = nbf.v4.new_notebook()
cells = []

# Título e introdução
cells.append(nbf.v4.new_markdown_cell("# Análise de Convergência do Método de Newton-Raphson\n\nEste notebook compara a convergência do método de Newton-Raphson em três casos distintos:\n- Raiz simples\n- Raiz dupla\n- Raiz tripla\n\nSerão apresentados os gráficos dos polinômios, as aproximações sucessivas e os gráficos de convergência."))

# Imports
cells.append(nbf.v4.new_code_cell("""\
import numpy as np
import matplotlib.pyplot as plt
"""))

# Método Newton-Raphson com histórico
cells.append(nbf.v4.new_code_cell("""\
def newton_raphson_n(f, df, alpha, x0, tol=1e-8, n_iter=50):
    xs = [x0]
    desvios = []
    x = x0
    for i in range(n_iter):
        fx = f(x) - alpha
        dfx = df(x)
        if abs(dfx) < 1e-12:
            break  # evita divisão por zero
        x_new = x - fx / dfx
        desvio = abs(x - x_new)
        xs.append(x_new)
        desvios.append(desvio)
        if desvio < tol:
            break
        x = x_new
    return xs, desvios
"""))

# Definição das funções: simples, dupla, tripla
cells.append(nbf.v4.new_code_cell("""\
# Raiz simples: f(x) = (x - 1)(x + 1)(x - 2)(x + 2)
def f_simples(x):
    return (x - 1)*(x + 1)*(x - 2)*(x + 2)
def df_simples(x):
    p = np.poly1d([1, 0, -6, 0, 4])  # Expandido
    return np.polyder(p)(x)

# Raiz dupla: f(x) = (x - 1)**2 * (x + 1)*(x - 2)
def f_dupla(x):
    return (x - 1)**2 * (x + 1)*(x - 2)
def df_dupla(x):
    p = np.poly1d([1, -2, -1, 4, -2])  # Expandido
    return np.polyder(p)(x)

# Raiz tripla: f(x) = (x - 1)**3 * (x + 2)
def f_tripla(x):
    return (x - 1)**3 * (x + 2)
def df_tripla(x):
    p = np.poly1d([1, -1, -5, 5, 2])  # Expandido
    return np.polyder(p)(x)
"""))

# Função de plot dos polinômios
cells.append(nbf.v4.new_code_cell("""\
def plot_func(f, title, raiz_esperada=None):
    x = np.linspace(-3, 3, 400)
    y = f(x)
    plt.figure(figsize=(6,4))
    plt.axhline(0, color='gray', linestyle='--')
    plt.plot(x, y, label='f(x)')
    if raiz_esperada is not None:
        plt.axvline(raiz_esperada, color='red', linestyle='--', label='Raiz esperada')
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()
"""))

# Plotar as 3 funções
cells.append(nbf.v4.new_markdown_cell("## Gráficos dos Polinômios"))
cells.append(nbf.v4.new_code_cell("""\
plot_func(f_simples, "Polinômio com raiz simples (x = 1)", raiz_esperada=1)
plot_func(f_dupla, "Polinômio com raiz dupla (x = 1)", raiz_esperada=1)
plot_func(f_tripla, "Polinômio com raiz tripla (x = 1)", raiz_esperada=1)
"""))

# Testar convergência e plotar desvios
cells.append(nbf.v4.new_markdown_cell("## Gráficos de Convergência dos Desvios"))
cells.append(nbf.v4.new_code_cell("""\
def plot_convergencia(f, df, nome, x0, cor):
    _, desvios = newton_raphson_n(f, df, 0, x0)
    plt.semilogy(range(1, len(desvios)+1), desvios, marker='o', label=nome, color=cor)
    plt.xlabel("Iteração")
    plt.ylabel("Desvio (log)")
    plt.title("Convergência do Método de Newton-Raphson")
    plt.grid(True)

plot_convergencia(f_simples, df_simples, "Raiz simples", 1.1, 'blue')
plot_convergencia(f_dupla, df_dupla, "Raiz dupla", 1.1, 'green')
plot_convergencia(f_tripla, df_tripla, "Raiz tripla", 1.1, 'red')
plt.legend()
plt.show()
"""))

# Análise crítica
cells.append(nbf.v4.new_markdown_cell("## Análise Crítica dos Resultados\n\n- **Raiz simples:** converge rapidamente de forma quadrática.\n- **Raiz dupla:** convergência mais lenta, quase linear.\n- **Raiz tripla:** convergência ainda mais lenta e instável dependendo do chute inicial.\n\nEsses resultados estão de acordo com a teoria:\n- Quanto maior a multiplicidade da raiz, mais lenta é a convergência do método de Newton-Raphson.\n- Para raízes múltiplas, métodos modificados são preferíveis."))

# Finalizar notebook
nb['cells'] = cells
output_path = Path("analise_convergencia_newton_raphson.ipynb")
with open(output_path, "w") as f:
    nbf.write(nb, f)

output_path