
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
        best_model = model.best_estimator_ if hasattr(model, 'best_estimator_') else model
        best_model_ = best_model.named_steps['classifier'] if 'classifier' in best_model.named_steps else best_model
        predictions = best_model.predict(df)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'prediction': predictions.tolist(),
            'prediction_proba': model.predict_proba(df).tolist(),
            'columns': df.columns.tolist(),
            'feature_names_out': best_model_.get_feature_names_out().tolist() if hasattr(best_model_, 'get_feature_names_out') else [],
            'n_features_out': best_model_.n_features_out_ if hasattr(best_model_, 'n_features_out_') else None,
            'feature_importances': best_model_.feature_importances_.tolist(),
            'n_features_in': best_model_.n_features_in_,
            'classes': best_model_.classes_.tolist(),
            'n_classes': best_model_.n_classes_,
            'model_type': str(type(best_model_)),
            'model': str(best_model_),
            'model_version': '1.0.0'
            }