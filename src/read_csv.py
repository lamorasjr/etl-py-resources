import pandas as pd

file_path = "data/sample_data.csv"
# Connect and read the CSV file into a Pandas DataFrame
df = pd.read_csv(file_path)

# To display the first few rows of the dataframe
print(df.head())