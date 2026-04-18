# 📈 Investment Portfolio Simulator (Monte Carlo + Real Market Data)



---

## 🧠 Overview

This project is a **Monte Carlo-based investment portfolio simulator** built in Python.  
It uses **real market data** to estimate risk and return distributions using stochastic modeling.

The system simulates thousands of possible future price paths using **Geometric Brownian Motion (GBM)** and evaluates portfolio risk using financial metrics.

---

## 🚀 Features

- 📊 Monte Carlo simulation of asset prices (GBM model)  
- 📉 Real market data integration via Yahoo Finance  
- ⚖️ Risk metrics:  
  - Expected return  
  - Value at Risk (VaR 95%)  
  - Sharpe Ratio  
  - Maximum Drawdown  
- 📈 Visualization:  
  - Price path simulations  
  - Histogram of outcomes  
  - Confidence bands  
- 💾 CSV export (clean financial reporting format)  
- 🧪 Unit testing with `unittest`  
- 🧩 Modular architecture (simulation / analysis / data / tests)  

---

## 📊 Model Description

The simulation is based on **Geometric Brownian Motion (GBM)**:

$$
S(t) = S_0 \cdot e^{(\mu - \frac{1}{2}\sigma^2)t + \sigma W_t}
$$

Where:
- \( \mu \) = expected return (drift)
- \( \sigma \) = volatility
- \( W_t \) = Wiener process (randomness)

---

## 📉 Risk Metrics

## 📉 Risk Metrics


| Metric | Description |
| :--- | :--- |
| 📊 **Expected Return** | Average simulated portfolio outcome |
| ⚠️ **VaR (95%)** | Worst-case loss in 5% scenarios |
| 📈 **Sharpe Ratio** | Risk-adjusted return |
| 📉 **Max Drawdown** | Maximum peak-to-trough loss |

---

## 📁 Output Files

simulation_summary.csv → final results per simulation

---

## 🧪 Run Tests

Type in bash in the project directory:  
python -m unittest discover unit_tests  

---

## ⭐ If you like this project

## Give it a ⭐ on GitHub — it helps!
