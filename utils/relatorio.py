"""
Geração de relatorio
"""

from utils.livro import Livro


def gerar_relatorio(dados:[[Livro,int,int]]): #primeiro int é a quantidade disponivel no momento, segundo é o tamanho da fila
        base = """
    =========================
    RELATORIO GERAL DO ACERVO
    =========================
        """
        livros = []
        for i in range(len(dados)):
            livro, qtd_disp, taman_fila = dados[i]
            livro_info = f"""\n
        [{i+1}] Título: {livro.titulo}
            Autor: {livro.autor} | Ano: {livro.ano_pub}
            ISBN: {livro.isbn}
            Exemplares: {qtd_disp} disponíveis / {livro.qtd_ex} total
            """
            if taman_fila > 0:
                livro_info += f"({taman_fila} usuários na fila de espera)"
            
            livros.append(livro_info)

        rodape = f"""\n
    =========================
    TOTAL DE LIVROS: {len(dados)}
    =========================
        """

        return [base,livros,rodape]


if __name__ == "__main__":
    livro1 = Livro("3143-543543-64-2", "culpa sua", "mago", 2001, 2)
    print(gerar_relatorio([[livro1, 1, 0],[livro1, 0, 1]]))
