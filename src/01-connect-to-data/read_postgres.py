import os
import pandas as pd
from sqlalchemy import create_engine

# Database connection parameters from environment variables
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

# Connection string creation using SQLAlchemy's create_engine
engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# SQL query to fetch data
query = """
select
  country
  ,count(customer_id) as total_customers
from northwind_raw.customers
group by
  country
order by
  count(customer_id) desc
"""

# Read the SQL query into a Pandas DataFrame
df = pd.read_sql(query, engine)


# Display the first few rows of the DataFrame
print(df.head())