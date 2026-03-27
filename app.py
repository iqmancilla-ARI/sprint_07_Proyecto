import os
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Leer el archivo csv
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE_DIR, 'vehicles_us.csv'))

# Encabezado de la aplicación
st.header('Análisis de Vehículos en Estados Unidos')

# Checkboxes
mostrar_histograma = st.checkbox('Mostrar Histograma de Años')
mostrar_dispersion = st.checkbox(
    'Mostrar Gráfico de Dispersión: Precio vs. Odómetro')

# Histograma
if mostrar_histograma:
    with st.spinner('Construyendo histograma...'):
        fig = go.Figure(data=[go.Histogram(x=df['model_year'], nbinsx=20)])
        fig.update_layout(
            title='Histograma de Años de Vehículos',
            xaxis_title='Año',
            yaxis_title='Frecuencia',
            bargap=0.2
        )
        st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersión
if mostrar_dispersion:
    with st.spinner('Construyendo gráfico de dispersión...'):
        fig = go.Figure(data=go.Scatter(
            x=df['odometer'], y=df['price'], mode='markers'
        ))
        fig.update_layout(
            title='Gráfico de Dispersión: Precio vs. Odómetro',
            xaxis_title='Odómetro (millas)',
            yaxis_title='Precio',
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
