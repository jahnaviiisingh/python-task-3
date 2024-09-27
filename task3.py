import yfinance as yf
import pandas as pd

class PortfolioTracker:
    def __init__(self):
        self.portfolio = pd.DataFrame(columns=['Ticker', 'Quantity'])

    def add_stock(self, ticker, quantity):
        self.portfolio = self.portfolio.append({'Ticker': ticker, 'Quantity': quantity}, ignore_index=True)

    def remove_stock(self, ticker):
        self.portfolio = self.portfolio[self.portfolio['Ticker'] != ticker]

    def update_stock_quantity(self, ticker, quantity):
        self.portfolio.loc[self.portfolio['Ticker'] == ticker, 'Quantity'] = quantity

    def get_stock_price(self, ticker):
        stock = yf.Ticker(ticker)
        price = stock.history(period='1d')['Close'].iloc[-1]
        return price

    def get_portfolio_value(self):
        self.portfolio['Price'] = self.portfolio['Ticker'].apply(self.get_stock_price)
        self.portfolio['Value'] = self.portfolio['Quantity'] * self.portfolio['Price']
        total_value = self.portfolio['Value'].sum()
        return self.portfolio, total_value

def main():
    tracker = PortfolioTracker()

    # Add stocks to portfolio
    tracker.add_stock('AAPL', 10)
    tracker.add_stock('GOOGL', 5)

    # Display portfolio value
    portfolio, total_value = tracker.get_portfolio_value()
    print("\nCurrent Portfolio:")
    print(portfolio[['Ticker', 'Quantity', 'Price', 'Value']])
    print(f"\nTotal Portfolio Value: ${total_value:.2f}")

    # Example of updating stock quantity
    tracker.update_stock_quantity('AAPL', 15)
    
    # Example of removing a stock
    tracker.remove_stock('GOOGL')

    # Display updated portfolio value
    portfolio, total_value = tracker.get_portfolio_value()
    print("\nUpdated Portfolio:")
    print(portfolio[['Ticker', 'Quantity', 'Price', 'Value']])
    print(f"\nTotal Portfolio Value: ${total_value:.2f}")

if __name__ == "__main__":
    main()
