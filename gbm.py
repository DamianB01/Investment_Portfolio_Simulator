import numpy as np

def monte_carlo(S0, mu, sigma, T, n_sims, dt=1/252):
    n_steps = int(T / dt)
    z = np.random.normal(0, 1, (n_steps, n_sims))
    drift = (mu - 0.5 * sigma ** 2) * dt
    shock = sigma * np.sqrt(dt) * z
    log_returns = drift + shock
    price_paths = S0 * np.exp(np.cumsum(log_returns, axis=0))
    return price_paths

