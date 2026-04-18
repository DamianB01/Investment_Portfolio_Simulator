import numpy as np

def expected_return(final_prices, start_cash):
    return np.mean(final_prices) - start_cash

def var_95(final_prices, start_cash):
    return start_cash - np.percentile(final_prices, 5)

def probability_loss(final_prices, start_cash):
    return np.mean(final_prices < start_cash) * 100

def sharpe_ratio(final_prices, start_cash):
    returns = (final_prices - start_cash) / start_cash
    return np.mean(returns) / np.std(returns)

def max_drawdown(path):
    peak = np.maximum.accumulate(path)
    drawdown = (path - peak) / peak
    return np.min(drawdown)

def confidence_bands(results):
    return (np.percentile(results, 10, axis=1),
        np.percentile(results, 50, axis=1),
        np.percentile(results, 90, axis=1),)
