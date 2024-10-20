import pandas as pd

file_path = "data/sample_data.xlsx"
sheet_name = 'Sheet1'

# Connect and read the Excel file into a Pandas DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name)

# To display the first few rows of the dataframe
print(df.head())