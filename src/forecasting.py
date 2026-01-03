from prophet import Prophet
import pandas as pd

def forecast_series(df, date_col, value_col, periods=10):
    data = df[[date_col, value_col]].copy()

    # Convert year or date to datetime (VERY IMPORTANT)
    if not pd.api.types.is_datetime64_any_dtype(data[date_col]):
        data[date_col] = pd.to_datetime(
            data[date_col].astype(str) + "-12-31"
        )

    data = data.rename(columns={date_col: "ds", value_col: "y"})

    model = Prophet()
    model.fit(data)   # ← YOU MISSED THIS

    future = model.make_future_dataframe(periods=periods, freq="Y")
    forecast = model.predict(future)

    return forecast[["ds", "yhat"]]
