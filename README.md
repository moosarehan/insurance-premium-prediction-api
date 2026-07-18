<div align="center">

# 🛡️ RiskScan — Insurance Premium Predictor

**AI-powered insurance risk assessment built with FastAPI, Streamlit & Scikit-Learn**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-005571?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-2.0+-E92063?style=for-the-badge&logo=pydantic&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)

<br>

A full-stack machine learning application that predicts an individual's **insurance premium risk category** — `Low`, `Medium`, or `High` — based on health, demographic, and financial inputs. The system combines a trained **Random Forest classifier** with a production-grade **REST API** and a sleek, dark-themed **web interface**.

<br>

## 🚀 Live Demo

| Service | URL |
|---------|-----|
| 🎨 **Frontend** | [https://insurance-app-nv9j.onrender.com](https://insurance-app-nv9j.onrender.com) |
| ⚡ **API Docs** | [https://insurance-premium-prediction-api-euqj.onrender.com/docs](https://insurance-premium-prediction-api-euqj.onrender.com/docs) |

> ⚠️ App may take **30-50 seconds** to wake up on first visit (free tier sleep mode)

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
| 🐳 **Dockerized** | Fully containerized with separate Dockerfiles for API and Frontend |
| ☁️ **Cloud Deployed** | Deployed on Render with automatic deployments from GitHub |

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

## 🐳 Docker Setup

### Prerequisites
- **Docker Desktop** installed
- **Docker Compose** installed

### Project Structure
```
insurance_premium_prediction/
│
├── app.py                          # FastAPI backend
├── frontend.py                     # Streamlit frontend
├── Dockerfile                      # API Docker image
├── Dockerfile.frontend             # Frontend Docker image
├── docker-compose.yml              # Local orchestration
├── model/                          # ML model files
├── schema/                         # Pydantic schemas
├── config/                         # Config files
├── requirement.txt                 # Python dependencies
├── .env                            # Environment config (not committed)
└── .gitignore                      # Git ignore rules
```

### Run Locally with Docker Compose

**1 · Clone the repository:**
```bash
git clone https://github.com/moosarehan/insurance-premium-prediction-api.git
cd insurance-premium-prediction-api
```

**2 · Create `.env` file:**
```env
API_URL=http://api:8000/predict
```

**3 · Run with Docker Compose:**
```bash
docker-compose up
```

**4 · Access the app:**
- Frontend → `http://localhost:8501`
- API Docs → `http://localhost:8000/docs`

### Docker Images on DockerHub
| Image | Link |
|-------|------|
| API | `musarehan/insurance-premium-prediction-api` |
| Frontend | `musarehan/insurance-frontend` |

---

## ☁️ Deployment

### Deployed on Render

Both services are deployed on **Render** using Docker:

| Service | Dockerfile | URL |
|---------|------------|-----|
| API | `./Dockerfile` | `https://insurance-premium-prediction-api-euqj.onrender.com` |
| Frontend | `./Dockerfile.frontend` | `https://insurance-app-nv9j.onrender.com` |

### Deploy Your Own

**1 · Fork this repository**

**2 · Deploy API on Render:**
- New Web Service → Connect GitHub repo
- Language: `Docker`
- Dockerfile Path: `./Dockerfile`
- Instance Type: `Free`

**3 · Deploy Frontend on Render:**
- New Web Service → Connect GitHub repo
- Language: `Docker`
- Dockerfile Path: `./Dockerfile.frontend`
- Instance Type: `Free`
- Environment Variable: `API_URL=https://your-api-url.onrender.com/predict`

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

All validation is enforced **server-side** through Pydantic.

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

| Input | Backend Response |
|---|---|
| `age: "abc"` | `422` — Input should be a valid integer |
| `age: -5` | `422` — Input should be greater than 0 |
| `height: 3.0` | `422` — Input should be less than 2.5 |
| `occupation: "pilot"` | `422` — Input should be one of the allowed values |
| Valid data | `200` — `{ "predicted_category": "low" }` |

---

## 🛠️ Local Development (Without Docker)

### 1 · Install Dependencies
```bash
pip install -r requirement.txt
```

### 2 · Configure Environment
```env
API_URL=http://127.0.0.1:8000/predict
```

### 3 · Start FastAPI Backend
```bash
uvicorn app:app --host 127.0.0.1 --port 8000 --reload
```

### 4 · Launch Streamlit Frontend
```bash
streamlit run frontend.py
```

---

## 🧪 Testing the API

### Via Swagger UI
Navigate to `https://insurance-premium-prediction-api-euqj.onrender.com/docs` and test with:

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
| **Containerization** | Docker + Docker Compose | Containerized deployment |
| **Cloud** | Render | Free cloud deployment |
| **Serialization** | Pickle | Model persistence |

---

## 📝 License

This project is for educational and demonstration purposes.

---

<div align="center">
<br>

**Built with 🧠 Machine Learning · ⚡ FastAPI · 🎨 Streamlit · 🐳 Docker · ☁️ Render**

</div>
