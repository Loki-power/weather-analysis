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

import plotly.express as px

def plot_rainfall(trend):
    fig = px.bar(
        trend,
        title="Yearly Total Rainfall",
        labels={"value": "Rainfall (mm)", "index": "Year"}
    )

    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Rainfall (mm)",
        bargap=0.2
    )

    return fig

