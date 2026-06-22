# API de Biblioteca

API para gerenciamento de livros, empréstimos e geração de relatórios.

---

# Objetos

## Livro

Representa um livro cadastrado na biblioteca.

### Estrutura

```json
{
  "isbn": "9788575226155",
  "titulo": "Clean Code",
  "autor": "Robert C. Martin",
  "ano_pub": 2008,
  "qtd_ex": 5
}
```

| Campo   | Tipo    | Descrição                            |
| ------- | ------- | ------------------------------------ |
| isbn    | string  | ISBN único do livro                  |
| titulo  | string  | Título do livro                      |
| autor   | string  | Nome do autor                        |
| ano_pub | integer | Ano de publicação                    |
| qtd_ex  | integer | Quantidade de exemplares disponíveis |

---

## Empréstimo

Representa uma operação de empréstimo ou devolução.

### Estrutura

```json
{
  "isbn": "9788575226155",
  "quem": "João Silva"
}
```

| Campo | Tipo   | Descrição                                  |
| ----- | ------ | ------------------------------------------ |
| isbn  | string | ISBN do livro                              |
| quem  | string | Nome da pessoa responsável pelo empréstimo |

## Livro_rel

Representa um livro vindo do relatorio

### Estrutura

```json
{
  "isbn": "9788575226155",
  "titulo": "Clean Code",
  "autor": "Robert C. Martin",
  "ano_pub": 2008,
  "qtd_ex": 5,
  "qtd_disp": 2,
  "tam_fila": 0
}
```

| Campo   | Tipo    | Descrição                            |
| ------- | ------- | ------------------------------------ |
| isbn    | string  | ISBN único do livro                  |
| titulo  | string  | Título do livro                      |
| autor   | string  | Nome do autor                        |
| ano_pub | integer | Ano de publicação                    |
| qtd_ex  | integer | Quantidade de exemplares             |
| qtd_disp | integer | Quantidade de exemplares disponiveis |
| tam_fila | integer | Tamanho da fila                     |

---

# Padrão de Resposta

Todas as rotas retornam um objeto contendo:

```json
{
  "status": "ok",
  "message": "Operação realizada com sucesso"
}
```

## Campos

| Campo   | Tipo   | Descrição                                         |
| ------- | ------ | ------------------------------------------------- |
| status  | string | `ok` ou `not ok`                                  |
| message | string | Mensagem descritiva da operação                   |
| data    | any    | Dados retornados pela operação (quando aplicável) |

---

# Endpoints

## GET /

Verifica se a API está em funcionamento.

### Resposta

```json
{
  "status": "ok",
  "message": "Funcionando"
}
```

---

## POST /api/cadastrar

Cadastra um novo livro.

### Body

```json
{
  "isbn": "9788575226155",
  "titulo": "Clean Code",
  "autor": "Robert C. Martin",
  "ano_pub": 2008,
  "qtd_ex": 5
}
```

### Resposta

```json
{
  "status": "ok",
  "message": "Livro cadastrado com sucesso"
}
```

---

## GET /api/buscar/{isbn}

Busca um livro pelo ISBN.

### Parâmetros

| Nome | Tipo   | Descrição     |
| ---- | ------ | ------------- |
| isbn | string | ISBN do livro |

### Sucesso

```json
{
  "status": "ok",
  "message": "Livro encontrado",
  "data": {
    "isbn": "9788575226155",
    "titulo": "Clean Code",
    "autor": "Robert C. Martin",
    "ano_pub": 2008,
    "qtd_ex": 5
  }
}
```

### Falha

```json
{
  "status": "not ok",
  "message": "Livro não encontrado"
}
```

---

## DELETE /api/delete/{isbn}

Remove um livro pelo ISBN.

### Parâmetros

| Nome | Tipo   | Descrição     |
| ---- | ------ | ------------- |
| isbn | string | ISBN do livro |

### Resposta

```json
{
  "status": "ok",
  "message": "Livro removido com sucesso"
}
```

---

## GET /api/listar

Lista todos os livros cadastrados em ordem alfabética de título.

### Sucesso

```json
{
  "status": "ok",
  "message": "Livros listados com sucesso",
  "data": [
    {
      "isbn": "9788575226155",
      "titulo": "Clean Code",
      "autor": "Robert C. Martin",
      "ano_pub": 2008,
      "qtd_ex": 5
    }
  ]
}
```

### Falha

```json
{
  "status": "not ok",
  "message": "Nenhum livro cadastrado"
}
```

---

## POST /api/emprestimo

Realiza o empréstimo de um livro.

### Body

```json
{
  "isbn": "9788575226155",
  "quem": "João Silva"
}
```

### Resposta

```json
{
  "status": "ok",
  "message": "Empréstimo realizado com sucesso"
}
```

---

## POST /api/devolver

Registra a devolução de um livro.

### Body

```json
{
  "isbn": "9788575226155",
  "quem": "João Silva"
}
```

### Resposta

```json
{
  "status": "ok",
  "message": "Livro devolvido com sucesso"
}
```

---

## GET /api/desfazer

Desfaz o último empréstimo realizado.

### Resposta

```json
{
  "status": "ok",
  "message": "Ação desfeita"
}
```

---

## GET /api/mock

Gera uma base de dados de teste contendo 50 livros fictícios.

### Resposta

```json
{
  "status": "ok",
  "message": "Dados mockados"
}
```

---

## GET /api/relatorio

Gera um relatório geral da biblioteca.

### Resposta

```json
{
  "status": "ok",
  "message": "Relatório gerado",
  "data": [
        {
        "isbn": "9781328869333",
        "titulo": "1984",
        "autor": "George Orwell",
        "ano_pub": 2017,
        "qtd_ex": 7,
        "qtd_disp": 7,
        "tam_fila": 0
        }
    ]
}
```
