import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load("models/model.pkl")
scaler = joblib.load("models/scaler.pkl")

# Title
st.title("🏦 Credit Risk Prediction System")

st.write("Enter Applicant Details")

# Inputs
person_age = st.number_input(
    "Person Age",
    min_value=18,
    max_value=100,
    value=25
)

person_income = st.number_input(
    "Person Income",
    value=50000
)

person_home_ownership = st.selectbox(
    "Home Ownership",
    [0,1,2,3]
)

person_emp_length = st.number_input(
    "Employment Length",
    value=2
)

loan_intent = st.selectbox(
    "Loan Intent",
    [0,1,2,3,4,5]
)

loan_grade = st.selectbox(
    "Loan Grade",
    [0,1,2,3,4,5,6]
)

loan_amnt = st.number_input(
    "Loan Amount",
    value=10000
)

loan_int_rate = st.number_input(
    "Interest Rate",
    value=12.5
)

loan_percent_income = st.number_input(
    "Loan Percent Income",
    value=0.20
)

cb_person_default_on_file = st.selectbox(
    "Previous Default",
    [0,1]
)

cb_person_cred_hist_length = st.number_input(
    "Credit History Length",
    value=5
)

# Prediction Button
if st.button("Predict Risk"):

    features = np.array([[

        person_age,
        person_income,
        person_home_ownership,
        person_emp_length,
        loan_intent,
        loan_grade,
        loan_amnt,
        loan_int_rate,
        loan_percent_income,
        cb_person_default_on_file,
        cb_person_cred_hist_length

    ]])

    # Scale features
    scaled_data = scaler.transform(features)

    # Prediction
    prediction = model.predict(scaled_data)[0]

    # Probability
    probability = model.predict_proba(
        scaled_data
    )[0][1]

    # Output
    st.subheader("Prediction Result")

    if prediction == 1:

        st.error("⚠️ High Risk Applicant")

    else:

        st.success("✅ Low Risk Applicant")

    st.write(
        f"Default Probability: {probability:.2f}"
    )