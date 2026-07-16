# 🏥 Insurance Premium Predictor

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

A machine learning-powered web application that predicts an individual's insurance premium risk category (Low, Medium, High) based on their personal and health demographics. 

---

## 🚀 What We Accomplished

1. **Machine Learning Model Generation**: Trained a robust Random Forest classification model (`insurance_prediction_random_forest.ipynb`) on an insurance dataset and serialized it (`model.pkl`).
2. **FastAPI Backend Integration**: Connected the serialized ML model to a lightning-fast FastAPI backend (`app.py`). The backend exposes a `/predict` endpoint that:
   - Validates incoming user payloads using Pydantic models.
   - Converts the incoming JSON into a Pandas DataFrame.
   - Generates and returns a risk category prediction safely serialized as JSON.
3. **Streamlit Frontend**: Created a clean and interactive Streamlit web application (`frontend.py`) where users can input physical details (BMI logic), demographic details, and more to instantly see their risk category. 
4. **Environment Variables**: Integrated a robust `.env` approach to smoothly bind the frontend API calls to wherever the backend is hosted.

---

## 🛠️ How to Run Locally

### 1. Install Dependencies
Make sure you have Python installed. Install the required packages via `pip`:
```bash
pip install -r req.txt
```

### 2. Start the FastAPI Backend
Start the FastAPI application on port `8000` using `uvicorn`:
```bash
uvicorn app:app --host 127.0.0.1 --port 8000 --reload
```
*The backend will now be actively listening on `http://127.0.0.1:8000`.*

### 3. Configure the Environment
Ensure your `.env` file in the root directory specifies the backend API URL. For a local setup, it should contain:
```env
API_URL=http://127.0.0.1:8000/predict
```

### 4. Start the Streamlit Frontend
Open a new terminal window (keep the backend running) and launch the UI:
```bash
streamlit run frontend.py
```
*Your browser will automatically open the interactive web app!*

---

## 🧪 Testing the API Yourself (FastAPI Docs)

FastAPI automatically generates an interactive Swagger UI documentation page. This makes it incredibly easy to test your API without writing a single line of client code!

1. **Open the Docs**: Once your backend is running, navigate to:
   👉 **http://127.0.0.1:8000/docs**
2. **Explore the Endpoint**: Click on the `POST /predict` route to expand it.
3. **Try it Out**: Click the **"Try it out"** button.
4. **Input Test Data**: Edit the JSON payload body. You can use the following profile as an example:
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
5. **Execute**: Click the **Execute** button and view the API response. You will see both the resulting HTTP Status Code (e.g., `200 OK` or `422 Unprocessable Entity`) and the JSON prediction!

---

## 📁 Project Structure

- `app.py`: The FastAPI backend application.
- `frontend.py`: The Streamlit web interface.
- `model.pkl`: The trained Random Forest machine learning model.
- `insurance_prediction_random_forest.ipynb`: The Jupyter Notebook used to clean the data and train the model.
- `insurance.csv`: The dataset used to train the machine learning model.
- `.env`: Environment variables configuring the frontend-to-backend URL connection.
- `req.txt`: Project dependencies and requirements.
