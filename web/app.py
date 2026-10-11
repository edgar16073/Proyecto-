import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Analítica", layout="wide")
st.title("📊 Panel de Control y Analítica")

# Datos de prueba para verificar visualización
data = {
    "Categoría": ["Segmento A", "Segmento B", "Segmento C", "Segmento D"],
    "Total": [45, 25, 20, 10]
}
df = pd.DataFrame(data)

col1, col2 = st.columns(2)

with col1:
    fig_bar = px.bar(df, x="Categoría", y="Total", title="Distribución por Categorías", color="Categoría")
    st.plotly_chart(fig_bar, use_container_width=True)

with col2:
    fig_pie = px.pie(df, names="Categoría", values="Total", title="Proporción General")
    st.plotly_chart(fig_pie, use_container_width=True)
