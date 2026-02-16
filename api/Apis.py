import pandas as pd
import pickle
import numpy as np
import tensorflow as tf

class api:
    def __init__(self):

        self.gradedmodel = tf.keras.models.load_model("models/model1.h5",compile=False)
        self.riskmodel = tf.keras.models.load_model("models/modelo_clasificacion_riesgo.keras",compile=False)

        #cargar los scaler y las columnas

        with open("models/scaler.pkl", "rb") as f:
            self.scaler = pickle.load(f)

        with open("models/columns.pkl", "rb") as f:
            self.columns = pickle.load(f)

        #Se guardan los valores de las ausencias maximas
        with open("models/max_absences.pkl", "rb") as f:
            self.max_absences = pickle.load(f)
    def preprocesamiento(self,data: dict):
        df = pd.DataFrame([data])

        df['avg_prev_grades'] = (df['G1'] + df['G2']) / 2
        df['absence_rate'] = df['absences']/self.max_absences if self.max_absences > 0 else 0

        df =pd.get_dummies(df, columns=['Mjob','Fjob','reason','guardian'])

        #Reordenamiento de columnas
        df = df.reindex(columns=self.columns, fill_value=0)

        #escalamiento
        df_escalar = self.scaler.transform(df)
        return df_escalar

    def pred_grade(self,data: dict):
        ft = self.preprocesamiento(data)
        prediccion = self.gradedmodel.predict(ft)
        pred_value = float(prediccion[0][0])
        return pred_value#{"Predicciones_graded": pred_value}

    def pred_risk(self,data: dict):
        ft = self.preprocesamiento(data)
        prediccion = self.riskmodel.predict(ft)

        indice = int(np.argmax(prediccion))
        risk_labels = {
            0:"Sin riesgo",
            1:"Riesgo bajo",
            2:"Riesgo medio",
            3:"Riesgo alto"
        }

        if indice == 1:
            alerta = "Intervención sugerida"
        elif indice == 2:
            alerta = "Intervención recomendada"
        elif indice == 3:
            alerta = "Intervención urgente"
        else:
            alerta = None

        return {
            "Nivelderiesgo": risk_labels[indice],
            "Confianza": round(float(np.max(prediccion)), 2),
            "Alerta": alerta
        }
        #return {
            #"Nivelderiesgo": risk_labels[indice],
            #"Confianza": round(float(np.max(prediccion)),2),
            #"Alerta": "Intervención recomendada" if indice >= 2 else None
            #"Alerta": "Intervención recomendada" if indice == 2 else "Intervención urgente" if indice == 3 else None
        #}