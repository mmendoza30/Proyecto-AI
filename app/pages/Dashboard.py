import streamlit as st
import requests
from PIL import Image

st.sidebar.title("Menú")
opciones = st.sidebar.radio("Selecciona una opción", ["Predicciones","Comparaciones de los modelos","Acerca del proyecto"])

col1,col2 = st.columns([1,3])
img = Image.open("app/img/educacion-futuro-696x464-1.jpg")
col1.image(img, width=150)
col2.title("Sistema de predicciones academicas")

if opciones == "Predicciones":
    with st.form("form"):

        age = st.slider("Edad", 15,25,15)
        studytime = st.selectbox("Horas de estudio",[1,2,3,4])
        failures = st.slider("Cantidad de reprobaciones",0,4,0)
        absences = st.slider("Cantidad de ausencias",0,50,5)
        G1 = st.slider("Nota del primer trimestre",0,20,0)
        G2 = st.slider("Nota del segundo trimestre",0,20,0)

        #Diccionarios para traduccion
        #Mjob = st.selectbox("Trabajo madre", ["teacher", "health", "services", "at_home", "other"])
        #Fjob = st.selectbox("Trabajo padre", ["teacher", "health", "services", "at_home", "other"])
        #reason = st.selectbox("Razón escuela", ["home", "reputation", "course", "other"])
        #guardian = st.selectbox("Tutor", ["mother", "father", "other"])

        # Diccionarios de traducción
        Mjob_options = {
            "Maestra": "teacher",
            "Salud": "health",
            "Servicios": "services",
            "Ama de casa": "at_home",
            "Otro": "other"
        }

        Fjob_options = {
            "Maestro": "teacher",
            "Salud": "health",
            "Servicios": "services",
            "Amo de casa": "at_home",
            "Otro": "other"
        }

        reason_options = {
            "Casa": "home",
            "Reputación": "reputation",
            "Curso": "course",
            "Otro": "other"
        }

        guardian_options = {
            "Madre": "mother",
            "Padre": "father",
            "Otro": "other"
        }

        Mjob_es = st.selectbox("Trabajo madre", list(Mjob_options.keys()))
        Fjob_es = st.selectbox("Trabajo padre", list(Fjob_options.keys()))
        reason_es = st.selectbox("Razón escuela", list(reason_options.keys()))
        guardian_es = st.selectbox("Tutor", list(guardian_options.keys()))

        # Convertir a inglés para el API
        Mjob_api = Mjob_options[Mjob_es]
        Fjob_api = Fjob_options[Fjob_es]
        reason_api = reason_options[reason_es]
        guardian_api = guardian_options[guardian_es]

        submit = st.form_submit_button("Predecir")

        if submit:
            data = {"age": age,
                    "studytime": studytime,
                    "failures": failures,
                    "absences": absences,
                    "G1": G1,
                    "G2": G2,
                    "Mjob": Mjob_es,
                    "Fjob": Fjob_es,
                    "reason": reason_es,
                    "guardian": guardian_api
            }
            #Llamar al api
            #grade = requests.post("http://localhost:8080/predict/graded", json=data).json()
            grade = requests.post("http://localhost:8080/predict/graded", json=data)
            print(grade.text)
            grade = grade.json()

            #risk = requests.post("http://localhost:8080/predict/risk_level", json=data).json()
            risk = requests.post("http://localhost:8080/predict/risk_level", json=data)
            print(risk.text)
            risk = risk.json()
            #st.metric("Nota predicha", grade["Predicciones_graded"])
            st.metric("Nota predicha", round(grade["Predicciones_graded"], 2))
            st.metric("Riesgo", risk["Nivelderiesgo"])
            st.metric("Confianza", risk["Confianza"])

            if risk["Alerta"]:
                st.error(risk["Alerta"])

elif opciones == "Comparaciones de los modelos":
    st.info("Comparaciones de los modelos prontooooo")

elif opciones == "Acerca del proyecto":
    st.info("Acerca del proyecto")