# 20-Day Rolling Volatility

20-day volatility measures an asset's short-term price fluctuations over a trailing one-month period, acting as a real-time gauge of market stress or calm.

## Why a 20-day window?

- A 20-day window represents one trading month, balancing responsiveness with the statistical relevance of the data.
- It spikes quickly during market sell-offs, liquidity crunches, or macroeconomic shocks.
- Rolling it forward daily reveals whether market stability is breaking down or returning.

## Practical uses in finance

- **Position sizing:** Traders can adjust leverage or capital allocation as short-term risk expands or contracts.
- **Option pricing:** Informs near-term derivative pricing and comparison against implied volatility.
- **Regime identification:** Helps classify market phases into distinct periods, such as "tranquil" or "volatile" (e.g., the 2008 financial crisis).

## What this project does

I calculated a moving 20-day rolling volatility and plotted it using three different languages: Python (yfinance, pandas, sqlite3), R (quantmod, zoo, xts), and SQL. Python was the easiest to work in, since it's the language I'm most confident with and has great packages for pulling the data I needed — I also used it to load the results into SQL. R was more challenging: I didn't write my own functions, and the syntax felt less intuitive to me. Overall, Python felt the most natural for quick data wrangling, SQL felt natural for structuring and querying the results once they existed, and R felt the least natural of the three — its vectorized, package-driven style took more getting used to than writing the equivalent logic in Python.
