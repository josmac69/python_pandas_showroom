"""
This script creates graphs from the titanic dataset
using matplotlib and seaborn libraries.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import xlrd

def main():
    """Main entry point of the app."""
    print("Pandas graphs using matpotlib")
    # Load the dataset from excel file into a pandas dataframe
    titanic_df = pd.read_excel('/inputs/titanic3.xls')

    # Histogram of passenger ages
    sns.histplot(data=titanic_df, x="age", bins=20)
    plt.title('Passenger Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.show()

    # Bar chart of passenger classes
    sns.countplot(data=titanic_df, x="pclass")
    plt.title('Passenger Class Counts')
    plt.xlabel('Class')
    plt.ylabel('Count')
    plt.show()

    # Scatter plot of passenger ages and fares
    sns.scatterplot(data=titanic_df, x="age", y="fare", hue="pclass")
    plt.title('Passenger Age vs. Fare by Class')
    plt.xlabel('Age')
    plt.ylabel('Fare')
    plt.show()

    # Box plot of passenger ages by class and sex
    sns.boxplot(data=titanic_df, x="pclass", y="age", hue="sex")
    plt.title('Passenger Age Distribution by Class and Sex')
    plt.xlabel('Class')
    plt.ylabel('Age')
    plt.show()

    # Violin plot of passenger ages by class and sex
    sns.violinplot(data=titanic_df, x="pclass", y="age", hue="sex")
    plt.title('Passenger Age Distribution by Class and Sex')
    plt.xlabel('Class')
    plt.ylabel('Age')
    plt.show()

    # Heatmap of passenger survival rates by class and sex
    survival_rates = titanic_df.pivot_table(index='class', columns='sex', values='survived', aggfunc='mean')
    sns.heatmap(survival_rates, annot=True, cmap="YlGnBu")
    plt.title('Passenger Survival Rates by Class and Sex')
    plt.xlabel('Sex')
    plt.ylabel('Class')
    plt.show()

    # Pair plot of passenger ages, fares, and survival status
    sns.pairplot(data=titanic_df, vars=["age", "fare"], hue="survived")
    plt.show()

# check if script is run as main
if __name__ == "__main__":
    main()
