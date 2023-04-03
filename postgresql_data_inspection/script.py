import configparser
import pandas as pd
import psycopg2

# Read the configuration file
config = configparser.ConfigParser()
config.read('/secrets/postgresql_adventureworks.ini')

# Get the PostgreSQL credentials from the configuration file
host = config.get('postgresql', 'host')
port = config.get('postgresql', 'port')
database = config.get('postgresql', 'database')
user = config.get('postgresql', 'user')
password = config.get('postgresql', 'password')

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host=host,
    port=port,
    database=database,
    user=user,
    password=password
)

# Define the SQL query to retrieve the data
query = "select schemaname, relname, n_live_tup from pg_stat_all_tables where schemaname not like 'pg_%' order by 1,2"

# Read the data from PostgreSQL into a Pandas DataFrame
df = pd.read_sql(query, conn)

# Inspect the data
print(df.head())

# Write the data to a CSV file
df.to_csv("/outputs/output.csv", index=False)

# Close the database connection
conn.close()
