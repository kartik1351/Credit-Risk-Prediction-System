# Credit Risk Prediction System

## Overview

The Credit Risk Prediction System is a Machine Learning project that predicts whether a loan applicant is a high-risk or low-risk borrower based on personal and financial information.

The project provides:

* A Machine Learning model for credit risk prediction
* A FastAPI-based REST API
* A Streamlit web application for user interaction
* Probability-based risk assessment

## Features

* Predicts credit default risk
* Calculates default probability
* FastAPI backend for API access
* Streamlit frontend for easy usage
* Pre-trained Machine Learning model
* Scaled input processing for improved accuracy

## Project Structure

```text
Project No.1/
│
├── app.py                     # FastAPI application
├── streamlit_app.py           # Streamlit web application
├── Main.ipynb                 # Model training notebook
├── credit_risk_dataset.csv    # Dataset
│
├── models/
│   ├── model.pkl
│   ├── scaler.pkl
│   └── label_encoders.pkl
│
└── __pycache__/
```

## Technologies Used

* Python
* Scikit-Learn
* NumPy
* FastAPI
* Streamlit
* Joblib
* Pandas

## Input Features

* Person Age
* Person Income
* Home Ownership
* Employment Length
* Loan Intent
* Loan Amount
* Interest Rate
* Loan Percent Income
* Previous Default History
* Credit History Length

## Output

The system returns:

* Risk Classification (High Risk / Low Risk)
* Prediction Value
* Default Probability Score

## API Endpoint

### Home

```http
GET /
```

Returns API status.

### Prediction

```http
POST /predict
```

Accepts applicant details and returns risk prediction.

## Future Improvements

* Model retraining pipeline
* Advanced feature engineering
* User authentication
* Cloud deployment
* Dashboard analytics

## Author

Kartik
