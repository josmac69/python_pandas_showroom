import pandas as pd
import json

def main():
    print("Pandas JSON data")
    filename = '/inputs/pets_and_owners.json'

    # Load the JSON data from a file into a pandas DataFrame
    print("\nLoading JSON data from a file into a pandas DataFrame:")
    df = pd.read_json(filename, encoding='utf-8')

    # Print the DataFrame
    print("\nDataFrame:")
    print(df)

    # print information about the DataFrame
    print("\nDataFrame info:")
    print(df.info())

    # describe the DataFrame
    print("\nDataFrame description:")
    print(df.describe())

    # Open the file and load the JSON data using the json module
    print("\nLoading JSON data from a file using the json module:")
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Print the loaded data
    print(data)

    # Flatten the nested JSON data into a pandas DataFrame
    print("\nFlattening the nested JSON data into a pandas DataFrame:")
    df_pets = pd.json_normalize(data, record_path=['pets'], meta=['name'], meta_prefix='owner_')

    # Print the DataFrame
    print("\nDataFrame:")
    print(df_pets)

    # Group the data by name and count the number of pets
    print("\nGrouping the data by owner_name and counting the number of pets:")
    #counts = df_pets.groupby('name')['name'].count()
    counts = df_pets.groupby('owner_name')['owner_name'].count()

    # Print the counts
    print("\nCounts:")
    print(counts)

    # Load the JSON data into a pandas DataFrame
    print("\nAlternative way of loading JSON data into a pandas DataFrame:")
    print("\nReading using json library:")
    with open(filename, 'r') as f:
        data = json.load(f)

    # Flatten the nested JSON data into a pandas DataFrame
    df = pd.json_normalize(data)
    print(df.head())

# check if script is run as main
if __name__ == "__main__":
    main()
