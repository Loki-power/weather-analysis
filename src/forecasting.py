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
