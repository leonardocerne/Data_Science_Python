class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def imprimir(self):
        print(f"Ola meu nome é {self.nome} e tenho {self.idade} anos")
    
    def me_apresentar(self):
        pass


class Gerente(Pessoa):
    
    def __init__(self, nome, idade, salario):
        Pessoa.__init__(self, nome, idade)
        self.salario = salario

    def me_apresentar(self):
        super().imprimir()
        print(f"E meu salario é {self.salario}")
    

class Funcionario(Pessoa):

    def __init__(self, nome, idade, carga):
        Pessoa.__init__(self, nome, idade)
        self.carga = carga
    
    def me_apresentar(self):
        super().imprimir()
        print(f"E eu trabalho {self.carga} horas por dia")
    

x = Gerente("Leonardo", 20, 2000)
y = Funcionario("Victor", 21, 8)
x.me_apresentar()
y.me_apresentar()