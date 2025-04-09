# Backend - Projeto de Investimentos

Bem-vindo ao **coração do sistema**! Aqui vamos explicar tudo o que acontece dentro do backend (a parte "invisível" que faz os cálculos e responde aos pedidos do site), passo a passo, como se estivéssemos contando uma história para uma criança.

---

## 🏡 O que é o backend?

Imagine que você vai até uma lanchonete. O **frontend** é o cardápio e o atendente que anota seu pedido. O **backend** é a **cozinha**, onde o lanche é preparado.

No nosso projeto, quando o usuário envia dados (como quanto quer investir), é o backend que faz as contas e devolve a resposta.

---

## 📂 Estrutura da Pasta

```
/backend
├── server.js             # Gerente do sistema, liga tudo
├── /controllers          # Chefs de cozinha: fazem os cálculos
├── /routes               # Garçons: recebem o pedido e entregam para os chefs
├── /middlewares          # Segurança: checam se os pedidos estão certos
├── /utils                # Ajudantes: funções extras que ajudam nos cálculos
├── /config               # Configurações (ex: banco de dados)
```

---

## 🚀 Como tudo funciona?

1. O usuário envia uma informação (por exemplo: investir R$100 por mês durante 12 meses com 1% de juros).
2. A **rota** recebe o pedido e chama o **controller**.
3. O **controller** faz os cálculos e devolve a resposta (como um chef fazendo um prato).
4. O sistema responde com o resultado pronto!

---

## 📊 Explicando os algoritmos dos controllers

### 1. Investimentos com juros compostos

No `investimentosController.js`, temos uma função que calcula o valor final de um investimento com aportes mensais.

**Lógica:**
Para cada mês, somamos o aporte e aplicamos a taxa de juros:
```javascript
let montante = 0;
for (let i = 1; i <= tempoMeses; i++) {
  montante = (montante + aporteMensal) * (1 + taxaJuros / 100);
}
```
Isso simula o crescimento do dinheiro mês a mês.

---

### 2. IRRF (Imposto de Renda)

Para calcular o IRRF, usamos as **faixas da tabela oficial**. Primeiro subtraímos a dedução por dependentes do salário, depois aplicamos a alíquota da faixa correspondente.

**Exemplo:**
```javascript
let base = salarioBruto - (dependentes * 189.59);
// Aplica a alíquota com base na faixa salarial
```

---

### 3. INSS

Usamos a tabela progressiva do INSS. Calculamos quanto pagar em cada faixa e somamos.

**Exemplo:**
```javascript
// Salário até R$1518 → 7.5%
// Parte entre R$1518 e R$2793,88 → 9%, e assim por diante
```

---

### 4. Equação da reta

Recebemos dois pontos (x1, y1) e (x2, y2) e calculamos:
- Coeficiente angular (a): `(y2 - y1) / (x2 - x1)`
- Termo independente (b): `y1 - a * x1`

Depois mostramos a equação: `f(x) = ax + b`, e os pontos onde toca os eixos.

---

## ⚙️ Como rodar o backend

1. Abra o terminal e digite:
```bash
cd backend
npm install
node server.js
```
2. O servidor vai dizer: `Servidor rodando na porta 3000`
3. Agora ele está pronto para responder pedidos!

---

## 📢 Exemplo de uso (com Postman ou Insomnia)

- Rota: `POST http://localhost:3000/api/investimentos/calcular`
- Corpo:
```json
{
  "aporteMensal": 1000,
  "taxaJuros": 1,
  "tempoMeses": 12
}
```
- Resposta esperada:
```json
{
  "montante": "12735.52"
}
```

---

## 💪 Em breve...
- Cálculos de inflação (IPCA)
- Gráficos comparando crescimento do dinheiro
- Integração com Python para cálculos matemáticos
- Banco de dados para salvar os resultados

---

Feito com muito carinho e cálculo ❤️ por **Gladson**

