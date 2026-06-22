"""
Geração de relatorio
"""

from utils.livro import Livro

class Livro_rel(Livro):
    def __init__(self, livro:Livro, qtd_disp:int, tamanho_fila:int):
        self.__dict__.update(livro.__dict__)
        self.qtd_disp = qtd_disp
        self.tam_fila = tamanho_fila


def gerar_relatorio(dados:[[Livro,int,int]]): #primeiro int é a quantidade disponivel no momento, segundo é o tamanho da fila
        livros = []
        for i in range(len(dados)):
            livro, qtd_disp, taman_fila = dados[i]
            lvr = Livro_rel(livro, qtd_disp, taman_fila)
            livros.append(lvr)
        return [livros]

if __name__ == "__main__":
    livro1 = Livro("3143-543543-64-2", "culpa sua", "mago", 2001, 2)
    print(gerar_relatorio([[livro1, 1, 0],[livro1, 0, 1]]))
