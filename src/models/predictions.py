
import pandas as pd
from fastapi import APIRouter
from typing import List
from .. schemas import PredictionInput
from . preprocess import load_model

router = APIRouter()
  
@router.post('/predict')
async def predict(input_data: List[PredictionInput]):
    model = load_model('src/models/model.pkl')
    input_data_ = [data.model_dump() for data in input_data]
    df = pd.DataFrame(input_data_, index=range(1, len(input_data_) + 1))
    print(df)
    predictions = model.predict(df)
    return {'prediction': predictions.tolist()}