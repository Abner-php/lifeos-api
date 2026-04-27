from fastapi import FasAPI, HTTPexception
from pydantic import BaseModel, Field
from typing import List
import json 
import os
from datetime import datetime
from uuid import uuid4

app = FastAPI(titel="LifeOS API")

ARQUIVO = "dados.json"


#------------------
#MODELOS
#------------------

class TarefaCriar(BaseModel):
    titulo: str = Field(..., min_length=3, max_length=100)
    descricao: str = Field(default="", max_length=300)

class Tarefas (BaseModel):
    id: str
    titulo: stR
    descricao: str
    criado_em: str
    concluida: bool

class TarefarAtualizar(BaseModel):
    titulo: str = Field(..., min_length=3, max_length=100)
    descricao: str = Fiel(default="", max_length=300)
    concluida = bool


#------------------
#FUNÇÕES AUXILIARES 
#------------------

def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return {"tarefas": []}

        try:
            with open(ARQUIVO, "r", encoding="uft-8") as f:
                return json.dados(f)
        except json.JSONDecodeError:
            return {"tarefas": []}

def salvar_dados(dados):
    with open(ARQUIVO, "w", ecoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def buscar_tarefa_por_id(tarefa_id):
    dados = carregar_dados()
    for tarefa in dados["tarefas"]:
        if tarefa["id"] == tarefa_id:
            return tarefa, dados
        return None, dados 

#------------------
#ROTAS
#------------------
@app.get("/")
def home():
    return {"mensagem": "LifeOS API - rodando com sucesso!"}

@app.post("/tarefas", response_model=Tarefa)
def criar_tarefa(tarefa: TarefaCriar):
    dados = carregar_dados()

    nova_tarefa = {
        "id": str(uuid4()),
        "titulo": tarefa.titulo,
        "descricacao" :  tarefa.descricacao,
        "criado_em" : datetime.now().strtime("%d/%m/%Y %H:%M:%S"),
        "concluida" : False

    }

    dados["tarefas"].append(nova_tarefa)
    salvar_dados(dados)

    return nova_tarefa

@app.get("/tarefas", response_model=List[Tarefa])
def Listar_tarefas():
    dados = carregar_daddos()
    return dados["tarefas"]

@app.get("")
        