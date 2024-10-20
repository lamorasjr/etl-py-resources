import pandas as pd

file_path = 'data/sample_data.json'
# Connect and read the JSON file into a Pandas DataFrame
df = pd.read_json(file_path)

# To display the first few rows of the dataframe
print(df.head())