import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/predict")

st.set_page_config(
    page_title="RiskScan — Insurance Predictor",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

* { box-sizing: border-box; margin: 0; padding: 0; }

.stApp {
    background: #060A12;
    font-family: 'Inter', sans-serif;
}

.block-container {
    max-width: 820px !important;
    padding: 1.5rem 2rem 4rem !important;
}

#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }

/* ── HERO ── */
.hero {
    text-align: center;
    padding: 2.5rem 0 2rem;
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: rgba(6, 182, 212, 0.08);
    border: 1px solid rgba(6, 182, 212, 0.25);
    color: #06B6D4;
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    padding: 0.4rem 1.1rem;
    border-radius: 100px;
    margin-bottom: 1.4rem;
    font-family: 'JetBrains Mono', monospace;
}

.hero-title {
    font-size: 2.8rem;
    font-weight: 700;
    color: #F1F5F9;
    margin-bottom: 0.8rem;
    letter-spacing: -0.035em;
    line-height: 1.12;
}

.hero-title .accent {
    background: linear-gradient(120deg, #06B6D4 0%, #818CF8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-sub {
    color: #475569;
    font-size: 0.92rem;
    line-height: 1.7;
    max-width: 480px;
    margin: 0 auto;
}

/* ── CARDS ── */
.card {
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(255,255,255,0.065);
    border-radius: 18px;
    padding: 1.6rem 1.75rem;
    margin-bottom: 1rem;
}

.card-label {
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: #334155;
    font-family: 'JetBrains Mono', monospace;
    margin-bottom: 1.2rem;
    display: flex;
    align-items: center;
    gap: 0.6rem;
}

.card-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: rgba(255,255,255,0.05);
}

/* ── INPUTS ── */
.stNumberInput input,
.stTextInput input {
    background: rgba(255,255,255,0.035) !important;
    border: 1px solid rgba(255,255,255,0.075) !important;
    border-radius: 10px !important;
    color: #E2E8F0 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.9rem !important;
    transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
    caret-color: #06B6D4 !important;
}

.stNumberInput input:focus,
.stTextInput input:focus {
    border-color: rgba(6, 182, 212, 0.45) !important;
    box-shadow: 0 0 0 3px rgba(6, 182, 212, 0.08) !important;
    outline: none !important;
}

.stNumberInput input:hover,
.stTextInput input:hover {
    border-color: rgba(255,255,255,0.13) !important;
}

/* ── SELECTBOX ── */
.stSelectbox > div > div {
    background: rgba(255,255,255,0.035) !important;
    border: 1px solid rgba(255,255,255,0.075) !important;
    border-radius: 10px !important;
    color: #E2E8F0 !important;
    font-size: 0.9rem !important;
}

.stSelectbox > div > div:hover {
    border-color: rgba(255,255,255,0.13) !important;
}

/* ── LABELS ── */
label,
.stSelectbox label,
.stNumberInput label,
.stTextInput label {
    color: #64748B !important;
    font-size: 0.8rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.02em !important;
    margin-bottom: 0.3rem !important;
}

/* ── BUTTON ── */
.stButton > button {
    width: 100% !important;
    background: linear-gradient(135deg, #0891B2, #6D28D9) !important;
    color: #F8FAFC !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.9rem 2rem !important;
    font-size: 0.92rem !important;
    font-weight: 600 !important;
    font-family: 'Inter', sans-serif !important;
    letter-spacing: 0.03em !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 20px rgba(8, 145, 178, 0.25) !important;
    position: relative !important;
}

.stButton > button:hover {
    opacity: 0.88 !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 30px rgba(8, 145, 178, 0.35) !important;
}

.stButton > button:active {
    transform: translateY(0) !important;
    box-shadow: 0 2px 10px rgba(8, 145, 178, 0.2) !important;
}

/* ── SPINNER ── */
.stSpinner { color: #06B6D4 !important; }

/* ── RESULT CARDS ── */
.result-wrap {
    margin-top: 1.5rem;
    animation: fadeUp 0.4s ease;
}

@keyframes fadeUp {
    from { opacity: 0; transform: translateY(16px); }
    to   { opacity: 1; transform: translateY(0); }
}

.result-card {
    border-radius: 18px;
    padding: 2.25rem 2rem;
    text-align: center;
    position: relative;
    overflow: hidden;
}

.result-card::before {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: 18px;
    pointer-events: none;
}

.result-card.high {
    background: rgba(239, 68, 68, 0.07);
    border: 1px solid rgba(239, 68, 68, 0.28);
    box-shadow: 0 0 60px rgba(239, 68, 68, 0.08), inset 0 1px 0 rgba(239,68,68,0.15);
}

.result-card.medium {
    background: rgba(245, 158, 11, 0.07);
    border: 1px solid rgba(245, 158, 11, 0.28);
    box-shadow: 0 0 60px rgba(245, 158, 11, 0.08), inset 0 1px 0 rgba(245,158,11,0.15);
}

.result-card.low {
    background: rgba(16, 185, 129, 0.07);
    border: 1px solid rgba(16, 185, 129, 0.28);
    box-shadow: 0 0 60px rgba(16, 185, 129, 0.08), inset 0 1px 0 rgba(16,185,129,0.15);
}

.result-icon { font-size: 2.8rem; margin-bottom: 1rem; }

.result-eyebrow {
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #475569;
    font-family: 'JetBrains Mono', monospace;
    margin-bottom: 0.6rem;
}

.result-value {
    font-size: 2.4rem;
    font-weight: 700;
    letter-spacing: -0.03em;
    margin-bottom: 0.75rem;
    line-height: 1;
}

.result-value.high   { color: #F87171; }
.result-value.medium { color: #FBBF24; }
.result-value.low    { color: #34D399; }

.result-desc {
    color: #475569;
    font-size: 0.85rem;
    line-height: 1.65;
}

/* ── ERROR STATES ── */
.err-box {
    background: rgba(239,68,68,0.06);
    border: 1px solid rgba(239,68,68,0.18);
    border-radius: 14px;
    padding: 1.25rem 1.5rem;
    margin-top: 1rem;
}

.err-title {
    color: #F87171;
    font-weight: 600;
    font-size: 0.9rem;
    margin-bottom: 0.5rem;
}

.err-body {
    color: #64748B;
    font-size: 0.85rem;
    line-height: 1.6;
}

.err-body code {
    color: #06B6D4;
    background: rgba(6,182,212,0.08);
    padding: 0.15rem 0.4rem;
    border-radius: 5px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.82rem;
}

.validation-item {
    background: rgba(245,158,11,0.06);
    border-left: 2px solid #F59E0B;
    border-radius: 0 8px 8px 0;
    padding: 0.55rem 1rem;
    margin: 0.4rem 0;
    color: #94A3B8;
    font-size: 0.84rem;
}

.validation-item strong { color: #CBD5E1; }

/* ── FOOTER ── */
.app-footer {
    text-align: center;
    color: #1E293B;
    font-size: 0.68rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    font-family: 'JetBrains Mono', monospace;
    padding: 2.5rem 0 1rem;
}
</style>
""", unsafe_allow_html=True)


# ── HERO SECTION ──
st.markdown("""
<div class="hero">
    <div class="hero-badge">⬡ ML-Powered Assessment</div>
    <h1 class="hero-title">Insurance <span class="accent">Risk</span><br>Predictor</h1>
    <p class="hero-sub">Enter health and demographic details to get an instant AI-powered insurance risk assessment</p>
</div>
""", unsafe_allow_html=True)


# ── PERSONAL DETAILS ──
st.markdown('<div class="card"><div class="card-label">👤 Personal Details</div>', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    age = st.number_input("Age", min_value=-150, max_value=300, value=35)
with c2:
    city = st.text_input("City", value="Mumbai")
with c3:
    occupation = st.selectbox("Occupation", options=[
        'private_job', 'government_job', 'business_owner',
        'freelancer', 'retired', 'student', 'unemployed'
    ])
st.markdown('</div>', unsafe_allow_html=True)


# ── HEALTH METRICS ──
st.markdown('<div class="card"><div class="card-label">💓 Health Metrics</div>', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    height = st.number_input("Height (m)", min_value=0.0, max_value=5.0, value=1.72, step=0.01, format="%.2f")
with c2:
    weight = st.number_input("Weight (kg)", min_value=-50.0, max_value=500.0, value=79.0, step=0.5, format="%.1f")
with c3:
    smoker = st.selectbox("Smoker?", options=[False, True], format_func=lambda x: "Yes 🚬" if x else "No ✅")
st.markdown('</div>', unsafe_allow_html=True)


# ── FINANCIAL PROFILE ──
st.markdown('<div class="card"><div class="card-label">💼 Financial Profile</div>', unsafe_allow_html=True)
income_lpa = st.number_input("Annual Income (LPA)", min_value=-10.0, value=10.0, step=0.1, format="%.1f")
st.markdown('</div>', unsafe_allow_html=True)


# ── CTA ──
st.markdown("<br>", unsafe_allow_html=True)
clicked = st.button("⬡  Run Risk Assessment", use_container_width=True)


# ── PREDICTION LOGIC ──
if clicked:
    ui_errors = []
    if age < 0 or age > 120:
        ui_errors.append(("Age", "Input should be between 0 and 120"))
    if height >= 2.5:
        ui_errors.append(("Height", "Input should be strictly less than 2.5 meters"))
    
    if ui_errors:
        st.markdown('<div class="err-box"><div class="err-title">❌ Validation Errors — please fix your inputs</div>', unsafe_allow_html=True)
        for field, msg in ui_errors:
            st.markdown(f'<div class="validation-item">👉 <strong>{field}</strong>: {msg}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.stop()

    payload = {
        "age":        int(age),
        "weight":     float(weight),
        "height":     float(height),
        "income_lpa": float(income_lpa),
        "smoker":     bool(smoker),
        "city":       city.strip(),
        "occupation": occupation,
    }

    with st.spinner("Contacting FastAPI server · Running model inference..."):
        try:
            response = requests.post(API_URL, json=payload, timeout=10)

            # ── SUCCESS ──
            if response.status_code == 200:
                result = response.json()

                if "predicted_category" in result:
                    pred = result["predicted_category"].lower()

                    risk_map = {
                        "high":   ("high",   "🛑", "HIGH RISK",   "This profile carries elevated insurance risk. A higher premium tier is recommended."),
                        "medium": ("medium", "⚠️", "MEDIUM RISK", "This profile falls within the moderate risk range. Standard premium tier applies."),
                    }
                    css_cls, icon, label, desc = risk_map.get(
                        pred, ("low", "✅", "LOW RISK", "This profile indicates low insurance risk. A standard or discounted premium applies.")
                    )

                    st.markdown(f"""
                    <div class="result-wrap">
                        <div class="result-card {css_cls}">
                            <div class="result-icon">{icon}</div>
                            <div class="result-eyebrow">Predicted Risk Category</div>
                            <div class="result-value {css_cls}">{label}</div>
                            <div class="result-desc">{desc}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                else:
                    st.markdown("""
                    <div class="err-box">
                        <div class="err-title">⚠️ Unexpected Response</div>
                        <div class="err-body">Response received but <code>predicted_category</code> key was missing.</div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.json(result)

            # ── VALIDATION ERROR ──
            elif response.status_code == 422:
                st.markdown('<div class="err-box"><div class="err-title">❌ Validation Errors — please fix your inputs</div>', unsafe_allow_html=True)
                try:
                    errors = response.json().get("detail", [])
                    for err in errors:
                        field = str(err.get("loc", ["?"])[-1]).replace("_", " ").title()
                        msg   = err.get("msg", "Invalid value")
                        st.markdown(f'<div class="validation-item">👉 <strong>{field}</strong>: {msg}</div>', unsafe_allow_html=True)
                except Exception:
                    st.json(response.json())
                st.markdown('</div>', unsafe_allow_html=True)

            # ── OTHER HTTP ERROR ──
            else:
                st.markdown(f"""
                <div class="err-box">
                    <div class="err-title">❌ API Error — HTTP {response.status_code}</div>
                    <div class="err-body">The server returned an unexpected status code.</div>
                </div>
                """, unsafe_allow_html=True)
                try:
                    st.json(response.json())
                except Exception:
                    st.write(response.text)

        # ── CONNECTION ERROR ──
        except requests.exceptions.ConnectionError:
            st.markdown(f"""
            <div class="err-box">
                <div class="err-title">❌ Connection Failed</div>
                <div class="err-body">
                    Could not reach the FastAPI server at <code>{API_URL}</code><br><br>
                    Make sure Uvicorn is running:<br>
                    <code>uvicorn main:app --reload</code>
                </div>
            </div>
            """, unsafe_allow_html=True)

        except requests.exceptions.Timeout:
            st.markdown("""
            <div class="err-box">
                <div class="err-title">⏱️ Request Timed Out</div>
                <div class="err-body">The server took too long to respond. Try again in a moment.</div>
            </div>
            """, unsafe_allow_html=True)


# ── FOOTER ──
st.markdown('<div class="app-footer">RiskScan &nbsp;·&nbsp; ML-Powered &nbsp;·&nbsp; FastAPI + Streamlit</div>', unsafe_allow_html=True)