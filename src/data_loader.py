import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    df['Date'] = pd.to_datetime(
        df['Date'],
        errors='coerce',
        dayfirst=True
    )

    df = df.dropna(subset=['Date'])
    return df
