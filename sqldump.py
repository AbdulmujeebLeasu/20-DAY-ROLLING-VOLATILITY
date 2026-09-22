import sqlite3
import csv

conn = sqlite3.connect('20drv.sqlite')
cur = conn.cursor()

cur.executescript('''
                  DROP TABLE IF EXISTS '20 DAY ROLLING VOLATILITY'
                  ''')

cur.executescript('''CREATE TABLE '20 DAY ROLLING VOLATILITY'(
                      Date DATE NOT NULL,
                      Close DECIMAL,
                      'Log Return' DECIMAL,
                      Volatility DECIMAL,
                      'Annualized Volatility' DECIMAL,
                      PRIMARY KEY (Date)
                  )''')

fname = input("Enter file name: ")
if len(fname) < 1:
    fname == 'resultsMU.csv'
    
with open(fname, mode = 'r', encoding = 'utf8') as file:
    csv_reader = csv.reader(file)
    
    next(csv_reader)
    
    cur.executemany(''' INSERT INTO '20 DAY ROLLING VOLATILITY'
                        ( Date , Close , 'Log Return' , Volatility , 'Annualized Volatility' )
                        VALUES ( ? , ? , ? , ? , ? )
                    ''', csv_reader)
    
conn.commit()
conn.close()