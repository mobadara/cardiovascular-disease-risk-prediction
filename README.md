# **Cardiovascular Disease Risk Prediction**

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0055D1?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)

## **Overview**

This project focuses on predicting the risk of cardiovascular disease based on patient data. It involves building a machine learning model and deploying it as a RESTful API using FastAPI. This allows users to input patient features and receive a prediction of their CVD risk.

## **Project Structure**

```python
├── datasets/
│   └── cardio-train.csv
├── references/
├── models/          # The dataset used for training
├── notebooks/
│   └── exploratory-data-analysis.ipynb # Notebook for EDA
│   └── model-training.ipynb        # Notebook for model training and evaluation
├── src/
│   ├── main.py                     # FastAPI application
│   └── models/                                      # Contains the trained ML model and related utilities
│       ├── model.pkl
|       |── predictions-input.py
|       |── predictions-output.py
│       └── preprocess.py
├── README.md
└── requirements.txt
```

## **Data Source**

The dataset used in this project is the "Cardiovascular Disease Dataset" available on Kaggle: [https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset).

## **Machine Learning Model**

- A classification model

## FastAPI Application

A FastAPI application (`src/main.py`) is built to serve the machine learning model. It provides an endpoint where users can send patient data as a JSON payload and receive a prediction of the cardiovascular disease risk.

### Endpoints

- `api/predict`: Accepts a JSON payload of patient features and returns the predicted risk.

### Example Request

```json
  {
    "age": 34,
    "gender": "Female",
    "height": 112,
    "cholesterol": "Well Above Normal",
    "gluc": "Normal",
    "smoke": "Yes",
    "alco": "Yes",
    "active": "Active",
    "bmi": 21.2,
    "age_group": "Senior",
    "blood_pressure_category": "Hypertension Stage 1",
    "pulse_pressure": 60
  }
  ```
### Access the API at:
[https://cardiovascular-disease-risk-prediction.onrender.com/docs/](https://cardiovascular-disease-risk-prediction.onrender.com/docs#/)


### Author
##### Twitter [@m_obadara](https://twitter.com/m_obadara)
##### LinkedIn [Muyiwa Obadara](https://linkedin.com/in/obadara-m)
