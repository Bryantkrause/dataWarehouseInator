import pandas as pd
import numpy as np
from sqlalchemy import column


useColumns = [
    'Unnamed: 0', 'Date', 'Num', 'Memo', 'Name', 'Amount'
]
file = r'C:\Users\bkrause\Documents\RevenueRaw1012222.CSV'
updatedFile = r'C:\Users\bkrause\Documents\refinedRev.xlsx'
df = pd.read_csv(file, usecols=useColumns, parse_dates=["Date"])
columnNames = [
    'Category', 'Date', 'InvoiceNumber', 'Memo', 'Name', 'Amount'
]
df.columns = columnNames
df['Category'] = df['Category'].fillna(method='ffill')
df = df.dropna(subset=['Date'])
# df = df[df['Category'].str.contains("Total")==False]
# df = df[~df.Category.str.contains("Total")]
# df = df[df['Category'] != 'Total']

print(df.head())
print(df.info())

writer = pd.ExcelWriter(updatedFile, engine='xlsxwriter')
df.to_excel(writer, sheet_name='Revenue')
writer.close()
