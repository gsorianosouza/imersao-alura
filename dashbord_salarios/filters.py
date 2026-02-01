import streamlit as st

def criar_filtros(df):
    st.sidebar.header("🔍 Filtros")

    anos = st.sidebar.multiselect("Ano", sorted(df['ano'].unique()), default=sorted(df['ano'].unique()))
    senioridade = st.sidebar.multiselect("Senioridade", sorted(df['senioridade'].unique()), default=sorted(df['senioridade'].unique()))
    contrato = st.sidebar.multiselect("Contrato", sorted(df['contrato'].unique()), default=sorted(df['contrato'].unique()))
    tamanho = st.sidebar.multiselect("Empresa", sorted(df['tamanho_empresa'].unique()), default=sorted(df['tamanho_empresa'].unique()))

    return df[
        df['ano'].isin(anos) &
        df['senioridade'].isin(senioridade) &
        df['contrato'].isin(contrato) &
        df['tamanho_empresa'].isin(tamanho)
    ]