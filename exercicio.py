from fastapi import FastAPI, HTTPException

app = FastAPI()

tarefas = []

@app.post("/adicionar tarefa")
def post_tarefas(nome: str, descricao: str):
    if nome in tarefas:
        raise HTTPException(status_code=400, detail="Essa tarefa já existe!")
    else:
        tarefas = {"nome": nome, "descrição": descricao}
        return {"mensagem": "Tarefa adicionada com sucesso!"}


@app.get("/tarefas")
def get_tarefas():
    if not tarefas:
        return {"mensagem": "Não há nenhuma tarefa."}
    else:
        return tarefas
    

@app.put("/status/{nome}")
def put_tarefas(nome: str, concluida: str):
    tarefas = {"concluída": concluida}
    if not tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada!")
    else:
        if nome:
            tarefas["concluída"] = concluida

        return {"mensagem": "Tarefa concluída!"}


@app.delete("/deletar/{nome}")
def delete_tarefas(nome: str):
    if nome not in tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada!")
    else:
        del tarefas[nome]

        return {"mensagem": "Tarefa deletada com sucesso"}
    