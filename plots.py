import matplotlib.pyplot as plt

def plot_paths(results):
    plt.figure()
    plt.plot(results[:, :100])
    plt.title("Monte Carlo Portfolio Paths")
    plt.xlabel("Days")
    plt.ylabel("Portfolio Value")
    plt.show()

def plot_histogram(final_prices, start_cash):
    plt.figure()
    plt.hist(final_prices, bins=100)
    plt.axvline(start_cash, color='red', linestyle='--')
    plt.title("Final Portfolio Distribution")
    plt.show()

def plot_bands(p10, p50, p90):
    plt.figure()
    plt.plot(p10, label="10% worst")
    plt.plot(p50, label="median")
    plt.plot(p90, label="90% best")
    plt.legend()
    plt.title("Confidence Bands")
    plt.show()

def plot_real_prices(prices):
    plt.figure()
    plt.plot(prices)
    plt.title("Real Market Data")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.show()
