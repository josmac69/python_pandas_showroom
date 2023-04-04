"""Script shows manual creation of dataset"""
import pandas as pd

def main():
    """Main function"""
    # create a DataFrame from a dictionary
    print("\nCreate a DataFrame from a dictionary")
    print("""
    command:
    data_frame = pd.DataFrame({"A" : [1, 3, 4], "B": [5, 9, 12]})
    """)
    data_frame = pd.DataFrame({"A" : [1, 3, 4], "B": [5, 9, 12]})
    print(data_frame)

    # create a DataFrame from a list of lists
    print("\nCreate a DataFrame from a list of lists")
    print("""
    command:
    data_frame = pd.DataFrame([[1, 4, 5], [7, 19, 13]], columns= ["J", "K", "L"])
    """)
    data_frame = pd.DataFrame([[1, 4, 5], [7, 19, 13]], columns= ["J", "K", "L"])
    print(data_frame)

    # create a DataFrame from a list of dictionaries
    print("\nCreate a DataFrame from a list of dictionaries")
    print("""
    command:
    data_frame = pd.DataFrame([{"A": 1, "B": 5}, {"A": 3, "B": 9}, {"A": 4, "B": 12}])
    """)
    data_frame = pd.DataFrame([{"A": 1, "B": 5}, {"A": 3, "B": 9}, {"A": 4, "B": 12}])
    print(data_frame)

    # create a DataFrame from a list of tuples
    print("\nCreate a DataFrame from a list of tuples")
    print("""
    command:
    data_frame = pd.DataFrame([(1, 5), (3, 9), (4, 12)], columns= ["M", "N"])
    """)
    data_frame = pd.DataFrame([(1, 5), (3, 9), (4, 12)], columns= ["M", "N"])
    print(data_frame)

    # create a DataFrame from a list of Series
    print("\nCreate a DataFrame from a list of Series")
    print("""
    command:
    data_frame = pd.DataFrame([pd.Series([1, 5]), pd.Series([3, 9]), pd.Series([4, 12])])
    """)
    data_frame = pd.DataFrame([pd.Series([1, 5]), pd.Series([3, 9]), pd.Series([4, 12])])
    print(data_frame)

    # create a DataFrame from a list of Series with column names
    print("\nCreate a DataFrame from a list of Series with column names")
    print("""
    command:
    data_frame = pd.DataFrame(
        [pd.Series([1, 5], name="X"),
        pd.Series([3, 9], name="Y"),
        pd.Series([4, 12], name="Z")])
    """)
    data_frame = pd.DataFrame([pd.Series([1, 5], index=["A", "B"]), \
        pd.Series([3, 9], index=["A", "B"]), pd.Series([4, 12], index=["A", "B"])])
    print(data_frame)

    print("\nCreate a DataFrame from a list of Series with column names and index")
    print("""
    command:
    data_frame = pd.DataFrame(
        [pd.Series([1, 5], index=["A", "B"], name="X"),
        pd.Series([3, 9], index=["A", "B"], name="Y"),
        pd.Series([4, 12], index=["A", "B"], name="Z")])
    """)
    data_frame = pd.DataFrame([pd.Series([1, 5], index=["A", "B"], name="X"), \
        pd.Series([3, 9], index=["A", "B"], name="Y"), pd.Series([4, 12], index=["A", "B"], name="Z")])
    print(data_frame)

    #Create a sample DataFrame
    print("\nCreate a sample DataFrame for melting")
    data_frame = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Math': [90, 75, 80],
        'Science': [95, 80, 85],
        'English': [92, 85, 90]
    })
    print("Created DataFrame:")
    print(data_frame)

    # Melt the DataFrame
    melted_df = pd.melt(data_frame, id_vars=['Name'], var_name='Subject', value_name='Score')

    # Print the melted DataFrame
    print("\nMelted DataFrame:")
    print(melted_df)

    #Access a DataFrame with a boolean index
    #In boolean indexing, we filter data with a boolean vector.
    # dictionary of lists
    print("\nAccess a DataFrame with a boolean index")
    dict = {'name':["name1", "name2", "name3", "name4"],
        'degree': ["degree1", "degree2", "degree3", "degree4"],
        'score':[1, 2, 3, 4]}
    print("Created dictionary:")
    print(dict)

    #Create a DataFrame
    df = pd.DataFrame(dict, index = [True, False, True, False])
    print("\nCreated DataFrame:")
    print(df)

    print("\nAll Done!")

# check if script is run as main program
if __name__ == "__main__":
    # execute only if run as a script
    main()
