"""
This script creates graphs from the titanic dataset using matplotlib library.
"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

def main():
    """Main entry point of the app."""
    print("Pandas graphs using matpotlib")
    # Load the dataset from excel file into a pandas dataframe
    titanic_df = pd.read_excel('/inputs/titanic3.xls')

    # Create a bar chart of passenger class counts
    print("\nCreating a bar chart of passenger class counts...")
    class_counts = titanic_df['pclass'].value_counts()
    class_counts.plot(kind='bar')
    plt.title('Passenger Class Counts')
    plt.xlabel('Class')
    plt.ylabel('Count')
    # saving the plot to a png file
    plt.savefig('/outputs/matplotlib_passenger_class_counts.png')

    # Create a histogram of passenger ages
    print("\nCreating a histogram of passenger ages...")
    titanic_df['age'].hist(bins=20)
    plt.title('Passenger Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Count')
    # saving the plot to a png file
    plt.savefig('/outputs/matplotlib_passenger_age_distribution.png')

    # Create a scatter plot of passenger ages and fares
    print("\nCreating a scatter plot of passenger ages and fares...")
    plt.scatter(titanic_df['age'], titanic_df['fare'])
    plt.title('Passenger Age vs. Fare')
    plt.xlabel('Age')
    plt.ylabel('Fare')
    # saving the plot to a png file
    plt.savefig('/outputs/matplotlib_passenger_age_vs_fare.png')

    # Create a pie chart of passenger survival rates
    print("\nCreating a pie chart of passenger survival rates...")
    survival_counts = titanic_df['survived'].value_counts()
    survival_counts.plot(kind='pie',
                        autopct='%1.1f%%',
                        startangle=90,
                        explode=[0, 0.1],
                        shadow=True,
                        labels=['Died', 'Survived'],
                        colors=['lightcoral', 'lightskyblue'],
                        pctdistance=1.1,
                        textprops={'fontsize': 14, 'fontweight': 'bold'})
    plt.title('Passenger Survival Rates')
    plt.legend(['Died', 'Survived'], loc='upper left', bbox_to_anchor=(1.2, 0.8))
    # saving the plot to a png file
    plt.savefig('/outputs/matplotlib_passenger_survival_rates.png')

    # Create a pie chart of passenger survival rates
    print("\nCreating a pie chart of passenger survival rates...")
    labels = ['Died', 'Survived']
    survival_counts = titanic_df['survived'].value_counts()
    print(survival_counts)
    colors = ['lightcoral', 'lightskyblue']
    legend_labels = ['{0} - {1} ({2:1.2f}%)'.format(i, j, k) \
                    for i,j,k in zip(labels, survival_counts, \
                    [x/sum(survival_counts)*100 for x in survival_counts])]
    legend_patches = \
        [Patch(color=color, label=label) for color, label in zip(colors, legend_labels)]
    plt.pie(survival_counts,
            labels=labels,
            colors=colors,
            autopct='%1.1f%%',
            pctdistance=0.5,
            labeldistance=0.1,
            startangle=90,
            explode=[0, 0.1],
            shadow=True,
            wedgeprops={'linewidth': 0.5, 'edgecolor': 'black'},
            textprops={'fontsize': 12, 'fontweight': 'bold'}
            )
    plt.title('Passenger Survival Rates')
    plt.legend(handles=legend_patches,
               loc='upper left',
               bbox_to_anchor=(0,1),
               frameon=False)
    # saving the plot to a png file
    plt.savefig('/outputs/matplotlib_passenger_survival_rates_v2.png')

# check if script is run as main
if __name__ == "__main__":
    main()
