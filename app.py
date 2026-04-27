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
        