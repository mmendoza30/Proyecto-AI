from pydantic import BaseModel

class Estudiante(BaseModel):
    age: int
    studytime: int
    failures: int
    absences: int
    G1: float
    G2: float
    Mjob: str
    Fjob: str
    reason: str
    guardian: str