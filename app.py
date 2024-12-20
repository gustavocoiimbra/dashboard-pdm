from google.cloud import bigquery
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configurando o cliente BigQuery
client = bigquery.Client()

# Queries
dist_cidade = "SELECT * FROM projeto_final_pdm.distribuicao_cidade_gold_layer"
estatisticas = "SELECT * FROM projeto_final_pdm.estatisticas_tipo_gold_layer"
anunciantes = "SELECT * FROM projeto_final_pdm.imoveis_anunciante_gold_layer"

# Obtendo os DataFrames
df_cidade = client.query(dist_cidade).to_dataframe()
df_estatisticas = client.query(estatisticas).to_dataframe()
df_anunciantes = client.query(anunciantes).to_dataframe()

# Função principal do dashboard
if __name__ == "__main__":
    st.title("Dashboard Imobiliário")
    st.markdown("### Visualize as informações do mercado imobiliário com dados atualizados.")

    # Container para distribuição por cidade
    st.header("Distribuição de Imóveis por Cidade")
    cidade = st.selectbox("Selecione uma cidade:", df_cidade["cidade"].unique())
    filtro_cidade = df_cidade[df_cidade["cidade"] == cidade]

    # Gráfico de barra
    st.subheader(f"Distribuição de imóveis em {cidade}")
    st.bar_chart(filtro_cidade.set_index("cidade")["count"])

    # Estatísticas básicas
    st.header("Estatísticas por Tipo de Imóvel")
    st.write("### Estatísticas dos imóveis (Preço e Área)")
    estatisticas_not_mim = df_estatisticas.drop(columns=["preco_min"])
    st.dataframe(estatisticas_not_mim)

   # Container para análise de anunciantes
    st.header("Análise por Anunciantes")
    top_anunciantes = df_anunciantes.nlargest(10, "quantidade_imoveis")  # Top 10 anunciantes por quantidade

    # Ajustando o tamanho das colunas
    col1, col2 = st.columns([2, 2])  # Proporções aumentadas para expandir as colunas

    # Gráficos nos containers
    with col1:
        st.subheader("Top 10 Anunciantes - Quantidade de Imóveis")
        fig, ax = plt.subplots(figsize=(8, 6))  # Aumentando também o tamanho do gráfico
        ax.barh(top_anunciantes["anunciante"], top_anunciantes["quantidade_imoveis"], color="skyblue")
        ax.set_xlabel("Quantidade de Imóveis")
        ax.set_ylabel("Anunciante")
        ax.set_title("Top 10 Anunciantes")
        st.pyplot(fig)

    with col2:
        st.subheader("Preço Médio por Anunciante")
        fig2, ax2 = plt.subplots(figsize=(8, 6))  # Tamanho ajustado
        ax2.bar(top_anunciantes["anunciante"], top_anunciantes["media_preco"], color="orange")
        ax2.set_ylabel("Preço Médio (R$)")
        ax2.set_xticklabels(top_anunciantes["anunciante"], rotation=45, ha='right')  # Rotação das labels
        ax2.set_title("Preço Médio por Anunciante")
        st.pyplot(fig2)
        # Footer com uma mensagem de conclusão
    # st.markdown("Desenvolvido com 💙 usando Streamlit e BigQuery.")