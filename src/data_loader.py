import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    # Convert Date column
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Convert numeric columns safely
    numeric_cols = ["Temp Max", "Temp Min", "Rain"]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Drop rows with invalid data
    df = df.dropna(subset=["Date"])

    return df
