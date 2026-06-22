"""
Fila para guardar emprestimos e devolução
"""

from utils.fila import Fila
from utils.livro import Livro

class Node:
    def __init__(self, livro: "Livro"):
        self.livro = livro
        self.prox = None
        self.qtd = livro.qtd_ex
        self.fila = Fila() # fila

class Emprestimos:
    # farei uma lista encadeada de livros quando houver emprestimo
    def __init__(self):
        self.head = None

    def buscar(self, ISBN:str)-> Node | None:
        if self.head == None:
            return None
        atual = self.head
        while atual != None:
            if atual.livro.isbn == ISBN:
                return atual
            else:
                atual = atual.prox
        return None

    def emprestar(self, livro: "Livro", quem:str)->str:
        busca = self.buscar(livro.isbn)
        if busca == None:
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
            if busca.qtd > 0: # tem disponivel
                busca.qtd -= 1
                return "Emprestimo realizado"
            elif busca.qtd == 0: # vai para fila de espera
                busca.fila.enfileirar(quem) # adiciona no fim
                return "Emprestimo não realizado, usuario foi para fila de espera"

    def devolver(self, livro: "Livro", quem:str=None)->str:
        busca = self.buscar(livro.isbn)
        if busca == None:
            return "Não tem como devolver o que não foi emprestado"
        if not busca.fila.vazia():
            if quem != None:
                return busca.fila.remover(quem)
            return f"Fila andou, {busca.fila.desenfileirar()} foi o próximo" # fila anda mas quantidade não aumenta
        else:
            busca.qtd += 1 # fila esta vazia, quantidade aumenta
            if busca.qtd == busca.livro.qtd_ex:
                self.limpar_emprestimo(busca)
            return "Devolução realizada"

    def limpar_emprestimo(self, no:Node)->None:
        if self.head == None:
            return
        elif self.head == no:
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
