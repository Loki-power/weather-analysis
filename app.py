from src.forecasting import forecast_temperature
import pandas as pd
import streamlit as st
from src.data_loader import load_data

# ---------------- LOAD DATA ----------------
DATA_PATH = "data/raw_weather.csv"
df = load_data(DATA_PATH)

# ---------------- CHECK ----------------
st.title("Historical Weather Data Analysis (1951–Present)")
st.write("Sample Data")
#st.dataframe(df.head())

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
st.markdown("## 📈 Yearly Average Maximum Temperature (°C)")
st.line_chart(yearly.set_index("Year")[TEMP_MAX_COL])

st.markdown("## 📉 Yearly Average Minimum Temperature (°C)")
st.line_chart(yearly.set_index("Year")[TEMP_MIN_COL])

st.markdown("## 🌧️ Yearly Average Rainfall (mm)")
st.line_chart(yearly.set_index("Year")[RAIN_COL])
# Year Range Slider
st.sidebar.header("📅 Year Filter")

min_year = int(df['Date'].dt.year.min())
max_year = int(df['Date'].dt.year.max())

year_range = st.sidebar.slider(
    "Select Year Range",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

df = df[
    (df['Date'].dt.year >= year_range[0]) &
    (df['Date'].dt.year <= year_range[1])
]




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
st.markdown("---")
st.subheader("🔮 Future Temperature Forecast")

future_year = st.number_input(
    "Enter a future year",
    min_value=max_year + 1,
    max_value=2100,
    value=max_year + 5
)

pred_max = forecast_temperature(df, "Temp Max", future_year)
pred_min = forecast_temperature(df, "Temp Min", future_year)

st.success(
    f"📈 Predicted Max Temp in {future_year}: {pred_max:.2f} °C"
)
st.info(
    f"📉 Predicted Min Temp in {future_year}: {pred_min:.2f} °C"
)
