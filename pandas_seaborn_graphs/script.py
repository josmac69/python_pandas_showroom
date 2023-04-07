"""
This script creates graphs from the titanic dataset
using matplotlib and seaborn libraries.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    """Main entry point of the app."""
    print("Pandas graphs using matpotlib")
    # Load the dataset from excel file into a pandas dataframe
    print("\nLoading titanic dataset from excel file...")
    titanic_df = pd.read_excel('/inputs/titanic3.xls')

    # Histogram of passenger ages
    print("\nCreating histogram of passenger ages...")
    sns.histplot(data=titanic_df, x="age", bins=20)
    plt.title('Passenger Age Distribution')
    plt.xlabel('age')
    plt.ylabel('count')
    plt.savefig('/outputs/seaborn_passengers_histogram_of_ages.png')

    # Bar chart of passenger classes
    print("\nCreating bar chart of passenger classes...")
    sns.countplot(data=titanic_df, x="pclass")
    plt.title('Passenger Class Counts')
    plt.xlabel('pclass')
    plt.ylabel('count')
    plt.savefig('/outputs/seaborn_passengers_bar_chart_of_classes.png')

    # Scatter plot of passenger ages and fares
    print("\nCreating scatter plot of passenger ages and fares...")
    sns.scatterplot(data=titanic_df, x="age", y="fare", hue="pclass")
    plt.title('Passenger Age vs. Fare by Class')
    plt.xlabel('age')
    plt.ylabel('fare')
    plt.savefig('/outputs/seaborn_passengers_scatter_plot_of_ages_and_fares.png')

    # Box plot of passenger ages by class and sex
    print("\nBox plot of passenger ages by class and sex...")
    sns.boxplot(data=titanic_df, x="pclass", y="age", hue="sex")
    plt.title('Passenger Age Distribution by Class and Sex')
    plt.xlabel('pclass')
    plt.ylabel('age')
    plt.savefig('/outputs/seaborn_passengers_box_plot_ages_by_class_and_sex.png')

    # Violin plot of passenger ages by class and sex
    print("\nBox plot of passenger ages by class and sex...")
    sns.violinplot(data=titanic_df, x="pclass", y="age", hue="sex")
    plt.title('Passenger Age Distribution by Class and Sex')
    plt.xlabel('pclass')
    plt.ylabel('age')
    plt.savefig('/outputs/seaborn_passengers_violin_plot_ages_by_class_and_sex.png')

    # Heatmap of passenger survival rates by class and sex
    print("\nHeatmap of passenger survival rates by class and sex...")
    survival_rates = titanic_df.pivot_table(index='pclass',
                                            columns='sex',
                                            values='survived',
                                            aggfunc='mean')
    sns.heatmap(survival_rates, annot=True, cmap="YlGnBu")
    plt.title('Passenger Survival Rates by Class and Sex')
    plt.xlabel('sex')
    plt.ylabel('pclass')
    plt.savefig('/outputs/seaborn_passengers_heatmap_survival_rates_by_class_and_sex.png')

    # Pair plot of passenger ages, fares, and survival status
    print("\nPair plot of passenger ages, fares, and survival status...")
    sns.pairplot(data=titanic_df, vars=["age", "fare"], hue="survived")
    plt.savefig('/outputs/seaborn_passengers_pair_plot_ages_fares_survival_status.png')

# check if script is run as main
if __name__ == "__main__":
    main()
