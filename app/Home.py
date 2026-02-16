import streamlit as st
from PIL import Image

st.set_page_config(page_title="Sistema Predicciones Académicas", layout="wide")

st.sidebar.title("Menú")
#opcion = st.sidebar.radio("Opciones", ["Predicciones", "Comparaciones de los modelos", "Acerca del proyecto"])

col1, col2 = st.columns([1, 4])
img = Image.open("app/img/educacion-futuro-696x464-1.jpg")
col1.image(img, width=150)
col2.title("Sistema de predicciones académicas")

st.write("Selecciona una opción en el menú")
