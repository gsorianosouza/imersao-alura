import streamlit as st
from styles import carregar_estilo
from data import carregar_dados
from filters import criar_filtros
from charts import *

st.set_page_config("Dashboard de Salários", "📊", layout="wide")

carregar_estilo()
df = carregar_dados()
df_filtrado = criar_filtros(df)

st.title("🎲 Dashboard de Análise de Salários na Área de Dados")
st.markdown("Explore os dados salariais na área de dados nos últimos anos. Utilize os filtros à esquerda para refinar sua análise.")

st.subheader("Métricas gerais (Salário anual em USD)")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Salário médio", f"${df_filtrado['usd'].mean():,.0f}")
col2.metric("Salário máximo", f"${df_filtrado['usd'].max():,.0f}")
col3.metric("Registros", f"{df_filtrado.shape[0]:,}")
col4.metric("Cargo comum", df_filtrado["cargo"].mode()[0])

st.markdown("---")

opcao = st.radio("Escolha o gráfico",
                 ["Top cargos", "Distribuição", "Tipos trabalho", "Salário por país"],
                 horizontal=True)

if opcao == "Top cargos":
    st.plotly_chart(grafico_top_cargos(df_filtrado), use_container_width=True)
elif opcao == "Distribuição":
    st.plotly_chart(grafico_distribuicao(df_filtrado), use_container_width=True)
elif opcao == "Tipos trabalho":
    st.plotly_chart(grafico_tipos_trabalho(df_filtrado), use_container_width=True)
else:
    st.plotly_chart(grafico_salario_pais(df_filtrado), use_container_width=True)

st.subheader("Dados Detalhados")
st.dataframe(df_filtrado)