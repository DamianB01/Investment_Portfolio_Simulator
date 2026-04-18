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
- $\mu$ = expected return (drift)
- $\sigma$ = volatility
- $W_t$ = Wiener process (randomness)

---

## 📉 Risk Metrics


| Metric | Description |
| :--- | :--- |
| 📊 **Expected Return** | Average simulated portfolio outcome |
| ⚠️ **VaR (95%)** | Worst-case loss in 5% scenarios |
| 📉 **Loss Probability** | Probability of ending with negative return |
| 📈 **Sharpe Ratio** | Risk-adjusted return |
| 📉 **Max Drawdown** | Maximum peak-to-trough loss |

---

## 📁 Output Files

`simulation_summary.csv` → final results per simulation

---

## 🧪 Run Tests

Type in bash in the project directory:  
`python -m unittest discover unit_tests`  

---

## ▶️ Usage Examples (Screenshots)

<img width="627" height="471" alt="Zrzut ekranu 2026-04-19 000613" src="https://github.com/user-attachments/assets/4dcf2a86-8fd5-4a5d-92a5-3307f906ff62" />  
<img width="679" height="465" alt="Zrzut ekranu 2026-04-19 000628" src="https://github.com/user-attachments/assets/cc775a32-068d-4d66-af0d-5c3635682d46" />  
<img width="626" height="465" alt="Zrzut ekranu 2026-04-19 000638" src="https://github.com/user-attachments/assets/8396fd1f-5e71-40ab-9aa3-9dffe65293dc" />  
<img width="624" height="452" alt="Zrzut ekranu 2026-04-19 000646" src="https://github.com/user-attachments/assets/a0d452d4-df0c-4fc8-bdd1-5f9227be2b1f" />  
  
<img width="561" height="274" alt="Zrzut ekranu 2026-04-19 000721" src="https://github.com/user-attachments/assets/b34eaf3f-148c-4471-9ed7-56ef2056a49a" />  
  
<img width="522" height="106" alt="image" src="https://github.com/user-attachments/assets/e254560b-4008-42a1-8083-45b7065cfaf6" />  

---

## ⭐ If you like this project

## Give it a ⭐ on GitHub — it helps!
