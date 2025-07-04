import pandas as pd
import glob
import os

# Grab all CSV files in the folder (change 'data/*.csv' to your path)
csv_files = glob.glob('C:/Users/rogun/international-payments-compliance-analytics/data/*.csv')

for file in csv_files:
    try:
        df = pd.read_csv(file)
        if df.empty:
            print(f"{file}: [EMPTY DATAFRAME]")
            continue

        profile = pd.DataFrame({
            'Data Type': df.dtypes,
            'Non-Null Count': df.notnull().sum(),
            'Unique Values': df.nunique(),
            'Missing Values': df.isnull().sum(),
            'Missing Percentage': (df.isnull().sum() / len(df)) * 100
        })

        print(f"\n=== Profile for {os.path.basename(file)} ===")
        print(profile)

        # Optional: save profile as CSV for later review
        profile.to_csv(file.replace('.csv', '_profile.csv'))

    except Exception as e:
        print(f"{file}: [ERROR] {e}")
