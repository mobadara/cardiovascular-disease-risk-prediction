from pydantic import BaseModel

class PredictionInput(BaseModel):
    age: int
    gender: str
    height: int
    cholesterol: str
    gluc: str
    smoke: str
    alco: str
    active: str
    bmi: float
    age_group: str
    blood_pressure_category: str
    pulse_pressure: int
           
