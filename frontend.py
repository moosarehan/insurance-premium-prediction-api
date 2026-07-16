import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/predict")

st.set_page_config(page_title="Insurance Premium Predictor", page_icon="🏥", layout="centered")

st.title("🏥 Insurance Premium Category Predictor")
st.markdown("Enter individual health and demographic details below to predict their insurance risk category.")
st.write("---")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1, max_value=119, value=55)
    height = st.number_input("Height (meters)", min_value=0.5, max_value=2.5, value=1.62, step=0.01)
    smoker = st.selectbox("Is the user a smoker?", options=[True, False])
    city = st.text_input("City", value="Mumbai")

with col2:
    weight = st.number_input("Weight (kg)", min_value=1.0, max_value=300.0, value=92.0, step=0.1)
    income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value=2.5, step=0.1)
    occupation = st.selectbox(
        "Occupation",
        options=['private_job', 'government_job', 'business_owner', 'freelancer', 'retired', 'student', 'unemployed']
    )

st.write("---")

if st.button("Predict Premium Category", use_container_width=True):
    input_data = {
        "age": int(age),
        "weight": float(weight),
        "height": float(height),
        "income_lpa": float(income_lpa),
        "smoker": bool(smoker),
        "city": city.strip(),
        "occupation": occupation
    }

    with st.spinner("Sending data to FastAPI server and running ML model..."):
        try:
            response = requests.post(API_URL, json=input_data)
            
            if response.status_code == 200:
                result = response.json()
                
                if "predicted_category" in result:
                    prediction = result["predicted_category"]
                    
                    if prediction.lower() == "high":
                        st.error(f"### Predicted Insurance Premium Category: **{prediction.upper()}** 🛑")
                    elif prediction.lower() == "medium":
                        st.warning(f"### Predicted Insurance Premium Category: **{prediction.upper()}** ⚠️")
                    else:
                        st.success(f"### Predicted Insurance Premium Category: **{prediction.upper()}** ✅")
                else:
                    st.error("⚠️ Response received but 'predicted_category' key was missing.")
                    st.write("Raw Response:", result)
            
            elif response.status_code == 422:
                st.error("❌ Validation Error: Please fix the following errors in your inputs:")
                try:
                    errors = response.json().get("detail", [])
                    for err in errors:
                        field_name = err.get("loc", [])[-1]
                        error_msg = err.get("msg", "Invalid value")
                        formatted_field = str(field_name).replace("_", " ").title()
                        st.warning(f"👉 **{formatted_field}**: {error_msg}")
                except Exception:
                    st.write(response.json())
            
            else:
                st.error(f"❌ API Error: HTTP Status Code {response.status_code}")
                try:
                    st.write(response.json())
                except Exception:
                    st.write(response.text)

        except requests.exceptions.ConnectionError:
            st.error(f"❌ Connection Failed: Could not connect to the FastAPI server at `{API_URL}`.")