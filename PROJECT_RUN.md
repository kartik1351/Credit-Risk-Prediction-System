# Project Run Instructions

## Step 1: Create Virtual Environment

```bash
python -m venv venv
```

## Step 2: Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## Step 3: Install Required Libraries

```bash
pip install fastapi uvicorn streamlit numpy pandas scikit-learn joblib
```

## Step 4: Verify Project Structure

Ensure the following files exist:

```text
app.py
streamlit_app.py
models/
    model.pkl
    scaler.pkl
    label_encoders.pkl
```

---

# Running FastAPI Application

## Start API Server

```bash
uvicorn app:app --reload
```

Server will start at:

```text
http://127.0.0.1:8000
```

## API Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

Interactive Swagger documentation will be available.

---

# Running Streamlit Application

## Start Streamlit

```bash
streamlit run streamlit_app.py
```

Application will open automatically in the browser.

Default URL:

```text
http://localhost:8501
```

---

# Testing Prediction API

Example Request:

```json
{
  "person_age": 25,
  "person_income": 50000,
  "person_home_ownership": 1,
  "person_emp_length": 2,
  "loan_intent": 3,
  "loan_amnt": 10000,
  "loan_int_rate": 12.5,
  "loan_percent_income": 0.20,
  "cb_person_default_on_file": 0,
  "cb_person_cred_hist_length": 5
}
```

The API will return:

```json
{
  "Prediction": 0,
  "Risk Level": "Low Risk",
  "Default Probability": 0.12
}
```

---

# Stop Application

Press:

```text
CTRL + C
```

to stop FastAPI or Streamlit servers.

## Author

Kartik
