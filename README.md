<div align="center">

# 🛡️ RiskScan — Insurance Premium Predictor

**AI-powered insurance risk assessment built with FastAPI, Streamlit & Scikit-Learn**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-005571?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-2.0+-E92063?style=for-the-badge&logo=pydantic&logoColor=white)

<br>

A full-stack machine learning application that predicts an individual's **insurance premium risk category** — `Low`, `Medium`, or `High` — based on health, demographic, and financial inputs. The system combines a trained **Random Forest classifier** with a production-grade **REST API** and a sleek, dark-themed **web interface**.

</div>

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🤖 **ML-Powered Predictions** | Random Forest classifier trained on real insurance data with engineered features |
| ⚡ **FastAPI Backend** | High-performance async REST API with automatic OpenAPI/Swagger documentation |
| 🎨 **Premium UI** | Dark-themed Streamlit frontend with glassmorphism cards, gradient accents & micro-animations |
| 🔒 **Pydantic Validation** | Strict server-side input validation — invalid data is rejected with detailed 422 error responses |
| 🏗️ **Feature Engineering** | Automatic computation of BMI, age group, lifestyle risk score, and city tier from raw inputs |
| 🌐 **Environment Configurable** | `.env`-driven API URL binding for seamless local ↔ deployment switching |

---

## 🏛️ Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                         CLIENT (Browser)                        │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │              Streamlit Frontend (frontend.py)              │  │
│  │  • Text inputs for all fields (no client-side clamping)    │  │
│  │  • Sends raw JSON payload to backend                       │  │
│  │  • Renders prediction results or 422 validation errors     │  │
│  └──────────────────────────┬─────────────────────────────────┘  │
└─────────────────────────────┼────────────────────────────────────┘
                              │  POST /predict
                              │  JSON payload
                              ▼
┌──────────────────────────────────────────────────────────────────┐
│                    FastAPI Backend (app.py)                       │
│                                                                  │
│  ┌──────────────────┐    ┌─────────────────────────────────────┐ │
│  │  Pydantic Model   │    │         Feature Engineering         │ │
│  │  (UserInput)      │───▶│  • BMI = weight / height²           │ │
│  │                   │    │  • age_group (young/adult/mid/sr)   │ │
│  │  Validates:       │    │  • lifestyle_risk (low/medium/high) │ │
│  │  • age (1–119)    │    │  • city_tier (1 / 2 / 3)            │ │
│  │  • height (<2.5m) │    └──────────────┬──────────────────────┘ │
│  │  • weight (>0)    │                   │                        │
│  │  • income (>0)    │                   ▼                        │
│  │  • occupation ∈   │    ┌─────────────────────────────────────┐ │
│  │    valid set      │    │   Random Forest Model (model.pkl)   │ │
│  └──────────────────┘    │   Predicts: low / medium / high      │ │
│                           └──────────────┬──────────────────────┘ │
└──────────────────────────────────────────┼───────────────────────┘
                                           │
                                           ▼
                                   JSON Response
                            { "predicted_category": "low" }
