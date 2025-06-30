import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

resposta = pd.read_csv('Praticando/PremierLeague/premier_league.csv')

numeric = resposta.select_dtypes(include='number')

plt.figure(figsize=(16, 12))
sns.heatmap(numeric.corr(), cmap='coolwarm', annot=False, linewidths=0.5)
plt.title('Mapa de Correlação entre Métricas dos Jogadores')
plt.tight_layout()
plt.savefig('Praticando/PremierLeague/mapa_de_corr.png')


# Seleciona apenas colunas numéricas
df_num = resposta.select_dtypes(include='number').dropna(axis=1)

# Remove colunas com baixa variação (opcional)
df_num = df_num.loc[:, df_num.std() > 0.01]

# Padroniza os dados (zero média, variância 1)
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_num)

pca = PCA(n_components=2)
pca_result = pca.fit_transform(df_scaled)

# DataFrame com os resultados do PCA
df_pca = pd.DataFrame(pca_result, columns=['PC1', 'PC2'])
df_pca['Player Name'] = resposta['Player Name'].values

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
df_pca['Cluster'] = kmeans.fit_predict(pca_result)

plt.figure(figsize=(12, 8))
sns.scatterplot(
    data=df_pca,
    x='PC1', y='PC2',
    hue='Cluster',
    palette='Set2',
    s=100,
    alpha=0.8
)

plt.title('Agrupamento de Jogadores com PCA + KMeans')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.legend(title='Cluster')
plt.grid(True)
plt.tight_layout()
plt.savefig('Praticando/PremierLeague/agrupamento_por_cluster')

resposta_com_cluster = resposta.copy()
resposta_com_cluster['Cluster'] = df_pca['Cluster']

# Agrupa por cluster e calcula média das estatísticas numéricas
cluster_description = resposta_com_cluster.groupby('Cluster').mean(numeric_only=True)

# Exibe (ou salva) o resumo
pd.set_option('display.max_columns', None)  # Mostrar todas as colunas
print(cluster_description)

plt.figure(figsize=(16, 8))
sns.heatmap(cluster_description.T, cmap='YlGnBu', annot=True, fmt=".1f", linewidths=0.5)
plt.title('Perfil Médio dos Jogadores por Cluster')
plt.xlabel('Cluster')
plt.ylabel('Métrica')
plt.tight_layout()
plt.savefig('Praticando/PremierLeague/perfil_medio_por_Cluster.png')

posicoes_por_cluster = resposta_com_cluster.groupby('Cluster')['Position'].value_counts().unstack().fillna(0)
posicoes_por_cluster.T.plot(kind='bar', figsize=(12, 6))
plt.title('Distribuição de Posições por Cluster')
plt.xlabel('Posição')
plt.ylabel('Número de Jogadores')
plt.legend(title='Cluster')
plt.tight_layout()
plt.savefig('Praticando/PremierLeague/posicoes_por_cluster.png')