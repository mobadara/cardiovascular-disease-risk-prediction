
import pandas as pd
from fastapi import APIRouter, HTTPException
from typing import List
from .. schemas import PredictionInput
from . preprocess import load_model

router = APIRouter()

@router.post('/predict')
async def predict(input_data: List[PredictionInput]):
    try:
        if not input_data:
            raise HTTPException(status_code=400, detail="Input data cannot be empty.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    try:
        model = load_model('src/models/model.pkl')
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Model file not found.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    input_data_ = [data.model_dump() for data in input_data]
    df = pd.DataFrame(input_data_, index=range(1, len(input_data_) + 1))
    print(df)
    
    try:
        predictions = model.predict(df)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'prediction': predictions.tolist()}