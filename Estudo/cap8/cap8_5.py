class Imovel():
    def __init__(self, preco, rua, numero):
        self.preco = preco
        self.rua = rua
        self.numero = numero

    def resumo(self):
        pass


class Predio(Imovel):
    def __init__(self, preco, rua, numero, num_apts):
        super().__init__(preco, rua, numero)
        self.num_apts = num_apts

    def resumo(self):
        print(f"O predio na rua {self.rua} e numero {self.numero} esta avaliado em {self.preco} reais e tem {self.num_apts} apts.")

    
class Casa(Imovel):
    def resumo(self):
        print(f"A casa na rua {self.rua} e numero {self.numero} esta avaliada em {self.preco} reais")
    
    def tocar_campainha(self):
        print("Blong blong")
    

class Apartamento(Imovel):
    def __init__(self, preco, rua, numero, num_apt):
        super().__init__(preco, rua, numero)
        self.num_apt = num_apt
    
    def resumo(self):
        print(f"O apartamento localizada no predio na rua {self.rua}, numero {self.numero}, e numero de apartamento {self.num_apt} esta avaliado em {self.preco} reais.")

    

casa1 = Casa(100000, "Rua Mata Grande", 163)
predio1 = Predio(10000000, "Rua General Osório", 45, 45)
apt1 = Apartamento(300000, "Rua General Osório", 45, 217)

lista = [casa1, predio1, apt1]

for imovel in lista:
    imovel.resumo()
    if isinstance(imovel, Casa):
        imovel.tocar_campainha()
    
    print("_________")
