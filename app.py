import yfinance as yf
from datetime import date, datetime
import pandas as pd

acao = ['PETR4.SA','MGLU3.SA']

data_incial = "2024-06-01"
data_final = date.today()

for a in acao:
  data = yf.download(a, start=data_incial, end=data_final, progress=False) 
  df = pd.DataFrame(data)
  df['name'] = a
  df.to_csv(f'{a}-{date.today()}.csv')

  
 


 
