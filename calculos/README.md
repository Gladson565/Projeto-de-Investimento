# 📊 Projeto de Cálculos Matemáticos em Python

Este projeto tem como objetivo realizar diferentes tipos de cálculos matemáticos e financeiros usando Python, incluindo a visualização gráfica das funções. Os seguintes tópicos foram abordados:

---

## 🧮 1. Juros Compostos

### 📘 Fórmula:
\[
M = C \cdot (1 + i)^t
\]

- `M`: Montante final  
- `C`: Capital inicial  
- `i`: Taxa de juros (mensal, anual, etc.)  
- `t`: Tempo (meses, anos, etc.)

### 📥 Entrada:

- Capital: `float`
- Taxa de juros (em %): `float`
- Tempo: `int`

### 📤 Saída:
- Montante final
- Gráfico da evolução do capital ao longo do tempo

---

## 💰 2. Juros Compostos com Aportes Mensais

### 📘 Fórmula:
\[
M = C \cdot (1 + i)^t + A \cdot \frac{(1 + i)^t - 1}{i}
\]

- `A`: Valor do aporte mensal

### 📥 Entrada:
- Capital inicial
- Taxa de juros
- Tempo (meses)
- Aporte mensal

### 📤 Saída:
- Montante final
- Gráfico mostrando a curva de crescimento com aportes

---

## 🧾 3. Cálculo de INSS

### 📘 Tabela Progressiva (valores de exemplo):
| Faixa Salarial         | Alíquota (%) |
|------------------------|--------------|
| Até R$ 1.320,00        | 7,5%         |
| R$ 1.320,01 a R$ 2.571,29 | 9%       |
| R$ 2.571,30 a R$ 3.856,94 | 12%      |
| R$ 3.856,95 a R$ 7.507,49 | 14%      |

> A tabela é aplicada de forma **progressiva**, ou seja, cada faixa é tributada separadamente.

### 📥 Entrada:
- Salário bruto

### 📤 Saída:
- Valor do desconto de INSS
- Salário base para IRRF

---

## 📉 4. Cálculo de IRRF

### 📘 Tabela Progressiva (valores de exemplo):
| Faixa Base de Cálculo      | Alíquota (%) | Parcela a Deduzir (R$) |
|----------------------------|---------------|-------------------------|
| Até R$ 2.112,00            | Isento        | -                       |
| R$ 2.112,01 a R$ 2.826,65  | 7,5%          | 158,40                  |
| R$ 2.826,66 a R$ 3.751,05  | 15%           | 370,40                  |
| R$ 3.751,06 a R$ 4.664,68  | 22,5%         | 651,73                  |
| Acima de R$ 4.664,68       | 27,5%         | 884,96                  |

### 📥 Entrada:
- Salário bruto

### 📤 Saída:
- Valor do desconto de IRRF
- Salário líquido final

---

## 📐 5. Equação da Reta (Função do 1º Grau)

### 📘 Fórmula da função:
\[
f(x) = ax + b
\]

- `a`: Coeficiente angular (inclinação da reta)  
- `b`: Coeficiente linear (intercepto no eixo y)

### 📥 Entrada:
- Dois pontos no plano cartesiano: `(x1, y1)` e `(x2, y2)`

### 🧮 Cálculos realizados:
- **Coeficiente angular (a):**
  \[
  a = \frac{y2 - y1}{x2 - x1}
  \]
- **Coeficiente linear (b):**
  \[
  b = y1 - a \cdot x1
  \]
- **Intercepto x (quando y = 0):**
  \[
  x = -\frac{b}{a}
  \]
- **Intercepto y (quando x = 0):**
  \[
  f(0) = b
  \]

### 📤 Saída:
- Equação da reta `f(x) = ax + b`
- Ponto de intercepto com o eixo X
- Ponto de intercepto com o eixo Y
- **Gráfico** da função com destaque para:
  - Pontos informados
  - Intercepto no eixo X (vermelho)
  - Intercepto no eixo Y (verde)

---

## 📊 Visualização Gráfica

Todos os gráficos foram gerados usando a biblioteca `matplotlib`, com destaque para:
- Estilização dos pontos calculados
- Legendas explicativas
- Título e rótulos nos eixos

---

## 🛠 Tecnologias Utilizadas

- Python 3.x
- Matplotlib
- VS Code / Terminal Git / Terminal Powershell

---

## 📂 Estrutura do Projeto

calculos/ ├── juros_compostos.py ├── juros_compostos_com_aportes.py ├── inss.py ├── irrf.py ├── equacao_reta.py ├── README.md


---
## ✍️ Autor

Desenvolvido por Gladson M Andrde como parte de estudo e prática com Python, matemática financeira e visualização de dados.

