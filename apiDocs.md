# Objeto livro

Livro = {
    isbn:str,
    titulo:str,
    autor:str,
    ano_pub:int,
    qtd_ex:int
}

# Objeto emprestimo

Emprestimo = {
    isbn:str,
    quem:str
}

# Rotas

> "status" varia apenas entre "ok" e "not ok"

* "/" - GET: Serve apenas para teste de funcionamento
> Retorno: {"status": "ok", "message":"Funcionando"}

* "/api/cadastrar" - POST: Serve para cadastar novos livros
> body: json(Livro)
> Retorno: {"status": "?", "message":"?"}

* "/api/buscar/{isbn}" - GET: Serve para buscar um livro pelo ISBN
> Retorno: {"status": "ok", "message":"?", "data": Livro}
> Retorno: {"status": "not ok", "message":"?"}

* "/api/delete/{isbn}" - DELETE: Serve para deletar um livro pelo ISBN
> Retorno: {"status": "?", "message":"?"}

* "/api/listar" - GET: Serve para listar todos os livros em ordem alfabetica
> Retorno: {"status": "not ok", "message":"?"}
> Retorno: {"status": "ok", "message":"?", "data":[Livro]}

* "/api/emprestimo" - POST: Serve para fazer emprestimos
> body: json(Emprestimo)
> Retorno: {"status": "?", "message":"?"}

* "/api/devolver" - POST: Serve para devolver um livro
> body: json(Emprestimo)
> Retorno: {"status": "?", "message":"?"}

* "/api/desfazer" - GET: Serve para desfazer o ultimo emprestimo
> Retorno: {"status":"ok", "message":"Ação desfeita"}

* "/api/mock" - GET: Serve para mockar os dados em um CSV com 50 "livros"
> Retorno: {"status":"ok", "message":"Dados mockados"}

* "/api/relatorio" - GET: Serve para gerar um relatorio geral da biblioteca
> Retorno: {"status":"ok", "message":"Relatorio gerado", "data":[header, [dados_livro:str], rodape]}
