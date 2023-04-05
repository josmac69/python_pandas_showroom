import pandas as pd
import xlrd

# Load the Titanic dataset
print("Loading the Titanic dataset...")
titanic_df = pd.read_excel('/inputs/titanic3.xls')

# print information about the dataset
print("\nDataset info:")
print(titanic_df.info())

# print descriptive statistics for the dataset
print("\nDescriptive statistics:")
print(titanic_df.describe())

# check column names
print("\nColumn names:")
print(titanic_df.columns)

# check null values
print("\nNull values:")
print(titanic_df.isnull().sum())

# Count the number of rows before dropping null values
num_rows_before = titanic_df.shape[0]

# Drop rows with null values in the 'Age' column
print("\nDropping rows with null values in the 'Age' column...")
titanic_df.dropna(subset=['age'], inplace=True)

# Count the number of rows after dropping null values
num_rows_after = titanic_df.shape[0]

# Calculate the number of dropped rows
num_dropped_rows = num_rows_before - num_rows_after
print(f"Number of dropped rows: {num_dropped_rows}")

# Check for duplicate rows
print("\nChecking for duplicate rows...")
duplicate_rows = titanic_df[titanic_df.duplicated()]

# Group the duplicate rows by passenger class and sex
print("\nGroup the duplicate rows by passenger class and sex")
grouped_duplicates = duplicate_rows.groupby(['pclass', 'sex']).size().reset_index(name='counts')

# Print the grouped duplicate rows
print("\nGrouped duplicate rows:")
print(grouped_duplicates)

# Different method to check for duplicate rows
print("\nChecking for duplicate rows...")
duplicate_rows = titanic_df[titanic_df.duplicated()]

# Print any duplicate rows
if not duplicate_rows.empty:
    print('The dataset contains duplicate rows:')
    print(duplicate_rows)

    # Remove duplicate rows
    print("\nRemoving duplicate rows...")
    titanic_df = titanic_df.drop_duplicates()

else:
    print('The dataset does not contain any duplicate rows.')

# Group the dataset by gender and calculate the average age for each group
print("\nGroup the dataset by gender and calculate the average age for each group...")
titanic_grouped_df = titanic_df.groupby('sex').agg({'age': 'mean'})

# print grouped dataset
print("\nGrouped dataset:")
print(titanic_grouped_df)

# Create a pivot table to summarize the average age for each gender and passenger class
print("\nCreate a pivot table to summarize the average age for each gender and passenger class...")
titanic_pivot_df = pd.pivot_table(titanic_df, values='age', index='sex', columns='pclass', aggfunc='mean')

# print pivot table
print("\nPivot table:")
print(titanic_pivot_df)

# Export the cleaned and transformed dataset to a new CSV file
titanic_df.to_csv('/outputs/cleaned_titanic.csv', index=False)
