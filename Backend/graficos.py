"""
Arquivo: graficos.py

Este módulo contém funções para gerar gráficos de comparação e crescimento de investimentos.
Pode ser importado por qualquer outro módulo de cálculo.

IMPORTANTE:
Este arquivo foi adaptado para evitar importações circulares. Agora, as funções de gráfico
recebem os dados prontos (listas de valores) gerados por outras funções.
"""
import matplotlib
matplotlib.use('Agg')  # Usa backend que não depende de GUI
import matplotlib.pyplot as plt
import io
import base64


def gerar_grafico_simples(tempos, valores, titulo, label):
    """
    Gera um gráfico simples com uma curva.
    """
    plt.plot(tempos, valores, marker='o', label=label)
    plt.title(titulo)
    plt.xlabel('Tempo')
    plt.ylabel('Valor Acumulado (R$)')
    plt.grid(True)
    plt.legend()
    plt.show()

def gerar_grafico_duplo(tempos, valores1, valores2, label1, label2, titulo):
    """
    Gera um gráfico com duas curvas para comparação.
    """
    plt.plot(tempos, valores1, marker='o', label=label1)
    plt.plot(tempos, valores2, marker='x', linestyle='--', label=label2)
    plt.title(titulo)
    plt.xlabel('Tempo')
    plt.ylabel('Valor Acumulado (R$)')
    plt.grid(True)
    plt.legend()
    plt.show()

def gerar_grafico_valores_finais(capital, taxa, tempo, aporte):
    valores_taxa = []
    valores_ipca = []
    tempos = list(range(tempo + 1))

    for t in tempos:
        montante_taxa = capital * ((1 + taxa / 100) ** t) + aporte * t
        montante_ipca = capital * ((1 + 0.04) ** t) + aporte * t
        valores_taxa.append(montante_taxa)
        valores_ipca.append(montante_ipca)

    plt.figure(figsize=(10, 5))
    plt.plot(tempos, valores_taxa, label="Com Taxa de Aplicação", color="blue")
    plt.plot(tempos, valores_ipca, label="Com IPCA (inflação)", color="orange", linestyle="--")
    plt.title("Comparativo: Aplicação vs IPCA")
    plt.xlabel("Tempo (meses)")
    plt.ylabel("Valor Acumulado (R$)")
    plt.grid(True)
    plt.legend()

    # Convertendo para base64
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    plt.close()
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.read()).decode("utf-8")
    return img_base64