```

---

## 🧠 Feature Engineering Pipeline

The Pydantic model doesn't just validate — it **computes derived features** via `@computed_field` that the ML model was trained on:

| Computed Feature | Logic | Values |
|---|---|---|
| **BMI** | `weight / height²` | Continuous float |
| **Age Group** | `<25` → young, `<45` → adult, `<60` → middle_aged, `60+` → senior | `young` · `adult` · `middle_aged` · `senior` |
| **Lifestyle Risk** | Smoker + BMI > 30 → high; Smoker OR BMI > 27 → medium; else → low | `low` · `medium` · `high` |
| **City Tier** | Tier 1 (metro) · Tier 2 (urban) · Tier 3 (other) | `1` · `2` · `3` |

The final feature vector sent to the model: `[bmi, age_group, lifestyle_risk, city_tier, income_lpa, occupation]`

---

## 🔒 Validation & Error Handling

All validation is enforced **server-side** through Pydantic. The frontend sends raw user input directly to the backend — no client-side filtering or clamping. This ensures that the single source of truth for data integrity is the `UserInput` Pydantic model.

**Pydantic Constraints:**

```python
age:        int    → gt=0, lt=120         # Must be 1–119
weight:     float  → gt=0                 # Must be positive
height:     float  → gt=0, lt=2.5         # Must be 0–2.5 meters
income_lpa: float  → gt=0                 # Must be positive
smoker:     bool                           # true / false
city:       str                            # Any city name
occupation: Literal → one of 7 valid jobs  # Enum-like constraint
```

**What happens with bad data:**

| Input | Backend Response |
|---|---|
| `age: "abc"` | `422` — Input should be a valid integer |
| `age: -5` | `422` — Input should be greater than 0 |
| `height: 3.0` | `422` — Input should be less than 2.5 |
| `occupation: "pilot"` | `422` — Input should be one of the allowed values |
| Valid data | `200` — `{ "predicted_category": "low" }` |

---

## 🛠️ Getting Started

### Prerequisites

- **Python 3.10+** installed on your system
- **pip** package manager

### 1 · Install Dependencies

```bash
pip install -r req.txt
```

### 2 · Configure Environment

Create a `.env` file in the project root (or use the existing one):

```env
API_URL=http://127.0.0.1:8000/predict
```

### 3 · Start the FastAPI Backend

```bash
uvicorn app:app --host 127.0.0.1 --port 8000 --reload
```

> The API is now live at `http://127.0.0.1:8000` with interactive docs at [`/docs`](http://127.0.0.1:8000/docs)

### 4 · Launch the Streamlit Frontend

Open a **second terminal** (keep the backend running):

```bash
streamlit run frontend.py
```

> Your browser will auto-open the RiskScan web app 🚀

---

## 🧪 Testing the API

### Via Swagger UI (Recommended)

FastAPI auto-generates interactive documentation:

1. Navigate to **http://127.0.0.1:8000/docs**
2. Expand the `POST /predict` endpoint
3. Click **"Try it out"**
4. Paste this sample payload:

```json
{
  "age": 30,
  "weight": 70,
  "height": 1.75,
  "income_lpa": 5.0,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

5. Click **Execute** — you'll see a `200` response with the predicted risk category

### Test Invalid Data

Try sending bad data to see Pydantic validation in action:

```json
{
  "age": -10,
  "weight": 0,
  "height": 5.0,
  "income_lpa": -1,
  "smoker": false,
  "city": "",
  "occupation": "astronaut"
}
```

> This returns `422 Unprocessable Entity` with detailed field-level error messages

---

## 📁 Project Structure

```
insurance_premium_prediction/
│
├── app.py                                    # FastAPI backend — API endpoint + Pydantic model
├── frontend.py                               # Streamlit frontend — dark-themed web UI
├── model.pkl                                 # Serialized Random Forest classifier
├── insurance_prediction_random_forest.ipynb   # Jupyter notebook — data cleaning & model training
├── insurance.csv                             # Source dataset used for training
├── req.txt                                   # Python dependencies
├── .env                                      # Environment config (API_URL)
└── .gitignore                                # Git ignore rules
```

---

## 🧰 Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **ML Model** | Scikit-Learn (Random Forest) | Classification of insurance risk categories |
| **Backend** | FastAPI + Uvicorn | High-performance async REST API |
| **Validation** | Pydantic v2 | Strict type checking + constraint enforcement |
| **Feature Engineering** | Pydantic `@computed_field` | Derives BMI, age group, lifestyle risk, city tier |
| **Data Processing** | Pandas | DataFrame construction for model input |
| **Frontend** | Streamlit | Interactive web UI with custom CSS |
| **Config** | python-dotenv | Environment variable management |
| **Serialization** | Pickle | Model persistence |

---

## 📝 License

This project is for educational and demonstration purposes.

---

<div align="center">
<br>

**Built with 🧠 Machine Learning · ⚡ FastAPI · 🎨 Streamlit**

</div>
