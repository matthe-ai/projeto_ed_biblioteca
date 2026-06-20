"""
Funcionalidades:
    cadastrar livro - Ok
    remover livro - Ok
    buscar livro - Ok
    listar livros em ordem alfabetica - Ok
    realizar emprestimo - Ok
    realizar devolução - Ok
    inserir em lista de espera quando não houver exemplares disponiveis - Ok
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

    def buscar_livro(self, isbn:str):
        if isbn:
            return self.tabela_hash.buscar(isbn)
        else:
            return "Informação faltando"
    
    def listar_livros(self):
        """
        Lista em ordem alfabetica
        """
        self.arvore.listar_alfabetico()
        return None

    def emprestar_livro(self, livro: "Livro", quem: str):
        """
        Recebe o objeto do livro a ser emprestado e o nome de quem tá pegando emprestado
        """
        if livro and quem:
            self.emprestimos.emprestar(livro, quem)
            self.historico.push((livro,quem))
        else:
            return "Informação faltando"

    def devolver_livro(self, livro: "Livro", quem: str = None):
        """
        Recebe o objeto do livro emprestado e devolve
        """
        if livro:
            self.emprestimos.devolver(livro, quem)
        else:
            return "Informação faltando"
    
    def desfazer_emprestimo(self):
        livro, quem = self.historico.topo_pilha()
        self.devolver_livro(livro, quem)
        return None

if __name__ == "__main__":
    lib = Biblioteca()
    lib.cadastrar_livro("1234-02-453-8", "testou", "testador", 2026, 1)
    lib.cadastrar_livro("8723-90-709-1", "garotando", "menino", 2004, 3)
    lib.remover_livro("0")
    lib.remover_livro("1234-02-453-8")
