import pandas as pd

def save_results(results, start_cash=None, filename="simulation_summary.csv"):
    final_prices = results[-1]
    df = pd.DataFrame({"simulation_id": range(len(final_prices)), "final_value": final_prices,})
    if start_cash is not None:
        df["return_%"] = (final_prices - start_cash) / start_cash * 100
    df.to_csv(filename, index=False, sep=';')
