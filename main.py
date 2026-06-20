"""
Modulo principal
Metodos:
    cadastrar_livro(isbn, titulo, autor, ano_publicacao, qtd_exemplares)->str
    remover_livro(isbn)->None|str
    buscar_livro(isbn)->Livro
    listar_livros()->None
    emprestar_livro(isbn, quem)->None|str
    devolver_livro(isbn, quem)->str
    desfazer_emprestimo()->None
    mostrar_relatorio()->str
"""

from biblioteca import Biblioteca

def mock_dados(lib:Biblioteca):
    import csv
    caminho = "mockdata/livros.csv"
    with open(caminho, "r", encoding='utf-8') as file:
        csv_read = csv.reader(file)
        next(csv_read) # pula o header
        for linha in csv_read:
            lib.cadastrar_livro(linha[0],linha[1],linha[2],int(linha[3]),int(linha[4]))

if __name__ == "__main__":
    lib = Biblioteca()
    if int(input("Deseja iniciar com dados mockados?\n [1] Sim \n [2] Não \nR: ")) == 1:
        mock_dados(lib)
    lib.listar_livros()
