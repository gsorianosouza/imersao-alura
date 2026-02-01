import streamlit as st

AMARELO = "#FACC15"
LARANJA = "#F59E0B"
VERMELHO = "#EF4444"
PRETO = "#000000"

def carregar_estilo():
    st.markdown(f"""
    <style>
    .stApp {{ background-color: #0E1117; }}
    section[data-testid="stSidebar"] {{ background-color: {PRETO}; }}
    span[data-baseweb="tag"] {{ background-color: {AMARELO}!important; color:black!important; }}
    h1, h2, h3 {{ color: {AMARELO}; }}

    div[data-testid="stMetric"],
    div[data-testid="stPlotlyChart"],
    div[data-testid="stDataFrame"] {{
        background: linear-gradient(145deg, #0a0a0a, #000);
        padding: 25px;
        border-radius: 18px;
        box-shadow: 0 10px 35px rgba(0,0,0,0.6);
        overflow:hidden;
    }}

    .js-plotly-plot {{ height: 500px !important; }}
    </style>
    """, unsafe_allow_html=True)