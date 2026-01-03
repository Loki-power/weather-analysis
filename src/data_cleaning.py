import pandas as pd

def clean_data(df):
    numeric_cols = ['Temp Max', 'Temp Min', 'Rainfall']

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Drop rows where essential numeric values are missing
    df = df.dropna(subset=['Temp Max', 'Temp Min'])

    return df
