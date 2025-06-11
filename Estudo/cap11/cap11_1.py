import matplotlib.pyplot as plt

x = [2,3,5]
y = [3,5,7]
plt.plot(x,y, label = 'Gráfico com Matplotlib')
plt.xlabel('Variável 1')
plt.ylabel('Variável 2')
plt.title('Teste Plot')
plt.legend()
plt.show()

x1 = [2,4,6,8,10]
y1 = [6,7,8,2,4]
plt.bar(x1,y1, label = 'Barras', color = 'green')
plt.legend()
plt.show()

x2 = [1,3,5,7,9]
y2 = [7,8,2,4,2]
plt.bar(x1,y1, label = 'Listas1', color = 'blue')
plt.bar(x2,y2, label = 'Listas2', color = 'red')
plt.legend()
plt.show()

x3 = [1,2,3,4,5,6,7,8]
y3 = [5,2,4,5,6,8,4,8]
plt.scatter(x3, y3, label = 'Pontos', color = 'r', marker = '*')
plt.legend()
plt.show()

dias = [1,2,3,4,5]
dormir = [7,8,6,77,7]
comer = [2,3,4,5,3]
trabalhar = [7,8,7,2,2]
passear = [8,5,7,8,13]
plt.stackplot(dias, dormir, comer, trabalhar, passear, colors = ['m','c','r','k','b'])
plt.show()

fatias = [7, 2, 2, 13]
atividades = ['dormir', 'comer', 'passear', 'trabalhar']
cores = ['olive', 'lime', 'violet', 'royalblue']
plt.pie(fatias, labels = atividades, colors = cores, startangle = 90, shadow = True, explode = (0,0.2,0,0))
plt.show()