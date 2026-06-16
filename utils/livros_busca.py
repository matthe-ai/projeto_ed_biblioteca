"""
Tabela hash para busca de livros por ISBN
"""

class Tabela:
    def __init__(self, tamanho = 10):
        self.tamanho = tamanho
        self.tabela = [[] for c in range(tamanho)]

    def _hash_func(self, chave):
        return chave % self.tamanho


    def inserir(self, livro):
        indice = self._hash_func(livro.isbn)

        for item in self.tabela[indice]:
            if item.isbn == livro.isbn:
                return "Livro ja cadastrado."
                 
        self.tabela[indice].append(livro)

    def buscar(self, isbn):
        indice = self._hash_func(isbn)

        for livro in self.tabela[indice]:
            if livro.isbn == isbn:
                return livro

        return None

    def remover(self, isbn):
        indice = self._hash_func(isbn)

        for livro in self.tabela[indice]:
            if livro.isbn == isbn:
                self.tabela[indice].remove(livro)
                return True

        return False

    def listar(self):
        for lista in self.tabela:
            for livro in lista:
                print(livro)