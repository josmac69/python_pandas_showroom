"""
This script shows usage of pandas for financial analysis.
"""
import pandas as pd
#import pandas_datareader as pdr # uncomment to download data from Yahoo! Finance

def main():
    """Main entry point of the app."""
    # Download stock prices from Yahoo! Finance
    print("You can download stock prices from Yahoo! Finance using pandas_datareader.")
    print("""command: df = pdr.get_data_yahoo('AAPL', start='YYYY-MM-DD', end='YYYY-MM-DD')""")
    print("For this example running in docker container, we will use already downloaded data.")

    # Read data from CSV file
    print("\nReading data from CSV file...")
    df = pd.read_csv('/inputs/AAPL.csv', index_col='Date', parse_dates=True)

    # Calculate rolling mean and standard deviation
    print("\nCalculating rolling mean and standard deviation...")
    df['Rolling Mean'] = df['Adj Close'].rolling(window=30).mean()
    df['Rolling Std'] = df['Adj Close'].rolling(window=30).std()

    # Calculate daily returns
    print("\nCalculating daily returns...")
    df['Daily Return'] = df['Adj Close'].pct_change()

    # Calculate cumulative returns
    print("\nCalculating cumulative returns...")
    df['Cumulative Return'] = (1 + df['Daily Return']).cumprod()

    # Resample data at a monthly frequency
    print("\nResampling data at a monthly frequency...")
    df_monthly = df.resample('M').last()

    # Print the final DataFrame
    print("\nPrinting the final DataFrame...")
    print(df_monthly)

# check if script is run as main
if __name__ == "__main__":
    main()
