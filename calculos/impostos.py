import matplotlib.pyplot as plt

# 3.1 Entrada
def calcular_base_calculo(salario_bruto, dependentes):
    """
    Calcula a base de cálculo do IRRF considerando dedução por dependentes.
    """
    deducao_por_dependente = 189.59
    return salario_bruto - (dependentes * deducao_por_dependente)

# 3.2.1 e 3.2.2
def calcular_irrf(base_calculo):
    """
    Calcula o valor do IRRF a ser recolhido, com base na tabela de 2025.
    """
    if base_calculo <= 2259.20:
        return 0.0
    elif base_calculo <= 2826.65:
        return base_calculo * 0.075 - 169.44
    elif base_calculo <= 3751.05:
        return base_calculo * 0.15 - 381.44
    elif base_calculo <= 4664.68:
        return base_calculo * 0.225 - 662.77
    else:
        return base_calculo * 0.275 - 896.00

def calcular_irrf_sem_deducao(base_calculo):
    """
    Calcula o IRRF sem considerar a parcela dedutível (para efeito de comparação no gráfico).
    """
    if base_calculo <= 2259.20:
        return 0.0
    elif base_calculo <= 2826.65:
        return base_calculo * 0.075
    elif base_calculo <= 3751.05:
        return base_calculo * 0.15
    elif base_calculo <= 4664.68:
        return base_calculo * 0.225
    else:
        return base_calculo * 0.275

# 3.2.3 e 3.2.4

def gerar_graficos_irrf(base_usuario):
    """
    Gera dois gráficos:
    1. IRRF real com dedução
    2. IRRF sem dedução
    Ambos destacam o valor calculado do IRRF do usuário.
    """
    salarios = list(range(0, 7001, 100))
    irrf_com_deducao = [calcular_irrf(s) for s in salarios]
    irrf_sem_deducao = [calcular_irrf_sem_deducao(s) for s in salarios]

    valor_calculado = calcular_irrf(base_usuario)
    valor_sem_deducao = calcular_irrf_sem_deducao(base_usuario)

    # Gráfico com dedução
    plt.figure(figsize=(10, 5))
    plt.plot(salarios, irrf_com_deducao, label='IRRF com dedução')
    plt.axvline(base_usuario, color='r', linestyle='--', label=f'Sua base: R$ {base_usuario:.2f}')
    plt.axhline(valor_calculado, color='r', linestyle='--', label=f'Seu IRRF: R$ {valor_calculado:.2f}')
    plt.title("IRRF com dedução (2025)")
    plt.xlabel("Base de Cálculo (R$)")
    plt.ylabel("Valor do IRRF (R$)")
    plt.grid(True)
    plt.legend()
    plt.show()

    # Gráfico sem dedução
    plt.figure(figsize=(10, 5))
    plt.plot(salarios, irrf_sem_deducao, label='IRRF sem dedução', color='orange')
    plt.axvline(base_usuario, color='r', linestyle='--', label=f'Sua base: R$ {base_usuario:.2f}')
    plt.axhline(valor_sem_deducao, color='r', linestyle='--', label=f'Seu IRRF (sem dedução): R$ {valor_sem_deducao:.2f}')
    plt.title("IRRF sem dedução (2025)")
    plt.xlabel("Base de Cálculo (R$)")
    plt.ylabel("Valor do IRRF (R$)")
    plt.grid(True)
    plt.legend()
    plt.show()

def calcular_irrf_final(salario: float, dependentes: int) -> float:
    """
    Função principal para uso na API. Calcula o IRRF com base no salário e número de dependentes.
    """
    base = calcular_base_calculo(salario, dependentes)
    irrf = calcular_irrf(base)
    return max(0, round(irrf, 2))

if __name__ == "__main__":
    salario = float(input("Digite o salário bruto: R$ "))
    dependentes = int(input("Digite o número de dependentes: "))

    base = calcular_base_calculo(salario, dependentes)
    irrf = calcular_irrf(base)

    print(f"\nBase de Cálculo: R$ {base:.2f}")
    print(f"IRRF a recolher: R$ {irrf:.2f}")

    gerar_graficos_irrf(base)
