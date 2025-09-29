import streamlit as st
import pandas as pd
import joblib
import yfinance as yf
import plotly.graph_objects as go
import os
import requests

st.set_page_config(page_title="Coca-Cola (KO) Stock Predictor", layout='wide')

st.title("Coca-Cola (KO) Stock - Predictions & Indicators")

# MODEL LOADING
MODEL_PATH = "rf_ko_model.pkl"
MODEL_URL = ""  # optional: put raw URL to your model file here

if not os.path.exists(MODEL_PATH) and MODEL_URL:
    try:
        with st.spinner("Downloading model..."):
            r = requests.get(MODEL_URL, stream=True, timeout=60)
            r.raise_for_status()
            with open(MODEL_PATH, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
    except Exception as e:
        st.error(f"Failed to download model: {e}")

model = None
if os.path.exists(MODEL_PATH):
    try:
        model = joblib.load(MODEL_PATH)
    except Exception as e:
        st.error(f"Failed to load model: {e}")

# Data input
uploaded = st.file_uploader("Upload history CSV (optional)", type="csv")
if uploaded:
    df = pd.read_csv(uploaded, parse_dates=['Date'])
else:
    with st.spinner("Fetching data from Yahoo Finance..."):
        df = yf.download("KO", start="2015-01-01", end=pd.Timestamp.today().strftime("%Y-%m-%d")).reset_index()

# Indicators
df['MA_20'] = df['Close'].rolling(20).mean()
df['MA_50'] = df['Close'].rolling(50).mean()

st.subheader("Price chart")
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'], name='Close'))
fig.add_trace(go.Scatter(x=df['Date'], y=df['MA_20'], name='MA20'))
fig.add_trace(go.Scatter(x=df['Date'], y=df['MA_50'], name='MA50'))
st.plotly_chart(fig, use_container_width=True)

st.subheader("Latest data")
st.write(df.tail(3))

if model is not None:
    features = ['Open','High','Low','Volume','MA_20','MA_50']
    missing = [f for f in features if f not in df.columns]
    if missing:
        st.warning(f"Missing features for model prediction: {missing}")
    else:
        latest = df.iloc[-1:]
        feat = latest[features].fillna(0)
        try:
            pred = model.predict(feat)[0]
            st.metric("Predicted Close (model)", f"{pred:.2f}")
        except Exception as e:
            st.error(f"Model prediction failed: {e}")
else:
    st.info("Model not found. Place rf_ko_model.pkl in the same folder as app.py or set MODEL_URL in the script.")
