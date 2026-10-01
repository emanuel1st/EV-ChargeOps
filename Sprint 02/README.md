# EV ChargeOps

Sistema desenvolvido para o projeto Enterprise Challenge 2026 — GoodWe + FIAP.

O EV ChargeOps tem como objetivo organizar o gerenciamento de carregamento de veículos elétricos, registrando sessões de carregamento, calculando o consumo individual, gerando faturas e disponibilizando análises de consumo.

## Funcionalidades

* Dashboard com indicadores do sistema
* Registro de sessões de carregamento
* Cálculo da duração da sessão
* Registro do consumo em kWh
* Cálculo de faturamento por consumo individual
* Geração de faturas
* Consulta de usuários
* Consulta de carregadores
* Análise de consumo
* Previsão de demanda
* Detecção de possíveis anomalias
* Testes automatizados

## Arquitetura

O sistema foi desenvolvido utilizando uma arquitetura organizada em camadas:

* **Apresentação:** páginas HTML e CSS
* **Rotas:** gerenciamento das requisições da aplicação
* **Serviços:** regras de negócio
* **Banco de dados:** SQLite
* **IA:** análise de consumo, previsão de demanda e detecção de anomalias

### Fluxo principal

Usuário → Sessão de carregamento → Banco de dados → Cálculo de consumo → Faturamento

O módulo de IA utiliza os dados registrados nas sessões para gerar indicadores, realizar uma previsão simples de consumo e identificar possíveis anomalias.

## Tecnologias utilizadas

* Python
* Flask
* SQLite
* HTML
* CSS
* Jinja2
* Pytest

## Estrutura do projeto

```text
EV-ChargeOps/
├── app/
│   ├── ai/
│   ├── database/
│   ├── routes/
│   ├── services/
│   └── templates/
├── static/
│   ├── css/
│   └── js/
├── tests/
├── data/
├── evidencias/
├── requirements.txt
└── run.py
```

## Como executar

### 1. Criar e ativar o ambiente virtual

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 2. Instalar as dependências

```powershell
pip install -r requirements.txt
```

### 3. Criar os dados de teste

```powershell
python -c "from app.database.seed import seed_database; seed_database(); print('Dados de teste inseridos com sucesso!')"
```

### 4. Executar o sistema

```powershell
python run.py
```

Depois, acessar:

```text
http://127.0.0.1:5000/dashboard
```

## Testes

Para executar os testes automatizados:

```powershell
python -m pytest -v
```

Os testes verificam funcionalidades relacionadas ao registro de sessões, faturamento e módulo de IA.

## Módulo de IA

O sistema possui três componentes principais:

### Análise de consumo

Calcula:

* quantidade de sessões;
* consumo total;
* consumo médio;
* maior consumo registrado.

### Previsão de demanda

Utiliza o histórico de consumo registrado para realizar uma previsão simples do consumo da próxima sessão.

### Detecção de anomalias

Compara os consumos registrados e identifica sessões que apresentam consumo significativamente acima da média utilizada pelo protótipo.

## Evidências

As evidências de funcionamento do sistema ficam armazenadas na pasta:

```text
evidencias/
```

Elas demonstram as principais funcionalidades desenvolvidas durante o Sprint 02.

## Projeto acadêmico

Projeto desenvolvido para o Enterprise Challenge 2026 — GoodWe + FIAP.

**EV ChargeOps — Sprint 02**
