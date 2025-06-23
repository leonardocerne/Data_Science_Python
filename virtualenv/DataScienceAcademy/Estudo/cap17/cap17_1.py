import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def visualiza_imagens(images, labels):
    plt.figure(figsize= (10,10))
    for i in range(25):
        plt.subplot(5,5,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(images[i], cmap = plt.cm.binary)
        plt.xlabel(nomes_classes[labels[i][0]])
    plt.show()


# Carregando imagens do dataset Cifar-10
(imagens_treino, labels_treino), (imagens_teste, labels_teste) = datasets.cifar10.load_data()

# Classes das imagens
nomes_classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

# Normaliza os valores dos pixels para que os dados fiquem na mesma escala
imagens_treino = imagens_treino / 255.0
imagens_teste = imagens_teste / 255.0

visualiza_imagens(imagens_treino, labels_treino)

# Modelo

# Cria o objeto de sequência de camadas
modelo = models.Sequential()

# Adiciona o primeiro bloco de convulução e max pooling (camada de entrada)
modelo.add(layers.Conv2D(32, (3, 3), activation = 'relu', input_shape = (32, 32, 3)))
modelo.add(layers.MaxPooling2D((2, 2)))

# Adiciona o segundo bloco de convolução e max pooling (camada intermediária)
modelo.add(layers.Conv2D(64, (3, 3), activation = 'relu'))
modelo.add(layers.MaxPooling2D((2, 2)))

# Adiciona o terceiro bloco de convolução e max pooling (camada intermediária)
modelo.add(layers.Conv2D(64, (3, 3), activation = 'relu'))
modelo.add(layers.MaxPooling2D((2, 2)))

# Adicionar camadas de classificação
modelo.add(layers.Flatten())
modelo.add(layers.Dense(64, activation = 'relu'))
modelo.add(layers.Dense(10, activation = 'softmax'))

# Sumário do modelo
modelo.summary()

# Compilação do modelo
modelo.compile(optimizer = 'adam',
               loss = 'sparse_categorical_crossentropy',
               metrics = ['accuracy'])

history = modelo.fit(imagens_treino, 
                         labels_treino, 
                         epochs = 10, 
                         validation_data = (imagens_teste, labels_teste))

# Avalia o modelo
erro_teste, acc_teste = modelo.evaluate(imagens_teste, labels_teste, verbose = 2)

print('\nAcurácia com Dados de Teste:', acc_teste)

# Carrega uma nova imagem
nova_imagem = Image.open("dados/nova_imagem.jpg")

# Obtém largura e altura da imagem
largura = nova_imagem.width
altura = nova_imagem.height

# Redimensiona para 32x32 pixels
nova_imagem = nova_imagem.resize((32, 32))

# Exibir a imagem
plt.figure(figsize = (1,1))
plt.imshow(nova_imagem)
plt.xticks([])
plt.yticks([])
plt.show()

# Converte a imagem para um array NumPy e normaliza
nova_imagem_array = np.array(nova_imagem) / 255.0

# Expande a dimensão do array para que ele tenha o formato (1, 32, 32, 3)
nova_imagem_array = np.expand_dims(nova_imagem_array, axis = 0) 

# Previsões
previsoes = modelo.predict(nova_imagem_array)

# Obtém a classe com maior probabilidade e o nome da classe
classe_prevista = np.argmax(previsoes)
nome_classe_prevista = nomes_classes[classe_prevista]

print("A nova imagem foi classificada como:", nome_classe_prevista)