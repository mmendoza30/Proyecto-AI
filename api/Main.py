from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.esquemas_api import Estudiante
from api.Apis import api

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = api()

@app.post("/predict/graded")

def predict_graded(estudiante: Estudiante):
    #return {"Predicciones_graded": model.pred_grade(estudiante.dict())}
    try:
        prediccion = model.pred_grade(estudiante.dict())
        return {"Predicciones_graded": prediccion}
    except Exception as e:
        return {"Error": str(e)}

@app.post("/predict/risk_level")
def predict_risk_level(estudiante: Estudiante):
    try:
        prediccion = model.pred_risk(estudiante.dict())
        return {
            "Nivelderiesgo" :prediccion["Nivelderiesgo"],
            "Confianza":prediccion["Confianza"],
            "Alerta":prediccion["Alerta"]
        }
    except Exception as e:
        return {"Error": str(e)}
