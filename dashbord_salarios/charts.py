import plotly.express as px
from styles import AMARELO, LARANJA, VERMELHO, PRETO

def estilo_grafico(fig):
    fig.update_layout(
        plot_bgcolor=PRETO,
        paper_bgcolor=PRETO,
        font_color=AMARELO,
        margin=dict(l=40, r=40, t=60, b=40),
    )
    return fig

def grafico_top_cargos(df):
    dados = df.groupby('cargo')['usd'].mean().nlargest(10).sort_values().reset_index()
    fig = px.bar(dados, x='usd', y='cargo', orientation='h', title="Top 10 cargos")
    fig.update_traces(marker_color=LARANJA)
    return estilo_grafico(fig)

def grafico_distribuicao(df):
    fig = px.histogram(df, x='usd', nbins=30, title="Distribuição de salários")
    fig.update_traces(marker_color=VERMELHO)
    return estilo_grafico(fig)

def grafico_tipos_trabalho(df):
    remoto = df['remoto'].value_counts().reset_index()
    remoto.columns = ['tipo', 'qtd']
    fig = px.pie(remoto, names='tipo', values='qtd', hole=0.5)
    fig.update_traces(marker=dict(colors=[AMARELO, LARANJA, VERMELHO]))
    return estilo_grafico(fig)

def grafico_salario_pais(df):
    df_ds = df[df['cargo'] == 'Data Scientist']
    media = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()
    fig = px.choropleth(media, locations='residencia_iso3', color='usd',
                        color_continuous_scale=[AMARELO, LARANJA, VERMELHO])
    return estilo_grafico(fig)