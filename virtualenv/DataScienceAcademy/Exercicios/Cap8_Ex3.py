class Smartphone:
    def __init__(self, tamanho, interface):
        self.tamanho = tamanho
        self.interface = interface

    def x(self):
        pass
    

class MP3Player(Smartphone):
    def __init__(self, tamanho, interface, capacidade):
        super().__init__(tamanho, interface)
        self.capacidade = capacidade
    
    def x(self):
        print("Blablabla")



mp3 = MP3Player(20, "IOS", 256)
mp3.x()