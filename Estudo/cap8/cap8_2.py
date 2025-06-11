class Livro():
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        print("Construtor chamado para criar um objeto desta classe.")
    
    def imprime(self):
        print(f"Foi criado o livro {self.titulo} com ISBN {self.isbn}")
    
titulo = input("Digite o titulo do livro")
isbn = int(input("Digite o isbn do livro"))    
livro1 = Livro(titulo, isbn)
livro1.imprime()
print(hasattr(livro1, "titulo"))
setattr(livro1, "isbn", 111)
livro1.imprime()
print(getattr(livro1, "isbn"))
delattr(livro1, "titulo")
print(hasattr(livro1, "titulo"))
