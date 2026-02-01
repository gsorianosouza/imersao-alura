# 📊 Dashboard de Análise de Salários na Área de Dados

Dashboard interativo desenvolvido durante a **Imersão Dados com Python – Alura (2026)** com foco em **análise exploratória de dados**, **visualização interativa** e **boas práticas de organização de código**.

O projeto permite explorar salários da área de dados ao longo dos anos através de filtros dinâmicos e gráficos interativos.

---

## 🚀 Funcionalidades

✔ Filtros por ano, senioridade, tipo de contrato e tamanho da empresa  
✔ Métricas principais (média, máximo, total de registros e cargo mais frequente)  
✔ Top cargos por média salarial  
✔ Distribuição de salários  
✔ Proporção de tipos de trabalho (remoto, híbrido, presencial)  
✔ Visualização de salários por país  
✔ Interface moderna com tema escuro e paleta quente personalizada  

---

## 🧠 Tecnologias utilizadas

| Tecnologia | Função |
|------------|--------|
| **Python** | Linguagem principal |
| **Streamlit** | Construção do dashboard |
| **Pandas** | Manipulação e análise dos dados |
| **Plotly** | Visualização interativa |

---

## 🎨 Interface

O dashboard utiliza um tema escuro personalizado:

- Fundo escuro moderno  
- Elementos em amarelo, laranja e vermelho  
- Cards com sombra e bordas suaves  
- Gráficos padronizados visualmente  

---

## 📂 Estrutura do projeto

IMERSAO-ALURA/
│
├── dashboard_salarios/ 
│ ├── app.py     # Arquivo principal que executa o app
│ ├── charts.py  # Funções responsáveis pelos gráficos
│ ├── data.py    # Carregamento do dataset
│ ├── filters.py # Lógica dos filtros laterais
│ ├── styles.py  # Tema visual e CSS
│ └── dados-imersao-final.csv
│
├── streamlit/
│ └── config.toml # Configurações do Streamlit
│
├── README.md
├── requirements.txt
├── requirements-dev.txt
└── .gitignore


---

## ⚙️ Como executar o projeto

``` 

### 1️⃣ Clonar o repositório

gitbash: 

git clone https://github.com/gsorianosouza/imersao-alura
cd IMERSAO-ALURA

### 2️⃣ Criar ambiente virtual (recomendado)

python -m venv .venv
.venv\Scripts\activate  # Windows

### 3️⃣ Instalar dependências

pip install -r requirements.txt

### 4️⃣ Executar o dashboard

streamlit run dashboard_salarios/app.py

📈 Fonte dos dados

Base de dados utilizada na Imersão Dados Alura, contendo informações sobre:

Salários anuais em USD

Cargos na área de dados

País de residência

Nível de senioridade

Tipo de contrato

Modelo de trabalho

🎯 Objetivo do projeto

Este projeto foi desenvolvido para praticar:

Análise de dados com Pandas

Criação de dashboards interativos

Visualização de dados com Plotly

Organização de código em arquitetura modular

Boas práticas de interface para dashboards

👨‍💻 Autor

Projeto desenvolvido por Gabriel Soriano durante a Imersão Dados + Python Alura (2026).