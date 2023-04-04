"""
This script demonstrates connection to a PostgreSQL database,
reading data from a table and showing basic statistics.
It also shows how to write the data to a CSV file and
how to create a histogram of a column.
"""
import configparser
import pandas as pd
import psycopg2
import matplotlib.pyplot as plt

def main():
    """Main function"""
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
    query = "select schemaname, relname, n_live_tup from pg_stat_all_tables \
        where schemaname not like 'pg_%' and schemaname <> 'information_schema' \
        order by 1,2"

    # Read the data from PostgreSQL into a Pandas DataFrame
    df = pd.read_sql(query, conn)

    # Write raw data to a CSV file
    print("\nWriting the data to a CSV file...")
    df.to_csv("/outputs/output.csv", index=False)

    # show basic statistics of the data
    print("\nBasic statistics of the data:")
    print(df.describe())

    # show column names and data types
    print("\nColumn names and data types:")
    print(df.dtypes)

    # show the first 5 biggest tables - without printing the original index
    print("\nThe first 5 rows of the data:")
    print(df.sort_values(by=['n_live_tup','schemaname','relname'], \
        ascending=[False, True, True]).reset_index(drop=True).head(10))

    # show the last 5 tables by row count - without printing the original index
    print("\nThe last 5 rows of the data:")
    print(df.sort_values(by=['n_live_tup','schemaname','relname'], \
        ascending=[False, True, True]).reset_index(drop=True).tail(10))

    # Group the dataframe by schemaname, count number of unique relname values and sum n_live_tup
    result = df.groupby('schemaname'). \
        agg({'relname': 'nunique', 'n_live_tup': 'sum'}) \
        .reset_index()

    # Rename the columns
    result.columns = ['schemaname', 'table_count', 'row_count']

    # print the result
    print("\nGroup the dataframe by schemaname, count unique relname values and sum n_live_tup:")
    print(result.sort_values(by='row_count', ascending=False))

    # Create a histogram of a column
    plt.hist(df['n_live_tup'], bins=20)

    # Save the histogram as a PNG file
    plt.savefig('/outputs/histogram.png')

    # Close the database connection
    conn.close()

    print("\nAll Done!")

# check if script is run as main program
if __name__ == "__main__":
    # execute only if run as a script
    main()
