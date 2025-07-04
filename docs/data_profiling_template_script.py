import pandas as pd

# Load your dataset
df = pd.read_csv('')

# Advanced profiling
profile = pd.DataFrame({
    'Data Type': df.dtypes,
    'Non-Null Count': df.notnull().sum(),
    'Unique Values': df.nunique(),
    'Missing Values': df.isnull().sum(),
    'Missing Percentage': (df.isnull().sum() / len(df)) * 100
})

print(profile)
