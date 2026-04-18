from config import *
from gbm import monte_carlo
from metrics import *
from plots import *
from csv_export import save_results
from market_data import load_market_data

prices, mu, sigma = load_market_data("AAPL")
print(f"Real mu: {mu:.4f}")
print(f"Real sigma: {sigma:.4f}")

results = monte_carlo(START_CASH, mu, sigma, YEARS, SIMULATIONS, DT)
final_prices = results[-1]

print("\n--- PORTFOLIO REPORT ---")
print("Expected return:", expected_return(final_prices, START_CASH))
print("VaR 95%:", var_95(final_prices, START_CASH))
print(f"Loss probability: {probability_loss(final_prices, START_CASH)}%")
print("Sharpe:", sharpe_ratio(final_prices, START_CASH))
mdd = max_drawdown(results[:, 0])
print("Max Drawdown:", mdd)

plot_real_prices(prices)
plot_paths(results)
plot_histogram(final_prices, START_CASH)
p10, p50, p90 = confidence_bands(results)
plot_bands(p10, p50, p90)

save_results(results, START_CASH)
print("\nSaved to CSV")
