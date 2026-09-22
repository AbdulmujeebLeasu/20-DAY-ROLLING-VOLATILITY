import pandas as pd
import sqlite3


fname = input("Enter the file name: ")
if len(fname) < 1:
    fname = 'resultsMU.csv' # fallbacks to a default
    
    
df = pd.read_csv(fname)

conn = sqlite3.connect("20drvp.sqlite")
cur = conn.cursor()

cur.executescript('''CREATE TABLE IF NOT EXISTS '20 DAY ROLLING VOLATILITY'(
                      Date DATE,
                      Close DECIMAL,
                      'Log Return' DECIMAL,
                      Volatility DECIMAL,
                      'Annualized Volatility' DECIMAL,
                      PRIMARY KEY (Date)
                  )''')

df.to_sql("20 DAY ROLLING VOLATILITY", conn, if_exists="replace", index=False)

conn.close()