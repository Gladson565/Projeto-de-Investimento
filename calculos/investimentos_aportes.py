import matplotlib.pyplot as plt
from graficos import gerar_grafico_duplo

def calcular_montante_com_aportes(capital_inicial, aporte_mensal, taxa, tempo):
    """
    Calcula o montante com aportes mensais e taxa de aplicação.
    """
    montante = capital_inicial
    for _ in range(tempo):
        montante = (montante + aporte_mensal) * (1 + taxa / 100)
    return round(montante, 2)

def calcular_montante_com_ipca(capital_inicial, aporte_mensal, ipca, tempo):
    """
    Calcula o montante com aportes mensais corrigido pela inflação (IPCA).
    """
    montante = capital_inicial
    for _ in range(tempo):
        montante = (montante + aporte_mensal) * (1 + ipca / 100)
    return round(montante, 2)

def calcular_diferenca(montante_aplicacao, montante_ipca):
    return round(montante_aplicacao - montante_ipca, 2)

# Teste direto (opcional)
if __name__ == "__main__":
    capital = 100.0
    aporte = 200.0
    taxa = 0.8   # 0.8% ao mês
    ipca = 0.4   # 0.4% ao mês
    tempo = 12   # meses

    montante_aplicacao = calcular_montante_com_aportes(capital, aporte, taxa, tempo)
    montante_ipca = calcular_montante_com_ipca(capital, aporte, ipca, tempo)
    diferenca = calcular_diferenca(montante_aplicacao, montante_ipca)

    print(f"Montante final com taxa de aplicação: R$ {montante_aplicacao}")
    print(f"Montante final com IPCA: R$ {montante_ipca}")
    print(f"Diferença entre eles: R$ {diferenca}")

    tempos = list(range(tempo + 1))
    valores_aplicacao = [calcular_montante_com_aportes(capital, aporte, taxa, t) for t in tempos]
    valores_ipca = [calcular_montante_com_ipca(capital, aporte, ipca, t) for t in tempos]

    gerar_grafico_duplo(
        tempos,
        valores_aplicacao,
        valores_ipca,
        "Aplicação + Aportes",
        "IPCA + Aportes",
        "Comparativo: Aplicação vs IPCA (com aportes)"
    )

