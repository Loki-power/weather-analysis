from prophet import Prophet
import pandas as pd

def forecast_temperature(df, column, periods):
    data = df[['Date', column]].rename(
        columns={'Date': 'ds', column: 'y'}
    )

    model = Prophet()
    model.fit(data)

    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)

    return forecast[['ds', 'yhat']]
