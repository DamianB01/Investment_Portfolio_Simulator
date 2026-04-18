import yfinance as yf
import numpy as np

def load_market_data(ticker="AAPL", period="5y"):
    data = yf.download(ticker, period=period)
    prices = data["Close"].squeeze()
    log_returns = np.log(prices / prices.shift(1)).dropna()    #yfinance uses pandas, so dropna() is included there
    mu = (log_returns.mean() * 252).item()      #annualized return
    sigma = (log_returns.std() * np.sqrt(252)).item()  #annualized volatility
    return prices, mu, sigma
