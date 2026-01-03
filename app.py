st.set_page_config(
    page_title="Weather Analysis",
    layout="wide"
)

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
st.markdown("---")

st.subheader("🌡️ Temperature Trends")

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(plot_temp_max(temp_max), use_container_width=True)

with col2:
    st.plotly_chart(plot_temp_min(temp_min), use_container_width=True)

st.markdown("---")
st.subheader("🌧️ Rainfall Pattern")

st.plotly_chart(plot_rainfall(rain), use_container_width=True)

from src.forecasting import forecast_temperature
from datetime import date

st.header("🔮 Future Weather Forecast")

future_date = st.date_input(
    "Select a future date",
    min_value=date.today()
)

days_ahead = (future_date - df['Date'].max().date()).days

if days_ahead > 0:
    forecast_max = forecast_temperature(df, 'Temp Max', days_ahead)
    forecast_min = forecast_temperature(df, 'Temp Min', days_ahead)

    st.subheader("Forecasted Maximum Temperature")
    st.line_chart(forecast_max.set_index('ds'))

    st.subheader("Forecasted Minimum Temperature")
    st.line_chart(forecast_min.set_index('ds'))
else:
    st.warning("Please select a future date after last available data.")


