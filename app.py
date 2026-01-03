import streamlit as st
import pandas as pd

from src.data_loader import load_data
from src.forecasting import forecast_temperature

st.set_page_config(page_title="Weather Analysis", layout="wide")

st.title("🌦 Historical Weather Data Analysis (1951–Present)")

# ---------------- LOAD DATA ----------------
DATA_PATH = "data/weather.csv"
df = load_data(DATA_PATH)

# ---------------- CLEAN COLUMN NAMES ----------------
# Adjust these if your CSV column names differ
TEMP_MAX_COL = "Temp Max"
TEMP_MIN_COL = "Temp Min"
RAIN_COL = "Rain"

# ---------------- YEARLY AGGREGATION ----------------
df["Year"] = df["Date"].dt.year

yearly = df.groupby("Year").agg({
    TEMP_MAX_COL: "mean",
    TEMP_MIN_COL: "mean",
    RAIN_COL: "sum"
}).reset_index()

# ---------------- PLOTS ----------------
st.subheader("📈 Yearly Average Maximum Temperature")
st.line_chart(yearly.set_index("Year")[TEMP_MAX_COL])

st.subheader("📉 Yearly Average Minimum Temperature")
st.line_chart(yearly.set_index("Year")[TEMP_MIN_COL])

st.subheader("🌧 Yearly Total Rainfall")
st.line_chart(yearly.set_index("Year")[RAIN_COL])

# ---------------- FORECASTING ----------------
st.subheader("🔮 Future Temperature Forecast")

forecast_days = st.slider("Days to forecast", 30, 365, 180)

forecast = forecast_temperature(df, TEMP_MAX_COL, forecast_days)

st.line_chart(
    forecast.set_index("ds")[["yhat"]]
)
