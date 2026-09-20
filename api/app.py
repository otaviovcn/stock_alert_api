from fastapi import FastAPI
import json
from pathlib import Path

app = FastAPI(title="Stock Alert API")

DATA_PATH = Path("reports/resumo_estoque.json")

def carregar_resumo():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

@app.get("/")
def root():
    return {"mensagem": "Stock Alert API. Use /resumo, /riscos, /parado, /categorias, /fornecedores"}

@app.get("/resumo")
def resumo():
    return carregar_resumo()

@app.get("/riscos")
def riscos():
    return carregar_resumo()["produtos_em_risco"]

@app.get("/parado")
def total_parado():
    return {"total_parado": carregar_resumo()["resumo_geral"]["total_parado"]}

@app.get("/categorias")
def categorias():
    return carregar_resumo()["por_categoria"]

@app.get("/fornecedores")
def fornecedores():
    return carregar_resumo()["por_fornecedor"]