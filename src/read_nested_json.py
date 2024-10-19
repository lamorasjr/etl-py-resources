import pandas as pd
import json

file_path='data/sample_data.json'
# Load the JSON structure (assuming it's in a file)
with open(file_path) as f:
    data = json.load(f)

# Normalize the JSON data to flatten the nested structure
df = pd.json_normalize(data, 
                       record_path=['glossary', 'GlossDiv', 'GlossList', 'GlossEntry', 'GlossDef', 'GlossSeeAlso'],
                       meta=[
                            ['glossary', 'title'],
                            ['glossary', 'GlossDiv', 'title'],
                            ['glossary', 'GlossDiv', 'GlossList', 'GlossEntry', 'ID'],
                            ['glossary', 'GlossDiv', 'GlossList', 'GlossEntry', 'SortAs'],
                            ['glossary', 'GlossDiv', 'GlossList', 'GlossEntry', 'GlossTerm'],
                            ['glossary', 'GlossDiv', 'GlossList', 'GlossEntry', 'Acronym'],
                            ['glossary', 'GlossDiv', 'GlossList', 'GlossEntry', 'Abbrev'],
                            ['glossary', 'GlossDiv', 'GlossList', 'GlossEntry', 'GlossDef', 'para'],
                            ['glossary', 'GlossDiv', 'GlossList', 'GlossEntry', 'GlossSee']
                       ])

# Show the resulting dataframe
print(df)
