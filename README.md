# Calculadora Financeira

## Introdução

A Calculadora Financeira é um projeto que reúne diversas ferramentas para auxiliar em cálculos financeiros e matemáticos. Com uma interface amigável e gráficos intuitivos, a aplicação oferece recursos para:

- **Cálculo de Juros Compostos**: Simule o crescimento de um investimento ao longo do tempo
- **Juros com Aportes Mensais**: Calcule o montante de um investimento com adições mensais
- **Cálculo de IRRF**: Estime o Imposto de Renda Retido na Fonte sobre rendimentos
- **Cálculo de INSS**: Calcule a contribuição ao INSS com base no salário
- **Equação da Reta**: Gere gráficos e equações lineares a partir de dois pontos

Todos os cálculos são processados no servidor Python, e os resultados são exibidos com gráficos interativos para melhor compreensão.

## Pré-requisitos

- Python 3.10 ou superior
- Conexão com a internet

## Instalação Simples

1. Clone o repositório ou baixe o código:
```
git clone https://github.com/seu-usuario/Projeto-de-Investimento.git
cd Projeto-de-Investimento
```

2. Instale as dependências:
```
pip install -r requirements.txt
```

## Executando o Projeto

1. Inicie o servidor com o comando:
```
python -m uvicorn main:app --host=0.0.0.0 --port=8000
```

2. Acesse a aplicação no navegador:
```
http://localhost:8000
```

## Como Usar as Calculadoras

### Página Inicial

A página inicial apresenta todas as calculadoras disponíveis. Clique no botão correspondente à calculadora que deseja utilizar.

### Calculadora de Juros Compostos

1. Preencha o capital inicial (valor a ser investido)
2. Defina o tempo em meses
3. Informe a taxa de juros mensal (%)
4. Digite o IPCA estimado anual (inflação)
5. Clique em "Calcular"

O resultado mostrará o montante final e um gráfico comparando o crescimento do investimento com a inflação.

### Juros com Aportes Mensais

1. Informe o capital inicial
2. Digite o valor do aporte mensal (valor a ser adicionado todos os meses)
3. Defina o tempo em meses
4. Informe a taxa de juros mensal (%)
5. Clique em "Calcular Investimento"

O resultado mostrará o montante final e um gráfico de evolução do investimento ao longo do tempo.

### Calculadora de IRRF

1. Informe o salário base (após descontar o INSS)
2. Digite o número de dependentes (se houver)
3. Clique em "Calcular IRRF"

O resultado mostrará o valor do IRRF a ser retido e um gráfico com a evolução do imposto de acordo com a faixa salarial.

### Calculadora de INSS

1. Digite o salário bruto
2. Clique em "Calcular Desconto"

O resultado mostrará o valor do desconto do INSS e um gráfico das faixas de contribuição.

### Equação da Reta

1. Informe as coordenadas X e Y do primeiro ponto
2. Informe as coordenadas X e Y do segundo ponto
3. Clique em "Gerar Gráfico"

O resultado mostrará a equação da reta que passa pelos dois pontos e o gráfico correspondente.

## Solução de Problemas Comuns

### O servidor não inicia
- Certifique-se de que as dependências foram instaladas corretamente
- Verifique se não há outro processo usando a porta 8000

### Os gráficos não aparecem
- Verifique se o servidor está rodando
- Tente atualizar a página (F5)
- Verifique no console do navegador (F12) se há erros de conexão

### Erro ao calcular valores
- Verifique se todos os campos estão preenchidos corretamente
- Use pontos (.) ao invés de vírgulas (,) para separar decimais
- Certifique-se de que os valores estão dentro de limites razoáveis

## Deployment no Render.com

Para fazer deploy deste projeto no Render.com:

1. Crie uma conta no [Render](https://render.com)
2. Clique em "New" e selecione "Web Service"
3. Conecte seu repositório GitHub ou forneça o URL do repositório
4. Configure as seguintes opções:
   - **Name**: Nome do seu projeto
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port 10000`
5. Clique em "Create Web Service"

O Render detectará automaticamente as alterações no repositório e fará novos deploys quando necessário.

## Desenvolvimento

Este projeto foi desenvolvido usando:
- Frontend: HTML, CSS e JavaScript incorporado nas páginas HTML
- Backend: Python com FastAPI
- Geração de gráficos: Matplotlib

## Licença

Este projeto é distribuído sob a licença MIT. Sinta-se livre para usar, modificar e distribuir conforme necessário.
