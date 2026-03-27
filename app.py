import os
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title='Análisis de Vehículos — EE.UU.',
    layout='wide'
)

# ── Estilo Blueprint ──────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@400;700&display=swap');

/* Fondo blueprint */
[data-testid="stAppViewContainer"] {
    background-color: #0a1628;
    background-image:
        linear-gradient(rgba(100,160,255,0.07) 1px, transparent 1px),
        linear-gradient(90deg, rgba(100,160,255,0.07) 1px, transparent 1px),
        linear-gradient(rgba(100,160,255,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(100,160,255,0.03) 1px, transparent 1px);
    background-size: 100px 100px, 100px 100px, 20px 20px, 20px 20px;
    font-family: 'Share Tech Mono', monospace;
}

[data-testid="stHeader"] { background: transparent; }
[data-testid="stSidebar"] { background-color: #060f1e; }

/* Títulos */
h1, h2, h3 {
    font-family: 'Orbitron', monospace !important;
    color: #4da6ff !important;
    text-shadow: 0 0 20px rgba(77,166,255,0.4);
    letter-spacing: 2px;
}

/* Botones */
.stButton > button {
    background-color: transparent;
    border: 1px solid #4da6ff;
    color: #4da6ff;
    font-family: 'Share Tech Mono', monospace;
    letter-spacing: 1px;
    transition: all 0.2s ease;
    white-space: nowrap;!important;
    width: 100% !important;
}
.stButton > button:hover {
    background-color: rgba(77,166,255,0.15);
    border-color: #80bfff;
    color: #80bfff;
    box-shadow: 0 0 12px rgba(77,166,255,0.3);
}

/* Texto general */
p, div, label, span {
    color: #a0c4ff !important;
    font-family: 'Share Tech Mono', monospace !important;
}
</style>
""", unsafe_allow_html=True)

# ── Datos ─────────────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE_DIR, 'vehicles_us.csv'))

# ── Paleta blueprint para gráficos ────────────────────────────────────────────
BLUEPRINT_LAYOUT = dict(
    paper_bgcolor='rgba(10,22,40,0.9)',
    plot_bgcolor='rgba(10,22,40,0.9)',
    font=dict(color='#a0c4ff', family='Share Tech Mono'),
    xaxis=dict(gridcolor='rgba(77,166,255,0.15)', linecolor='#4da6ff'),
    yaxis=dict(gridcolor='rgba(77,166,255,0.15)', linecolor='#4da6ff'),
)

# ── Encabezado ────────────────────────────────────────────────────────────────
st.header('[ ANÁLISIS DE VEHÍCULOS — EE.UU. ]')
st.markdown('---')

# ── Session state para limpiar pantalla ──────────────────────────────────────
if 'mostrar_hist_anio' not in st.session_state:
    st.session_state.mostrar_hist_anio = False
if 'mostrar_hist_modelo' not in st.session_state:
    st.session_state.mostrar_hist_modelo = False
if 'mostrar_dispersion' not in st.session_state:
    st.session_state.mostrar_dispersion = False

# ── Botones principales ───────────────────────────────────────────────────────
col1, col2, col3 = st.columns([3, 4, 2])

with col1:
    if st.button('▶ HISTOGRAMA'):
        st.session_state.mostrar_hist_anio = True
        st.session_state.mostrar_hist_modelo = False

with col2:
    if st.button('▶ DISPERSIÓN: PRECIO vs ODÓMETRO'):
        st.session_state.mostrar_dispersion = True

with col3:
    if st.button('✕ LIMPIAR'):
        st.session_state.mostrar_hist_anio = False
        st.session_state.mostrar_hist_modelo = False
        st.session_state.mostrar_dispersion = False

# ── Histograma por año ────────────────────────────────────────────────────────
if st.session_state.mostrar_hist_anio:
    st.markdown('##### DISTRIBUCIÓN POR AÑO')

    # Sub-botón: histograma por modelo
    if st.button('   ↳ VER POR MODELO'):
        st.session_state.mostrar_hist_modelo = True

    with st.spinner('Generando histograma...'):
        fig = go.Figure(data=[go.Histogram(
            x=df['model_year'],
            nbinsx=20,
            marker_color='#4da6ff',
            marker_line_color='#0a1628',
            marker_line_width=1,
            opacity=0.85
        )])
        fig.update_layout(
            title='Histograma — Año de Fabricación',
            xaxis_title='Año',
            yaxis_title='Frecuencia',
            bargap=0.2,
            **BLUEPRINT_LAYOUT
        )
        st.plotly_chart(fig, use_container_width=True)

# ── Histograma por modelo ─────────────────────────────────────────────────────
if st.session_state.mostrar_hist_modelo:
    st.markdown('##### DISTRIBUCIÓN POR MODELO (TOP 20)')
    with st.spinner('Generando histograma por modelo...'):
        top_modelos = df['model'].value_counts().nlargest(20)
        fig2 = go.Figure(data=[go.Bar(
            x=top_modelos.index,
            y=top_modelos.values,
            marker_color='#4da6ff',
            marker_line_color='#0a1628',
            marker_line_width=1,
            opacity=0.85
        )])
        fig2.update_layout(
            title='Histograma — Top 20 Modelos',
            xaxis_title='Modelo',
            yaxis_title='Frecuencia',
            bargap=0.2,
            **BLUEPRINT_LAYOUT
        )
        st.plotly_chart(fig2, use_container_width=True)

# ── Gráfico de dispersión ─────────────────────────────────────────────────────
if st.session_state.mostrar_dispersion:
    st.markdown('##### PRECIO vs. ODÓMETRO')
    with st.spinner('Generando gráfico de dispersión...'):
        fig3 = go.Figure(data=go.Scatter(
            x=df['odometer'],
            y=df['price'],
            mode='markers',
            marker=dict(
                color='#4da6ff',
                size=4,
                opacity=0.5,
                line=dict(width=0)
            )
        ))
        fig3.update_layout(
            title='Dispersión — Precio vs. Odómetro',
            xaxis_title='Odómetro (millas)',
            yaxis_title='Precio (USD)',
            showlegend=False,
            **BLUEPRINT_LAYOUT
        )
        st.plotly_chart(fig3, use_container_width=True)
