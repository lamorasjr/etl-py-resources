import pandas as pd

file_path = 'data/sample_data.csv'

df = pd.read_csv(file_path)

print(df.head())