"""
Tabela hash para busca de livros por ISBN
"""

class Tabela:
    def __init__(self, tamanho = 10):
        self.tamanho = tamanho
        self.tabela = [[] for c in range(tamanho)]

    def __hash_func(self, isbn:str)->int:
        chave = 0
        for i in isbn: # isbn é uma string do formato "000-00-000-0000-0" pela existencia dos hifens tem que tratar com o for
            if i.isdecimal():
                chave += int(i)
        return chave % self.tamanho


    def inserir(self, livro):
        indice = self.__hash_func(livro.isbn)

        for item in self.tabela[indice]:
            if item.isbn == livro.isbn:
                return "Livro ja cadastrado."
                 
        self.tabela[indice].append(livro)

    def buscar(self, isbn):
        indice = self.__hash_func(isbn)

        for livro in self.tabela[indice]:
            if livro.isbn == isbn:
                return livro

        return None

    def remover(self, isbn):
        indice = self.__hash_func(isbn)

        for livro in self.tabela[indice]:
            if livro.isbn == isbn:
                self.tabela[indice].remove(livro)
                return True

        return False

    def listar(self):
        for lista in self.tabela:
            for livro in lista:
                print(livro.titulo)

if __name__ == "__main__":
    hs = Tabela()
    livro = Livro("123-04-321-7689-2", "Jorge", "Alex", 1976, 2)
    hs.inserir(livro)
    hs.listar()
    hs.remover("123-04-321-7689-2")
    hs.listar()
