"""
Modulo principal
Metodos:
    cadastrar_livro(isbn, titulo, autor, ano_publicacao, qtd_exemplares)->str
    remover_livro(isbn)->None|str
    buscar_livro(isbn)->Livro|str
    listar_livros()->None|[Livro]
    emprestar_livro(isbn, quem)->None|str
    devolver_livro(isbn, quem)->str
    desfazer_emprestimo()->None
    mostrar_relatorio()->str
"""

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from biblioteca import Biblioteca

# Definição dos CORS

origins = [
        "http://localhost:5173"
]

# Instancia da biblioteca

lib = Biblioteca()

# Definição de body da API

class Livro_dados(BaseModel):
    isbn: str
    titulo: str
    autor: str
    ano_pub: int
    qtd_ex: int

class Emprestimo(BaseModel):
    isbn:str
    quem:str

# CONFIG

class Config:
    def __init__(self):
        self.MOCKADO = False

config = Config()

# Instancia do app

app = FastAPI()

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

# Definição de rotas

@app.get("/")
def root():
    return {"status": "ok", "message":"Funcionando"}

@app.post("/api/cadastrar")
def cadastrar(dados: Livro_dados):
    response:str = lib.cadastrar_livro(dados.isbn, dados.titulo, dados.autor, dados.ano_pub, dados.qtd_ex)
    if response.lower() == "cadastrado":
        return {"status": "ok", "message":"Livro cadastrado com sucesso"}
    else:
        return {"status": "not ok", "message":"Livro não cadastrado, deve estar faltando informação"}

@app.get("/api/buscar/{isbn}")
def buscar(isbn:str):
    response:Livro_dados|None|str = lib.buscar_livro(isbn)
    if type(response) != str:
        if response == None or type(response) == str:
            return {"status": "not ok", "message":"Livro não encontrado ou não existe"}
        else:
            response = jsonable_encoder(response.__dict__)
            return {"status": "ok", "message":"Livro encontrado", "data":response}

@app.delete("/api/delete/{isbn}")
def deletar(isbn:str):
    response:str = lib.remover_livro(isbn)
    return {"status": "ok", "message": response}

@app.get("/api/listar")
def listar():
    response:[Livro_dados]|None = lib.listar_livros(False)
    if response == None:
        return {"status": "not ok", "message":"Nenhum livro para listar"}
    dados = []
    for livro in response:
        dados.append(jsonable_encoder(livro.__dict__))
    return {"status":"ok", "message":"Livros encontrados","data":dados}

@app.post("/api/emprestimo")
def emprestar(dados: Emprestimo):
    response:str = lib.emprestar_livro(dados.isbn, dados.quem)
    return {"status":"ok", "message":response}

@app.post("/api/devolver")
def devolver(dados: Emprestimo):
    response:str = lib.devolver_livro(dados.isbn, dados.quem)
    return {"status":"ok", "message":response}

@app.get("/api/desfazer")
def desfazer():
    lib.desfazer_emprestimo()
    return {"status":"ok", "message":"Ação desfeita"}

@app.get("/api/relatorio")
def relatorio():
    response:str = lib.mostrar_relatorio()
    return {"status":"ok", "message":"Relatorio gerado", "data":response}

@app.get("/api/mock")
def mock_dados():
    if config.MOCKADO == True:
        return {"status":"ok", "message":"Dados já foram mockados"}
    import csv
    caminho = "mockdata/livros.csv"
    with open(caminho, "r", encoding='utf-8') as file:
        csv_read = csv.reader(file)
        next(csv_read) # pula o header
        for linha in csv_read:
            lib.cadastrar_livro(linha[0],linha[1],linha[2],int(linha[3]),int(linha[4]))
    config.MOCKADO = True
    return {"status":"ok", "message":"Dados mockados"}
