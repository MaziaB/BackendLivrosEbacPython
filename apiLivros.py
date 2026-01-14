# API de Livros

# POST - Adicionar novos livros (Creat)
# GET - Buscar os dados dos livros (Read)
# PUT - Atualizar informações dos livros (Update)
# DELETE - Deletar informações dos livros (Delete)

# vamos acessar nosso endpoint e os PATHs desse endpoint
# GET:
# http://127.0.0.1:8000/livros
# Endpoint(http://127.0.0.1:8000) path(/livros)

# POST:
# http://127.0.0.1:8000/adiciona?id_livro=1&nome_livro=Harry%20Potter&autor_livro=J.K&ano_livro=2005
# Query Strings ('?' para adicionar informações à URL), tudo depois do '?' é 'query string'

from fastapi import FastAPI, HTTPException # HTTPException - para tratamento de erros

app = FastAPI()

livros = {} # Para armazenamento e manipulação de dados; banco de dados improvisado.

@app.get("/livros") # rota/path - /livros
def get_livros():
    if not livros:
        return {"mensagem": "Não existe nenhum livro!"} # JSON
    else:
        return {"Livros": livros}
    

@app.post("/adiciona")
def post_livros(id_livro: int, nome_livro: str, autor_livro: str, ano_livro: int):
    if id_livro in livros:
        raise HTTPException (status_code=400, detail="Este livro já existe!")
    else:
        livros[id_livro] = {"nome_livro": nome_livro, "autor_livro": autor_livro, "ano_livro": ano_livro}
        return{"mensagem": "Livro criado com sucesso!"}
    

@app.put("/atualiza/{id_livro}")
def put_livros(id_livro: int, nome_livro: str, autor_livro: str, ano_livro: str):
    meu_livro = livros.get(id_livro)
    if not meu_livro:
        raise HTTPException(status_code=404, detail="Esse livro não foi encontrado!")
    else:
        if nome_livro: # validação
            meu_livro["nome_livro"] = nome_livro # atualização
        if autor_livro:
            meu_livro["autor_livro"] = autor_livro
        if ano_livro:
            meu_livro["ano_livro"] = ano_livro

        return {"mensagem": "As informações do seu livro foram atualizadas com sucesso!"}
    

@app.delete("/deletar/{id_livro}")
def delete_livro(id_livro: int):
    if id_livro not in livros:
        raise HTTPException(status_code=404, detail="Esse livro não foi encontrado!")
    else:
        del livros[id_livro]

        return{"mensagem": "Seu livro foi deletado com sucesso!"}
