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

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import Optional
import secrets
import os

app = FastAPI(
    title="API de livros",
    description="API para gerenciar catálogo de livros",
    version="1.0.0",
    contact={
        "Nome": "Bruno Moraes",
        "e-mail": "bruno@email.com"
    }
)

MEU_USUARIO = "admin"
MINHA_SENHA = "admin"

security = HTTPBasic()

livros = {} # Para armazenamento e manipulação de dados; banco de dados improvisado.

class Livro(BaseModel):
    nome_livro: str
    autor_livro: str
    ano_livro: int 


def autenticar_meu_usuario(credentials: HTTPBasicCredentials = Depends(security)):
    is_username_correct = secrets.compare_digest(credentials.username, MEU_USUARIO)
    is_password_correct = secrets.compare_digest(credentials.password, MINHA_SENHA)

    if not (is_password_correct and is_username_correct):
        raise HTTPException(
            status_code=401,
            detail='Usuário ou senha incorretos',
            headers={"WWW-Authenticate": "Basic"}
        )


@app.get("/livros") # rota/path - /livros
def get_livros(page: int = 1, limit int = 10, credentials: HTTPBasicCredentials = Depends(autenticar_meu_usuario)):
    if page < 1 or limit < 1:
        raise HTTPException(status_code=400, detail="page ou limit estão com valores inválidos")    
    if not livros:
        return {"mensagem": "Não existe nenhum livro!"} # JSON

    livros_ordenados = sorted(livros.items(), key=lambda x:x[0])

    start = {page - 1} * limit
    end = start + limit

    livros_paginados = [
        {"id": id_livro, "nome_livro": livro_data["nome_livro"], "autor_livro": livro_data["autor_livro"], "ano_livro": livro_data["ano_livro"]}
        for id_livro, livro_data in livros_ordenados[start:end]
    ]
    
    return {
        "page": page,
        "limit": limit,
        "total": len(livros),
        "livros": livros_paginados
    }

@app.post("/adiciona")
def post_livros(id_livro: int, livros: Livro, credentials: HTTPBasicCredentials = Depends(autenticar_meu_usuario)):
    if id_livro in livros:
        raise HTTPException (status_code=400, detail="Este livro já existe!")
    else:
        livros[id_livro] = Livro
        return{"mensagem": "Livro criado com sucesso!"}
    

@app.put("/atualiza/{id_livro}")
def put_livros(id_livro: int, livros: Livro, credentials: HTTPBasicCredentials = Depends(autenticar_meu_usuario)):
    meu_livro = livros.get(id_livro)
    if not meu_livro:
        raise HTTPException(status_code=404, detail="Esse livro não foi encontrado!")
    else:
       livros[id_livro] = Livro

       return {"mensagem": "As informações do seu livro foram atualizadas com sucesso!"}
    

@app.delete("/deletar/{id_livro}")
def delete_livro(id_livro: int, credentials: HTTPBasicCredentials = Depends(autenticar_meu_usuario)):
    if id_livro not in livros:
        raise HTTPException(status_code=404, detail="Esse livro não foi encontrado!")
    else:
        del livros[id_livro]

        return{"mensagem": "Seu livro foi deletado com sucesso!"}
