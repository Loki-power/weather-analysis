import pandas as pd
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
import streamlit as st
from src.forecasting import forecast_for_date

st.markdown("## 🔮 Predict Weather for Any Future Date")

target_date = st.date_input(
    "Select a future date",
    min_value=df["Date"].max().date()
)

if st.button("Predict Weather"):
    max_temp = forecast_for_date(df, "Date", TEMP_MAX_COL, target_date)
    min_temp = forecast_for_date(df, "Date", TEMP_MIN_COL, target_date)
    rain = forecast_for_date(df, "Date", RAIN_COL, target_date)

    col1, col2, col3 = st.columns(3)

    col1.metric("🌡️ Max Temp (°C)", max_temp)
    col2.metric("🌡️ Min Temp (°C)", min_temp)
    col3.metric("🌧️ Rainfall (mm)", rain)

st.markdown("## 🔮 Predict Weather for Any Future Date")

input_date = st.date_input(
    "Select a future date",
    value=pd.to_datetime("2030-01-01")
)

if st.button("Predict Temperature"):
    prediction = forecast_for_date(
        df,
        date_col="Date",
        value_col="Temp Max",
        target_date=input_date
    )

    st.success(f"🌡️ Predicted Max Temperature on {input_date}: **{prediction:.2f} °C**")


