"""
Arvore AVL para buscar livros e fazer amostragem em ordem alfabetica
"""

from livro import Livro

class Node:
    def __init__(self, livro:Livro):
        self.livro = livro
        self.esq = None
        self.dir = None
        self.altura = 1


class Livros_arvore:
    def __init__(self):
        self.raiz = None

    def altura(self, no):
        if no is None:
            return 0
        return no.altura

    def atualizar_altura(self, no):
        no.altura = 1 + max(
            self.altura(no.esq),
            self.altura(no.dir)
        )

    def fator_balanceamento(self, no):
        if no is None:
            return 0
        return ( self.altura(no.esq) - self.altura(no.dir) )

    def rotacao_direita(self, y):
        x = y.esq
        t2 = x.dir

        x.dir = y
        y.esq = t2

        self.atualizar_altura(y)
        self.atualizar_altura(x)

        return x

    def rotacao_esquerda(self, x):
        y = x.dir
        t2 = y.esq

        y.esq = x
        x.dir = t2

        self.atualizar_altura(x)
        self.atualizar_altura(y)

        return y

    def inserir(self, livro):
        self.raiz = self._inserir(self.raiz, livro)

    def _inserir(self, no, livro):
        if no is None:
            return Node(livro)

        if livro.titulo.lower() < no.livro.titulo.lower():
            no.esq = self._inserir(no.esq, livro)

        else:
            no.dir = self._inserir(no.dir, livro)

        self.atualizar_altura(no)

        balanceamento = self.fator_balanceamento(no)

        # EE
        if (
            balanceamento > 1 and
            livro.titulo.lower() <
            no.esq.livro.titulo.lower()
        ):
            return self.rotacao_direita(no)

        # DD
        if (
            balanceamento < -1 and
            livro.titulo.lower() >
            no.dir.livro.titulo.lower()
        ):
            return self.rotacao_esquerda(no)

        # ED
        if (
            balanceamento > 1 and
            livro.titulo.lower() >
            no.esq.livro.titulo.lower()
        ):
            no.esq = self.rotacao_esquerda(no.esq)
            return self.rotacao_direita(no)

        # DE
        if (
            balanceamento < -1 and
            livro.titulo.lower() <
            no.dir.livro.titulo.lower()
        ):
            no.dir = self.rotacao_direita(no.dir)
            return self.rotacao_esquerda(no)

        return no

    def buscar_titulo(self, titulo):
        return self._buscar_titulo(
            self.raiz,
            titulo.lower()
        )

    def _buscar_titulo(self, no, titulo):

        if no is None:
            return None

        atual = no.livro.titulo.lower()

        if titulo == atual:
            return no.livro

        if titulo < atual:
            return self._buscar_titulo(
                no.esq,
                titulo
            )

        return self._buscar_titulo(
            no.dir,
            titulo
        )

    def listar_alfabetico(self):
        self._em_ordem(self.raiz)

    def _em_ordem(self, no):
    # se for necessario usar em outro lugar, acho valido criar um array e para cada livro, faz o append
        if no is not None:
            self._em_ordem(no.esq)
            print(no.livro.titulo)
            self._em_ordem(no.dir)

    def remover(self, titulo):
        self.raiz = self._remover(
            self.raiz,
            titulo.lower()
        )

    def _remover(self, no, titulo):

        if no is None:
            return None

        atual = no.livro.titulo.lower()

        if titulo < atual:

            no.esq = self._remover(
                no.esq,
                titulo
            )

        elif titulo > atual:

            no.dir = self._remover(
                no.dir,
                titulo
            )

        else:

            # 0 ou 1 filho

            if no.esq is None:
                return no.dir

            if no.dir is None:
                return no.esq

            # 2 filhos

            sucessor = self._menor(no.dir)

            no.livro = sucessor.livro

            no.dir = self._remover(
                no.dir,
                sucessor.livro.titulo.lower()
            )

        if no is None:
            return None

        self.atualizar_altura(no)

        balanceamento = self.fator_balanceamento(no)

        # EE

        if (
            balanceamento > 1 and
            self.fator_balanceamento(no.esq) >= 0
        ):
            return self.rotacao_direita(no)

        # ED

        if (
            balanceamento > 1 and
            self.fator_balanceamento(no.esq) < 0
        ):
            no.esq = self.rotacao_esquerda(no.esq)
            return self.rotacao_direita(no)

        # DD

        if (
            balanceamento < -1 and
            self.fator_balanceamento(no.dir) <= 0
        ):
            return self.rotacao_esquerda(no)

        # DE

        if (
            balanceamento < -1 and
            self.fator_balanceamento(no.dir) > 0
        ):
            no.dir = self.rotacao_direita(no.dir)
            return self.rotacao_esquerda(no)

        return no

    def _menor(self, no):

        atual = no

        while atual.esq is not None:
            atual = atual.esq

        return atual

if __name__ == "__main__":
    arv = Livros_arvore()
    livro1 = Livro("295221423-9", "Faces of Death 5", "jorge", 2011, 9)
    livro2 = Livro("114893376-X", "Datetown", "mininu", 2005, 3)
    livro3 = Livro("295221423-9", "The crazy", "Thiago", 2010, 8)
    arv.inserir(livro1)
    arv.listar_alfabetico()
    print()
    arv.inserir(livro2)
    arv.listar_alfabetico()
    print()
    arv.inserir(livro3)
    arv.listar_alfabetico()
    print()
    arv.remover(livro1.titulo)
    arv.listar_alfabetico()
