from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import matplotlib.pyplot as plt
import io
import base64

# -------------------- LÓGICA DO CÁLCULO -----------------------

def calcular_inss(salario):
    if salario <= 1412.00:
        return salario * 0.075
    elif salario <= 2666.68:
        return (1412 * 0.075) + ((salario - 1412) * 0.09)
    elif salario <= 4000.03:
        return (1412 * 0.075) + ((2666.68 - 1412) * 0.09) + ((salario - 2666.68) * 0.12)
    elif salario <= 7786.02:
        return (1412 * 0.075) + ((2666.68 - 1412) * 0.09) + ((4000.03 - 2666.68) * 0.12) + ((salario - 4000.03) * 0.14)
    else:
        return 908.86  # Teto do INSS em 2025

def gerar_grafico_inss(salario_usuario, inss_usuario):
    salarios = list(range(0, 9000, 100))
    descontos = [calcular_inss(s) for s in salarios]

    plt.figure(figsize=(10, 5))
    plt.plot(salarios, descontos, label="Desconto INSS")
    plt.axvline(salario_usuario, color='r', linestyle='--', label=f"Seu salário: R$ {salario_usuario:.2f}")
    plt.axhline(inss_usuario, color='r', linestyle='--', label=f"Desconto: R$ {inss_usuario:.2f}")
    plt.xlabel("Salário (R$)")
    plt.ylabel("INSS (R$)")
    plt.title("Cálculo do INSS - 2025")
    plt.grid(True)
    plt.legend()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)
    imagem_base64 = base64.b64encode(buf.read()).decode("utf-8")
    return imagem_base64
