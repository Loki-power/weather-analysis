import plotly.express as px

def plot_temp_max(trend):
    return px.line(
        trend,
        title="Yearly Average Maximum Temperature",
        labels={"value": "Temp Max (°C)", "index": "Year"}
    )

def plot_temp_min(trend):
    return px.line(
        trend,
        title="Yearly Average Minimum Temperature",
        labels={"value": "Temp Min (°C)", "index": "Year"}
    )

def plot_rainfall(trend):
    return px.line(
        trend,
        title="Yearly Total Rainfall",
        labels={"value": "Rainfall (mm)", "index": "Year"}
    )

