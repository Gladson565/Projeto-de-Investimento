# equacao_reta.py

import matplotlib
matplotlib.use('Agg')  # Usa backend que não depende de GUI
import matplotlib.pyplot as plt
import io
import base64

def calcular_equacao_reta(x1, y1, x2, y2):
    if x1 == x2:
        raise ValueError("Os valores de x1 e x2 não podem ser iguais. A reta seria vertical.")
    a = (y2 - y1) / (x2 - x1)
    b = y1 - a * x1
    return a, b

def gerar_grafico_reta(x1, y1, x2, y2):
    a, b = calcular_equacao_reta(x1, y1, x2, y2)
    x_intercept = -b / a
    y_intercept = b

    x_vals = [min(x1, x2) - 2, max(x1, x2) + 2]
    y_vals = [a * x + b for x in x_vals]

    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label=f'f(x) = {a:.2f}x + {b:.2f}', color='blue')
    plt.scatter([x1, x2], [y1, y2], color='black', label='Pontos informados')
    plt.scatter([x_intercept], [0], color='red', label=f'Intercepto x: ({x_intercept:.2f}, 0)')
    plt.scatter([0], [y_intercept], color='green', label=f'Intercepto y: (0, {y_intercept:.2f})')

    plt.axhline(0, color='gray', linewidth=0.5)
    plt.axvline(0, color='gray', linewidth=0.5)
    plt.title("Gráfico da Função do 1º Grau")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)

    return base64.b64encode(buffer.read()).decode('utf-8')
