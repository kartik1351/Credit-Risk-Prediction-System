from fastapi import FastAPI
from pydantic import BaseModel

import numpy as np
import joblib

# Load files
model = joblib.load("models/model.pkl")

scaler = joblib.load("models/scaler.pkl")

# Initialize FastAPI
app = FastAPI(
    title="Credit Risk Prediction API"
)

# Input Schema
class Applicant(BaseModel):

    person_age: float
    person_income: float
    person_home_ownership: int
    person_emp_length: float
    loan_intent: int
    loan_amnt: float
    loan_int_rate: float
    loan_percent_income: float
    cb_person_default_on_file: int
    cb_person_cred_hist_length: float

# Home Route
@app.get("/")
def home():

    return {
        "message":
        "Credit Risk Prediction API Running"
    }

# Prediction Route
@app.post("/predict")
def predict(data: Applicant):

    # Convert input into array
    features = np.array([[
        data.person_age,
        data.person_income,
        data.person_home_ownership,
        data.person_emp_length,
        data.loan_intent,
        data.loan_amnt,
        data.loan_int_rate,
        data.loan_percent_income,
        data.cb_person_default_on_file,
        data.cb_person_cred_hist_length
    ]])

    # Scale features
    scaled_data = scaler.transform(features)

    # Prediction
    prediction = model.predict(scaled_data)[0]

    # Probability
    probability = model.predict_proba(
        scaled_data
    )[0][1]

    # Result
    if prediction == 1:
        risk = "High Risk"
    else:
        risk = "Low Risk"

    return {

        "Prediction": int(prediction),

        "Risk Level": risk,

        "Default Probability":
            round(float(probability), 4)
    }