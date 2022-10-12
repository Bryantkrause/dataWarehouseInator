import pandas as pd
import numpy as np
from sqlalchemy import column


useColumns = [
    'Unnamed: 0','Date', 'Num', 'Memo', 'Name', 'Amount'
]
file = r'C:\Users\bkrause\Documents\RevenueRaw1012222.CSV'

df = pd.read_csv(file, usecols=useColumns, parse_dates=["Date"])
columnNames = [
    'Category','Date','InvoiceNumber', 'Memo', 'Name', 'Amount'
]
df.columns = columnNames
df = df.fillna(method='ffill')

print(df.head())
print(df.info())



