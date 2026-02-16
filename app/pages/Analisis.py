import streamlit as st
import pandas as pd
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT_DIR))

from src.data_prep import ProcesadoEDA

st.title("EDA")
st.subheader("Regresión con ANN (Predicción de G3)")

def load_data():
    return pd.read_csv('data/processed/student_performance.csv')

df = load_data()

st.write("Vista previa del dataset:")
st.dataframe(df.head())

# Procesado
procesado = ProcesadoEDA(df)

st.markdown("## Correlación")
corr = procesado.grafico_correlación()
st.pyplot(corr)

st.markdown("## Distribución de G3")
dist = procesado.grafico_distribucion("G3")
st.pyplot(dist)

st.markdown("## Boxplot Mjob vs G3")
mjob = procesado.grafico_boxplot("Mjob","G3")
st.pyplot(mjob)

st.markdown("## Boxplot Fjob vs G3")
fjob = procesado.grafico_boxplot("Fjob","G3")
st.pyplot(fjob)

st.markdown("## Boxplot Guardian vs G3")
guardian = procesado.grafico_boxplot("guardian","G3")
st.pyplot(guardian)
