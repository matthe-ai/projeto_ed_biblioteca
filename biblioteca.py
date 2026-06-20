"""
Funcionalidades:
    cadastrar livro - Ok
    remover livro - Ok
    buscar livro
    listar livros em ordem alfabetica
    realizar emprestimo
    realizar devolução
    inserir em lista de espera quando não houver exemplares disponiveis
    desfazer ultimos emprestimos
    gerar relatorio geral do acervo
"""

from utils import livro as lvr, livros_busca, livros_lista, org_livros, desfazer, emprestimos

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
        self.emprestimos = emprestimos.Emprestimos()

    def cadastrar_livro(self, isbn:str, titulo:str, autor:str, ano_publicacao:int, qtd_exemplares:int):
        if isbn and titulo and autor and ano_publicacao and qtd_exemplares:
            livro = lvr.Livro(isbn, titulo, autor, ano_publicacao, qtd_exemplares)
            self.tabela_hash.inserir(livro)
            self.lista_enc.cadastrar_livro(livro)
            self.arvore.inserir(livro)
            return "Cadastrado"
        else:
            return "Informação faltando"

    def remover_livro(self, isbn:str):
        if isbn:
            livro = self.tabela_hash.buscar(isbn)
            if livro == None:
                return "ISBN não encontrado"
            titulo = livro.titulo
            self.tabela_hash.remover(isbn)
            self.lista_enc.remover_livro(isbn)
            self.arvore.remover(titulo)
            self.emprestimos.limpar_emprestimo(self.emprestimos.buscar(isbn))
            print(f"{titulo} foi removido")
        else:
            return "Informação faltando"

if __name__ == "__main__":
    lib = Biblioteca()
    lib.cadastrar_livro("1234-02-453-8", "testou", "testador", 2026, 1)
    lib.cadastrar_livro("8723-90-709-1", "garotando", "menino", 2004, 3)
    lib.remover_livro("0")
    lib.remover_livro("1234-02-453-8")
