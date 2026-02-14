# Proyecto C: Sistema de Predicción de Rendimiento Académico

## 👥 Equipo
- **Integrante 1**: Victor Rojas Navarro
- **Integrante 2**: Wedell Orozco Gonzalez
- **Integrante 3**: Mónica Mendoza Morales

## 📋 Descripción del Proyecto
Sistema de IA para predecir el desempeño académico de estudiantes y detectar tempranamente riesgo de deserción, permitiendo implementar intervenciones educativas oportunas.

## 🎯 Objetivos
- Identificar factores que impactan el rendimiento académico
- Predecir calificaciones finales esperadas
- Clasificar estudiantes por nivel de riesgo académico
- Generar recomendaciones automáticas de intervención

## 📊 Dataset
- **Fuente**: Student Performance Dataset (UCI)
- **URL**: https://archive.ics.uci.edu/dataset/320/student+performance
- **Registros**: 649 estudiantes (matemáticas) + 382 (portugués)
- **Variables**: 33 (demográficas, sociales, escolares)
- **Variables principales**: edad, educación de padres, tiempo de estudio, faltas, actividades extracurriculares, apoyo familiar, calificaciones previas

## 🔧 Instalación

### Requisitos Previos
- Python 3.8+
- pip

### Pasos de Instalación
```bash
# 1. Navegar al proyecto
cd ProyectoC_RendimientoAcademico

# 2. Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Descargar dataset
python data/raw/download_data.py
```

## 🚀 Uso

### Notebooks (orden recomendado)
```bash
jupyter notebook notebooks/
```
1. `01_EDA_StudentPerformance.ipynb` - Análisis de factores académicos
2. `02_FeatureEngineering.ipynb` - Creación de variables derivadas
3. `03_ANN_GradePredictor.ipynb` - Predicción de calificaciones
4. `04_ANN_RiskClassifier.ipynb` - Clasificación de riesgo
5. `05_InterventionSystem.ipynb` - Sistema de recomendaciones

### Entrenar Modelos
```bash
python src/train/grade_predictor.py
python src/train/risk_classifier.py
```

### API
```bash
cd api
uvicorn main:app --reload
```
Documentación: http://localhost:8000/docs

### Frontend
```bash
cd app
streamlit run Home.py
```
Disponible en: http://localhost:8501

## 📁 Estructura del Proyecto
```
ProyectoC_RendimientoAcademico/
├── data/
│   ├── raw/download_data.py
│   └── processed/
├── notebooks/
│   ├── 01_EDA_StudentPerformance.ipynb
│   ├── 02_FeatureEngineering.ipynb
│   ├── 03_ANN_GradePredictor.ipynb
│   ├── 04_ANN_RiskClassifier.ipynb
│   └── 05_InterventionSystem.ipynb
├── src/
│   ├── data_prep.py
│   ├── config.py
│   └── train/
├── models/
├── api/
└── app/
```

## 🧪 Modelos Implementados

### Modelo 1: Predicción de Calificaciones (Regresión)
- **Objetivo**: Predecir calificación final (0-20)
- **Métricas**: MAE, MSE, RMSE, R²

### Modelo 2: Clasificación de Riesgo (Multiclase)
- **Objetivo**: Clasificar en 4 niveles
  - Sin riesgo (calificación esperada ≥ 15)
  - Riesgo bajo (12-14)
  - Riesgo medio (10-11)
  - Riesgo alto (<10)

## 🎯 Sistema de Intervenciones
El sistema genera recomendaciones personalizadas:
- **Riesgo alto**: Tutoría individualizada urgente
- **Riesgo medio**: Grupos de estudio, sesiones de refuerzo
- **Riesgo bajo**: Monitoreo preventivo
- **Sin riesgo**: Oportunidades de profundización

## 📊 Features Engineered
Variables derivadas creadas:
- Promedio de calificaciones previas
- Tasa de ausentismo
- Índice de apoyo familiar
- Ratio tiempo estudio/tiempo libre
- Score de motivación académica

## 🛠️ Tecnologías
- TensorFlow/Keras, Pandas, NumPy, Scikit-learn
- Matplotlib, Seaborn, Plotly
- FastAPI, Streamlit

## 📈 Aplicaciones Potenciales
- Sistema de alertas tempranas para instituciones educativas
- Herramienta de apoyo para orientadores académicos
- Dashboard para seguimiento de cohortes estudiantiles
- Base para políticas de apoyo académico personalizadas

---
**CUC - Inteligencia Artificial Aplicada - 2025**
