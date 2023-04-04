"""This script creates graphs from the titanic dataset."""
import pandas as pd
import matplotlib.pyplot as plt

def main():
    """Main entry point of the app."""
    print("Pandas graphs")
    # Load the dataset
    titanic_df = pd.read_csv('/inputs/titanic.csv')

    # Create a bar chart of passenger class counts
    print("\nCreating a bar chart of passenger class counts...")
    class_counts = titanic_df['Pclass'].value_counts()
    class_counts.plot(kind='bar')
    plt.title('Passenger Class Counts')
    plt.xlabel('Class')
    plt.ylabel('Count')
    # saving the plot to a png file
    plt.savefig('/outputs/passenger_class_counts.png')

    # Create a histogram of passenger ages
    print("\nCreating a histogram of passenger ages...")
    titanic_df['Age'].hist(bins=20)
    plt.title('Passenger Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Count')
    # saving the plot to a png file
    plt.savefig('/outputs/passenger_age_distribution.png')

    # Create a scatter plot of passenger ages and fares
    print("\nCreating a scatter plot of passenger ages and fares...")
    plt.scatter(titanic_df['Age'], titanic_df['Fare'])
    plt.title('Passenger Age vs. Fare')
    plt.xlabel('Age')
    plt.ylabel('Fare')
    # saving the plot to a png file
    plt.savefig('/outputs/passenger_age_vs_fare.png')

    # Create a pie chart of passenger survival rates
    print("\nCreating a pie chart of passenger survival rates...")
    survival_counts = titanic_df['Survived'].value_counts()
    survival_counts.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Passenger Survival Rates')
    plt.legend(['Died', 'Survived'])
    # saving the plot to a png file
    plt.savefig('/outputs/passenger_survival_rates.png')

# check if script is run as main
if __name__ == "__main__":
    main()
