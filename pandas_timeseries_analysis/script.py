"""
This script demonstrates time series analysis using pandas.
"""
import pandas as pd
import numpy as np

def main():
    """Main entry point of the app."""
    # Create a pandas series with datetime index
    print("Creating a pandas series with datetime index...")
    dates = pd.date_range(start='2020-01-01', end='2020-01-31')
    sales = pd.Series(np.random.randint(1, 10, len(dates)), index=dates)

    # Resample the data to weekly frequency and compute the sum
    print("\nResampling the data to weekly frequency and computing the sum...")
    weekly_sales = sales.resample('W').sum()

    # Shift the data by one week and compute the difference
    print("\nShifting the data by one week and computing the difference...")
    shifted_sales = weekly_sales.shift(1)
    sales_diff = weekly_sales - shifted_sales

    # Compute the rolling mean of the data with a window size of 3
    print("\nComputing the rolling mean of the data with a window size of 3...")
    rolling_mean = sales.rolling(window=3).mean()

    # Print the results
    print("\nPrinting the results...")
    print("\nOriginal sales data:\n", sales)
    print("\nWeekly sales data:\n", weekly_sales)
    print("\nShifted sales data:\n", shifted_sales)
    print("\nDifference in weekly sales data:\n", sales_diff)
    print("\nRolling mean of sales data:\n", rolling_mean)

# check if script is run as main
if __name__ == "__main__":
    main()
