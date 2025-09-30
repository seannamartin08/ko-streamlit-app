📊 Coca-Cola (KO) Stock Analysis & Prediction App

This project is an interactive Streamlit web application that analyzes and visualizes the stock performance of Coca-Cola Company (ticker: KO). It combines historical stock data, technical indicators, and machine learning predictions into one easy-to-use dashboard.

🔹 Features

✅ Live stock data: Fetches Coca-Cola’s latest price data from Yahoo Finance.

✅ Interactive charts: Visualize price movements, moving averages, and trends with Plotly.

✅ Machine learning predictions: Uses a trained Random Forest model (rf_ko_model.pkl) to predict Coca-Cola’s stock closing price.

✅ Custom file upload: Option to upload your own historical stock dataset (.csv) for analysis.

✅ Technical indicators: Built-in calculations like 20-day and 50-day moving averages (MA20, MA50).

✅ Streamlit app: User-friendly interface accessible via browser.


🔹 Tech Stack

Python 🐍

Streamlit (web app framework)

Pandas, NumPy (data analysis)

Plotly (interactive visualizations)

scikit-learn (machine learning)

yfinance (real-time stock data)

Joblib (model persistence)

🔹 Project Workflow

Data Collection

Fetch Coca-Cola stock history from Yahoo Finance (yfinance)

Optionally upload custom CSV data

Feature Engineering

Compute moving averages (MA20, MA50)

Prepare features for machine learning

Model

Pre-trained Random Forest model (rf_ko_model.pkl) predicts closing price

Visualization

Interactive Plotly charts (candlestick/line + moving averages)

Metrics display for model predictions

Deployment

Runs locally with Streamlit

Ready for Streamlit Cloud deployment
