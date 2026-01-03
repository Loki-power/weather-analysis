def yearly_avg_temp_max(df):
    return df.groupby(df['Date'].dt.year)['Temp Max'].mean()

def yearly_avg_temp_min(df):
    return df.groupby(df['Date'].dt.year)['Temp Min'].mean()

def yearly_rainfall(df):
    return df.groupby(df['Date'].dt.year)['Rain'].sum()

