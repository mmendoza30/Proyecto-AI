import streamlit as st
from PIL import Image

st.set_page_config(page_title="Sistema Predicciones Académicas", layout="wide")

#st.sidebar.title("Menú")
#opcion = st.sidebar.radio("Opciones", ["Predicciones", "Comparaciones de los modelos", "Acerca del proyecto"])

col1, col2 = st.columns([1, 4])
img = Image.open("app/img/educacion-futuro-696x464-1.jpg")
col1.image(img, width=150)
col2.title("Sistema de predicciones académicas")

st.markdown("""
### Objetivo

Este sistema ha sido desarrollado con el objetivo de predecir el desempeño académico de los estudiantes y detectar de manera temprana el riesgo de deserción escolar mediante el uso de modelos de Inteligencia Artificial.

A partir de variables académicas, sociales y demográficas, la plataforma permite estimar la nota final esperada y clasificar el nivel de riesgo, generando alertas tempranas que facilitan la implementación de intervenciones educativas oportunas.""")

st.markdown("""
### Creado por:

-Victor Rojas Navarro

-Wedell Orozco Gonzalez

-Mónica Mendoza Morales
""")