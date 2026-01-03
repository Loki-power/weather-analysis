import streamlit as st
from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.analysis import (
    yearly_avg_temp_max,
    yearly_avg_temp_min,
    yearly_rainfall
)
from src.visualization import (
    plot_temp_max,
    plot_temp_min,
    plot_rainfall
)

st.set_page_config(page_title="Weather Analysis", layout="wide")

st.title("🌦️ Historical Weather Data Analysis (1951–Present)")

df = load_data("data/raw_weather.csv")
df = clean_data(df)

temp_max = yearly_avg_temp_max(df)
temp_min = yearly_avg_temp_min(df)
rain = yearly_rainfall(df)

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(plot_temp_max(temp_max))

with col2:
    st.plotly_chart(plot_temp_min(temp_min))

st.plotly_chart(plot_rainfall(rain))


