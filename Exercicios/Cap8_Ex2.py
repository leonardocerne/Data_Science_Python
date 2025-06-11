class Pessoa:
    def __init__(self, nome, cidade, telefone, email):
        self.nome = nome 
        self.cidade = cidade
        self.telefone = telefone
        self.email = email
    
    def printa_pessoa(self):
        print(f"Pessoa de nome {self.nome} que mora em {self.cidade}, possui telefone {self.telefone} e email {self.email}")
    
    def altera_telefone(self, novotel):
        self.telefone = novotel
        print(f"Novo telefone = {novotel}")
    

pessoa1 = Pessoa("Leonardo", "Rio de Janeiro", "21988172804", "leobcerne@gmail.com")
pessoa1.printa_pessoa()
pessoa1.altera_telefone("21968834224")
pessoa1.printa_pessoa()