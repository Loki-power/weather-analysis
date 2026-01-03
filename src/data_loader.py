import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    # Convert Date column safely (handles Excel serial + strings)
    df['Date'] = pd.to_datetime(
        df['Date'],
        errors='coerce',
        dayfirst=True
    )

    # Drop rows where date could not be parsed
    df = df.dropna(subset=['Date'])

    return df
