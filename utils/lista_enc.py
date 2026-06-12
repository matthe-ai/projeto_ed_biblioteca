"""
Lista dinamica para guardar os livros
"""

from livro import Livro

class Node:
    def __init__(self, dado:Livro):
        self.prox = None
        self.dado = dado

class Lista:
    def __init__(self):
        self.head = None

    def cadastrar_livro(self, livro:Livro):
        """
        Insere um livro sempre no fim da lista
        """
        if self.head == None:
            self.head = Node(livro)
        else:
            atual = self.head
            while atual.prox != None:
                atual = atual.prox
            atual.prox = Node(livro)

    def remover_livro(self, isbn:str):
        """
        Remove livro pelo ISBN
        """
        if self.head == None:
            print("Nenhum livro cadastrado")
        else:
            if self.head.dado.isbn == isbn:
                self.head = self.head.prox
            else:
                atual = self.head
                while atual != None:
                    if atual.prox.dado.isbn == isbn: #achou o livro a ser removido
                        atual.prox = atual.prox.prox
                    else:
                        atual = atual.prox

