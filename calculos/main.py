from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from investimentos import calcular_juros_compostos
from investimentos_aportes import calcular_montante_com_aportes
from inss import calcular_inss, gerar_grafico_inss
from impostos import calcular_irrf_final as calcular_irrf
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


# ---------- MODELOS ----------

class JurosCompostosInput(BaseModel):
    capital: float
    taxa: float
    tempo: int

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
async def calcular_inss_api(req: INSSRequest): # type: ignore
    salario = req.salario
    inss = calcular_inss(salario)
    grafico_base64 = calcular_inss(salario, inss)

    return {
        "inss": inss,
        "grafico_base64": grafico_base64
    }
@app.post("/api/irrf")
def irrf(data: IRRFRequest):
    desconto = calcular_irrf(data.salario, data.dependentes)
    return {"desconto_irrf": round(desconto, 2)}


@app.post("/api/equacao-reta-grafico")
def gerar_grafico(pontos: Pontos):
    grafico_base64 = gerar_grafico_reta(pontos.x1, pontos.y1, pontos.x2, pontos.y2)
    return {"grafico_base64": grafico_base64}
