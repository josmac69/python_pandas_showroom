"""
This script shows usage of pandas for financial analysis.
"""
import pandas as pd
import pandas_datareader as pdr

def main():
    """Main entry point of the app."""
    # Download stock prices from Yahoo! Finance
    print("Downloading stock prices from Yahoo! Finance...")
    df = pdr.get_data_yahoo('AAPL', start='2021-01-01', end='2022-01-01')

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
