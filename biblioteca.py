"""
Funcionalidades:
    cadastrar livro - Ok
    remover livro
    buscar livro
    listar livros em ordem alfabetica
    realizar emprestimo
    realizar devolução
    inserir em lista de espera quando não houver exemplares disponiveis
    desfazer ultimos emprestimos
    gerar relatorio geral do acervo
"""

from utils import livro, livros_busca, livros_lista, org_livros, desfazer, emprestimo

# livro: classe livro
# livros_busca: tabela hash
# livros_lista: lista encadeada
# org_livros: arvore AVL
# desfazer: pilha
# emprestimo: fila

class Biblioteca:
    def __init__(self):
        self.tabela_hash = livros_busca.Tabela()
        self.lista_enc = livros_lista.Livros_enc()
        self.arvore = org_livros.Livros_arvore()
        self.historico = desfazer.Historico()
        self.emprestimos = emprestimo.Emprestimos()

    def cadastrar_livro(self, isbn:str, titulo:str, autor:str, ano_publicacao:int, qtd_exemplares:int):
        if isbn and titulo and autor and ano_publicacao and qtd_exemplares:
            livro = livro.Livro(isbn, titulo, autor, ano_publicacao, qtd_exemplares)
            self.tabela_hash.inserir(livro)
            self.lista_enc.cadastrar_livro(livro)
            self.arvore.inserir(livro)
        else:
            return "Informação faltando"
