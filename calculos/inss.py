# calculos/inss.py

import matplotlib.pyplot as plt

def calcular_inss(salario_bruto):
    faixas = [
        (0.00, 1518.00, 0.075, 0.00),
        (1518.01, 2793.88, 0.09, 22.77),
        (2793.89, 4190.83, 0.12, 106.59),
        (4190.84, 8157.41, 0.14, 190.40)
    ]

    for faixa in faixas:
        minimo, maximo, aliquota, deducao = faixa
        if minimo <= salario_bruto <= maximo:
            inss = (salario_bruto * aliquota) - deducao
            return round(inss, 2)
    # Acima do teto
    teto = 8157.41
    inss_max = (teto * 0.14) - 190.40
    return round(inss_max, 2)

def gerar_grafico(salario_bruto, inss_valor):
    salarios = list(range(0, 9000, 50))
    valores_inss = [calcular_inss(sal) for sal in salarios]

    plt.figure(figsize=(10, 6))
    plt.plot(salarios, valores_inss, label='INSS com dedução (2025)', color='blue')
    plt.axvline(salario_bruto, color='red', linestyle='--', label=f'Salário: R$ {salario_bruto:.2f}')
    plt.axhline(inss_valor, color='green', linestyle='--', label=f'INSS: R$ {inss_valor:.2f}')
    plt.title('INSS com dedução (2025)')
    plt.xlabel('Salário Bruto (R$)')
    plt.ylabel('Valor do INSS (R$)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    salario = float(input("Digite o salário bruto: R$ "))
    inss = calcular_inss(salario)
    print(f"\nINSS a recolher: R$ {inss:.2f}")
    gerar_grafico(salario, inss)
