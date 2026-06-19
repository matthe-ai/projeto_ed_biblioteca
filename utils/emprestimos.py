"""
Fila para guardar emprestimos e devolução
"""

from livro import Livro
from fila import Fila

class Node:
    def __init__(self, livro:Livro):
        self.livro = livro
        self.prox = None
        self.qtd = livro.qtd_ex
        self.fila = Fila() # fila

class Emprestimos:
    # farei uma lista encadeada de livros quando houver emprestimo
    def __init__(self):
        self.head = None

    def __existe(self,ISBN:str)->bool:
        if self.head == None:
            return False
        atual = self.head
        while atual != None:
            if atual.livro.isbn == ISBN:
                return True
            else:
                atual = atual.prox
        return False

    def emprestar(self, livro:Livro, quem:str)->str:
        if not self.__existe(livro.isbn):
            # Não existe e o head está vazio
            if self.head == None:
                self.head = Node(livro)
                self.head.qtd -= 1
                return "Emprestimo realizado"
            # procura um espaço vazio
            atual = self.head
            while atual != None:
                if atual.prox == None: # achou espaço vazio
                    atual.prox = Node(livro)
                    atual.prox.qtd -= 1
                else:
                    atual = atual.prox
            return "Emprestimo realizado"
        else: # livro já foi emprestado alguma vez
            atual = self.head
            while atual.livro.isbn != livro.isbn:
                atual = atual.prox
            # aqui está no Node do livro após passar pelo while
            if atual.qtd > 0: # tem disponivel
                atual.qtd -= 1
                return "Emprestimo realizado"
            elif atual.qtd == 0: # vai para fila de espera
                atual.fila.enfileirar(quem) # adiciona no fim
                return "Emprestimo não realizado, usuario foi para fila de espera"

    def devolver(self, livro:Livro)->str:
        if not self.__existe(livro.isbn):
            return "Não tem como devolver o que não foi emprestado"
        atual = self.head
        while atual.livro.isbn != livro.isbn:
            atual = atual.prox
        # achou o livro
        if not atual.fila.vazia():
            return f"Fila andou, {atual.fila.desenfileirar()} foi o próximo" # fila anda mas quantidade não aumenta
        else:
            atual.qtd += 1 # fila esta vazia, quantidade aumenta
            if atual.qtd == atual.livro.qtd_ex:
                self.__limpar_emprestimo(atual)
            return "Devolução realizada"

    def __limpar_emprestimo(self, no:Node)->None:
        if self.head == no:
            self.head = self.head.prox
        else:
            atual = self.head
            while atual.prox != no:
                atual = atual.prox
            atual.prox = atual.prox.prox

if __name__ == "__main__":
    ls = Emprestimos()
    livro1 = Livro("123-321-05-1232-9", "mininu", "jorge", 2021, 4)
    for i in range(5):
        ls.emprestar(livro1,f"pessoa{i}")
    print(ls.devolver(livro1))
