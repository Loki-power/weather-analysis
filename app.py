import streamlit as st
from src.data_loader import load_data

# ---------------- LOAD DATA ----------------
DATA_PATH = "data/raw_weather.csv"
df = load_data(DATA_PATH)

# ---------------- CHECK ----------------
st.title("Historical Weather Data Analysis (1951–Present)")
st.write("Sample Data")
st.dataframe(df.head())

# ---------------- COLUMN NAMES ----------------
# Change these if CSV column names differ
TEMP_MAX_COL = "Temp Max"
TEMP_MIN_COL = "Temp Min"
RAIN_COL = "Rain"

# ---------------- GROUP YEARLY ----------------
df["Year"] = df["Date"].dt.year

yearly = df.groupby("Year").agg({
    TEMP_MAX_COL: "mean",
    TEMP_MIN_COL: "mean",
    RAIN_COL: "mean"
}).reset_index()

# ---------------- PLOTS ----------------
st.line_chart(yearly.set_index("Year")[TEMP_MAX_COL])
st.line_chart(yearly.set_index("Year")[TEMP_MIN_COL])
st.line_chart(yearly.set_index("Year")[RAIN_COL])
from src.forecasting import forecast_series

st.subheader("🔮 Future Temperature Forecast (Next 10 Years)")

forecast = forecast_series(
    yearly,
    "Year",
    TEMP_MAX_COL,
    periods=10
)

st.line_chart(
    forecast.set_index("ds")["yhat"]
)

