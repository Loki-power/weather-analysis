from prophet import Prophet
import pandas as pd


def forecast_for_date(df, date_col, value_col, target_date):
    data = df[[date_col, value_col]].rename(
        columns={date_col: "ds", value_col: "y"}
    )

    model = Prophet()
    model.fit(data)

    future = pd.DataFrame({"ds": [pd.to_datetime(target_date)]})
    forecast = model.predict(future)

    return float(forecast["yhat"].iloc[0])


def forecast_temperature(df, value_col, future_year):
    data = df[["Date", value_col]].rename(
        columns={"Date": "ds", value_col: "y"}
    )

    model = Prophet()
    model.fit(data)

    # Forecast for 1st Jan of future year
    future_date = pd.to_datetime(f"{future_year}-01-01")
    future = pd.DataFrame({"ds": [future_date]})

    forecast = model.predict(future)

    return float(forecast["yhat"].iloc[0])
