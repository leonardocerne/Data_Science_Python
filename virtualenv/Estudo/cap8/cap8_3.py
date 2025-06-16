class Quadrado():
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return (self.lado ** 2)

    def setLado(self, novo_lado):
        self.lado = novo_lado
    
    def getLado(self):
        return self.lado


quad = Quadrado(5)
print(f"Lado do quadrado: {quad.getLado()}")
print(f"Area do quadrado:{quad.area()}")
quad.setLado(10)
print(f"Area do quadrado:{quad.area()}")
