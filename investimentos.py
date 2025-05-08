from graficos import gerar_grafico_duplo

def calcular_juros_compostos(capital_inicial, taxa, tempo):
    """
    Calcula o montante final com juros compostos sem aportes.
    Fórmula: M = C * (1 + i) ^ t
    """
    montante = capital_inicial * ((1 + taxa / 100) ** tempo)
    return round(montante, 2)

def calcular_montante_ipca(capital_inicial, ipca, tempo):
    """
    Calcula o montante final com base apenas na taxa do IPCA.
    """
    montante = capital_inicial * (1 + ipca) ** tempo
    return round(montante, 2)

def calcular_diferenca(montante_aplicacao, montante_ipca):
    """
    Calcula a diferença entre o valor investido com taxa real e com inflação.
    """
    return round(montante_aplicacao - montante_ipca, 2)

if __name__ == "__main__":
    capital = 1000.0
    taxa = 0.10  # 10% ao ano
    ipca = 0.04  # 4% ao ano
    tempo = 10   # anos

    montante_taxa = calcular_juros_compostos(capital, taxa, tempo)
    montante_ipca = calcular_montante_ipca(capital, ipca, tempo)

    diferenca = calcular_diferenca(montante_taxa, montante_ipca)

    print(f"Montante com taxa de aplicação: R$ {montante_taxa}")
    print(f"Montante com IPCA: R$ {montante_ipca}")
    print(f"Diferença: R$ {diferenca}")

    tempos = list(range(tempo + 1))
    valores_taxa = [calcular_juros_compostos(capital, taxa, t) for t in tempos]
    valores_ipca = [calcular_montante_ipca(capital, ipca, t) for t in tempos]

    gerar_grafico_duplo(
        tempos,
        valores_taxa,
        valores_ipca,
        "Taxa de Aplicação",
        "IPCA",
        "Comparativo: Aplicação vs IPCA (sem aportes)"
    )

    # ✅ Mover este bloco para dentro também
    if montante_taxa > montante_ipca:
        print("✅ A aplicação superou a inflação. Houve ganho real.")
    else:
        print("⚠️ A inflação superou a aplicação. Houve perda de poder de compra.")
