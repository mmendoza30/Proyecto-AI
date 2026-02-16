import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Comparación de Modelos", layout="wide")

st.title("Comparación de Modelos")
st.image("app/img/comparativa.png", width=300)
st.subheader("Sistema de Predicción de Rendimiento Académico")

st.markdown("""
### Resultados obtenidos

**Modelo 1 - Regresión**
- Objetivo: Predecir calificación final G3 (0-20)
- Arquitectura: ANN con Dense + Dropout
- Loss: MSE
- Optimizer: Adam
- MAE: 1.5431
- Error Relativo: 14.35%

**Modelo 2 - Clasificación -Multiclase**
- Objetivo: Clasificar nivel de riesgo académico
- Arquitectura: ANN con Dense + Dropout
- Loss: Categorical Crossentropy
- Optimizer: Adam
- Accuracy: 76.56%
- Número de clases: 4
""")

st.divider()

#Comparativa

st.subheader("Tabla Comparativa")

comparacion = pd.DataFrame({
    "Modelo": ["Modelo 1 - Regresión", "Modelo 2 - Clasificación - Multiclase"],
    "Tipo": ["Regresión", "Clasificación Multiclase"],
    "Variable Objetivo": ["Nota Final (G3)", "Nivel de Riesgo Académico"],
    "Métrica Principal": ["MAE", "Accuracy"],
    "Resultado": [1.5431, 0.7656]
})
st.dataframe(comparacion, use_container_width=True)
st.divider()

#Visualizaciones
st.subheader("Visualización Comparativa")

modelos = ["Regresión (MAE)", "Clasificación (Accuracy)"]
valores = [1.5431, 0.7656]

fig, ax = plt.subplots()
ax.bar(modelos, valores)
ax.set_title("Comparación de Desempeño de Modelos")
ax.set_ylabel("Valor de Métrica")

st.pyplot(fig)
st.divider()

st.subheader("Interpretación de Resultados")

st.markdown("""
### Modelo 1 - Regresión
El modelo presenta un MAE de **1.5431** puntos sobre una escala de 0 a 20.  
Esto indica que, en promedio, la predicción se desvía aproximadamente 1.5 puntos de la nota real.  
El error relativo del **14.35%** demuestra un buen desempeño predictivo.

### Modelo 2 - Clasificación
El modelo alcanza una precisión del **76.56%** en la clasificación de estudiantes en cuatro niveles de riesgo.  
Esto significa que aproximadamente 77 de cada 100 estudiantes son correctamente clasificados.
""")

st.divider()
st.subheader("Conclusión Final")

st.markdown("""
El **Modelo 1** mostró una alta precisión numérica en la predicción de la nota final (G3), con un bajo error promedio.
El **Modelo 2** logró una buena capacidad de clasificación, permitiendo identificar estudiantes en diferentes niveles de riesgo académico.
Si el objetivo es obtener una predicción exacta de la calificación final, el modelo de regresión es el más adecuado.
Sin embargo, desde una perspectiva práctica y educativa, el modelo de clasificación es más útil, ya que permite detectar estudiantes en riesgo y tomar decisiones preventivas.
Ambos modelos demuestran que las Redes Neuronales Artificiales son herramientas efectivas para el análisis predictivo en el ámbito educativo.
""")