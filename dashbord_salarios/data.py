import pandas as pd
import streamlit as st

@st.cache_data
def carregar_dados():
    return pd.read_csv("dados-imersao-final.csv")