import numpy as np
import pandas as pd
import yfinance as yf
 
TICKER = str(input("What stock: "))
LOOKBACK_PERIOD = "1y"
VOL_WINDOW = 20
TRADING_DAYS_PER_YEAR = 252
 
 
def fetch_close_prices(ticker: str, period: str) -> pd.Series:
    history = yf.Ticker(ticker).history(period = period)
    # Use yf.download(ticker).history(period = period) for multiple tickers
 
    if history.empty:
        raise ValueError(f"No price data returned for ticker '{ticker}'.")
 
    return history["Close"]
 
 
def compute_annualized_volatility(
    close: pd.Series,
    window: int = VOL_WINDOW,
    trading_days: int = TRADING_DAYS_PER_YEAR,
) -> pd.DataFrame:
    log_return = np.log(close / close.shift(1))
    volatility = log_return.rolling(window = window).std()
    annualized_volatility = volatility * np.sqrt(trading_days)
 
    return pd.DataFrame(
        {
            "Close": close,
            "Log Return": log_return,
            "Volatility": volatility,
            "Annualized Volatility": annualized_volatility
        }
    )
 
 
def run() -> None:
    result = compute_annualized_volatility(
        fetch_close_prices(
        TICKER, 
        LOOKBACK_PERIOD
        )
    )
    df_result = result.dropna()
    print(df_result.to_string())
    df_result.to_csv(f'results{TICKER}.csv', index=True)
 
 
run()