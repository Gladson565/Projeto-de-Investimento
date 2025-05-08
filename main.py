from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

from investimentos import calcular_juros_compostos
from investimentos_aportes import calcular_montante_com_aportes
from inss import calcular_inss, gerar_grafico_inss
from impostos import calcular_irrf_final as calcular_irrf, gerar_grafico_irrf_base64
from equacao_reta import gerar_grafico_reta
from graficos import gerar_grafico_valores_finais
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou restrinja por domínio se quiser
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar a pasta de arquivos estáticos
app.mount("/css", StaticFiles(directory="css"), name="css")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

# Rota para a página principal
@app.get("/")
async def read_index():
    return FileResponse('index.html')

# Rotas para outras páginas HTML
@app.get("/jurosCompostos.html")
async def read_juros_compostos():
    return FileResponse('jurosCompostos.html')

@app.get("/irrf.html")
async def read_irrf():
    return FileResponse('irrf.html')

@app.get("/inss.html")
async def read_inss():
    return FileResponse('inss.html')

@app.get("/ipca.html")
async def read_ipca():
    return FileResponse('ipca.html')

@app.get("/equacao.htm")
async def read_equacao():
    return FileResponse('equacao.htm')

# ---------- MODELOS ----------

class JurosCompostosInput(BaseModel):
    capital: float
    taxa: float
    tempo: int
    ipca: float

class JurosAporteInput(BaseModel):
    capital: float
    taxa: float
    tempo: int
    aporte_mensal: float

class INSSRequest(BaseModel):
    salario: float

class IRRFRequest(BaseModel):
    salario: float
    dependentes: int

class Pontos(BaseModel):
    x1: float
    y1: float
    x2: float
    y2: float

class GraficoInput(BaseModel):
    capital_inicial: float
    taxa_juros: float
    tempo: int
    aporte: float

# ---------- ROTAS ----------

@app.post("/api/juros-compostos")
def juros_compostos(data: JurosCompostosInput):
    resultado = calcular_juros_compostos(data.capital, data.taxa, data.tempo)
    return {"montante": round(resultado, 2)}

@app.post("/api/juros-compostos-grafico")
def juros_compostos_grafico_json(data: JurosCompostosInput):
    """Endpoint para fornecer dados para gráfico interativo de juros compostos"""
    capital = data.capital
    taxa = data.taxa
    tempo = data.tempo
    ipca = data.ipca if hasattr(data, 'ipca') else 4.5  # Valor padrão de IPCA caso não seja fornecido
    
    # Converter IPCA anual para mensal
    ipca_mensal = ((1 + ipca/100) ** (1/12) - 1) * 100
    
    # Gerar dados para todo o período
    tempos = list(range(tempo + 1))
    valores_juros = [round(capital * ((1 + taxa/100) ** t), 2) for t in tempos]
    valores_ipca = [round(capital * ((1 + ipca_mensal/100) ** t), 2) for t in tempos]
    
    return {
        "labels": tempos,
        "datasets": [
            {
                "name": "Rendimento com Juros",
                "valores": valores_juros
            },
            {
                "name": "Correção pela Inflação (IPCA)",
                "valores": valores_ipca
            }
        ]
    }

@app.post("/api/grafico")
def grafico(data: GraficoInput):
    img_base64 = gerar_grafico_valores_finais(
        data.capital_inicial, data.taxa_juros, data.tempo, data.aporte
    )
    return {"grafico_base64": img_base64}

@app.post("/api/juros-aporte")
def juros_com_aporte(data: JurosAporteInput):
    resultado = calcular_montante_com_aportes(
        data.capital, data.aporte_mensal, data.taxa, data.tempo
    )
    return {"montante": round(resultado, 2)}

@app.post("/api/inss")
async def calcular_inss_api(req: INSSRequest):
    salario_usuario = req.salario
    inss_usuario = round(calcular_inss(salario_usuario), 2)
    
    # Gerar gráfico com matplotlib e converter para base64
    grafico_base64 = gerar_grafico_inss(salario_usuario, inss_usuario)
    
    # Certifique-se de que a chave corresponde ao que o frontend espera
    return {
        "desconto": inss_usuario,
        "graficoUrl": f"data:image/png;base64,{grafico_base64}"
    }

@app.post("/api/irrf")
def irrf(data: IRRFRequest):
    base_calculo = data.salario 
    dependentes = data.dependentes if hasattr(data, 'dependentes') else 0
    desconto = calcular_irrf(base_calculo, dependentes)
    
    # Gerar gráfico com matplotlib e converter para base64
    grafico_base64 = gerar_grafico_irrf_base64(base_calculo, dependentes)
    
    return {
        "irrf": round(desconto, 2),
        "graficoUrl": f"data:image/png;base64,{grafico_base64}"
    }

@app.post("/api/equacao-reta-grafico")
def gerar_grafico(pontos: Pontos):
    grafico_base64 = gerar_grafico_reta(pontos.x1, pontos.y1, pontos.x2, pontos.y2)
    return {"grafico_base64": grafico_base64}
