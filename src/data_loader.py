import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    # Fix Date column
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce", dayfirst=True)
    df = df.dropna(subset=["Date"])

    # FORCE numeric conversion (THIS FIXES YOUR ERROR)
    numeric_cols = df.columns.drop("Date")

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Drop rows where all numeric values are NaN
    df = df.dropna(how="all", subset=numeric_cols)

    return df
