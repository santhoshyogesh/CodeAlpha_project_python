import yfinance as yf
import pandas as pd

# Define your portfolio
portfolio = {
    'AAPL': 10,  # 10 shares of Apple
    'MSFT': 5,   # 5 shares of Microsoft
    'GOOGL': 2   # 2 shares of Google
}

# Fetch stock data for multiple tickers at once
def fetch_stock_data(tickers):
    return yf.download(tickers, group_by='ticker')

# Calculate the portfolio value
def calculate_portfolio_value(portfolio):
    total_value = 0
    tickers = list(portfolio.keys())
    stock_data = fetch_stock_data(tickers)

    for ticker, shares in portfolio.items():
        current_price = stock_data[ticker]['Close'].iloc[-1]  # Get the latest closing price
        total_value += current_price * shares
        print(f"{ticker}: {shares} shares at ${current_price:.2f} each")
    
    return total_value

# Main function
if __name__ == "__main__":
    total_value = calculate_portfolio_value(portfolio)
    print(f"Total Portfolio Value: ${total_value:.2f}")
