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
├── data/
│   └── cardio-train.csv           # The dataset used for training
├── notebooks/
│   └── exploratory-data-analysis.ipynb # Notebook for EDA
│   └── model-training.ipynb        # Notebook for model training and evaluation
├── src/
│   ├── main.py                     # FastAPI application
│   └── models/                     # Pydantic models for API input/output
│   │   └── prediction-input.py
│   │   └── prediction-output.py
│   └── ml_model/                   # Contains the trained ML model and related utilities
│       ├── model.pkl
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

-   `/predict`: Accepts a JSON payload of patient features and returns the predicted risk.

### Example Request

```json
{
  "age": 50,
  "gender": 2,
  "height": 170,
  "weight": 70.0,
  "ap_hi": 120,
  "ap_lo": 80,
  "cholesterol": 1,
  "gluc": 1,
  "smoke": 0,
  "alco": 0,
  "active": 1
}

