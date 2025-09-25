import joblib
from typing import Any


def load_model(model_path) -> Any:
    """
    Load a machine learning model from a pickle file.
    
    Args:
        model_path (str): Path to the pickle file containing the model.
    
    Returns:
        model (Any) : The loaded machine learning model.
        
    Raises:
        FileNotFoundError: If the specified model file does not exist.
        Exception: For any other issues that arise during model loading.
    """
    model = joblib.load(model_path)
    return model
