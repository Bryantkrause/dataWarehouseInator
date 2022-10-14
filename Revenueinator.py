import pandas as pd
import numpy as np
from sqlalchemy import column
import datetime

useColumns = [
    'Unnamed: 0', 'Date', 'Num', 'Memo', 'Name', 'Amount'
]
# Get Files
file = r'C:\Users\bkrause\Documents\RevenueRaw1012222.CSV'
updatedFile = r'C:\Users\bkrause\Documents\refinedRev.xlsx'
cNFile = 'CustomerNumbers.csv'
subFile = 'SubTypes.csv'
locFile = 'Location.csv'
# create data frame only use needed data
df = pd.read_csv(file, usecols=useColumns, parse_dates=["Date"])
columnNames = [
    'Category', 'Date', 'InvoiceNumber', 'Memo', 'Name', 'Amount'
]
df.columns = columnNames
df['Category'] = df['Category'].fillna(method='ffill')
# remove totals and rows with out amount
df = df.dropna(subset=['Date'])
df = df[df.Amount != 0]


conditions = [
    df['Category'].str.contains(
        r'Bank Fee', na=False),
    df['Category'].str.contains(
        r'Administrative', na=False),
    df['Category'].str.contains(
        r'EDI Fees', na=False),
    df['Category'].str.contains(
        r'Rescheduing Fee', na=False),
    df['Category'].str.contains(
        r'Rescheduling fee', na=False),
    df['Category'].str.contains(
        r'Delv Service', na=False),
    df['Category'].str.contains(
        r'Dray La Mirada', na=False),
    df['Category'].str.contains(
        r'Inbound Handling', na=False),
    df['Category'].str.contains(
        r'OF Inbound Handling', na=False),
    df['Category'].str.contains(
        r'MTRLS', na=False),
    df['Category'].str.contains(
        r'OF Outbound Handling', na=False),
    df['Category'].str.contains(
        r'Outbound Handling', na=False),
    df['Category'].str.contains(
        r'Product Handling Services', na=False),
    df['Category'].str.contains(
        r'Fedex', na=False),
    df['Category'].str.contains(
        r'Postage', na=False),
    df['Category'].str.contains(
        r'Rework', na=False),
    df['Category'].str.contains(
        r'Minimum Monthly', na=False),
    df['Category'].str.contains(
        r'Re-Occurring Storage: Overflow', na=False),
    df['Category'].str.contains(
        r'Re-Occurring Storage', na=False),
    df['Category'].str.contains(
        r'Re-Occuring Storage: Cerritos', na=False),
    df['Category'].str.contains(
        r'Re-Occurring Storage', na=False)
]

choices = [
    'Clerical',
    'Clerical',
    'Clerical',
    'Clerical',
    'Clerical',
    'Drayage',
    'Drayage',
    'Inbound',
    'Inbound',
    'Materials',
    'Outbound',
    'Outbound',
    'Outbound',
    'Postage',
    'Postage',
    'Rework',
    'Storage',
    'Storage',
    'Storage',
    'Storage',
    'Storage'
]
print(len(conditions))
print(len(choices))
df['CategoryType'] = np.select(conditions, choices, default='None')
cnDF = pd.read_csv(cNFile)


df = df.merge(cnDF, how='left')
subDF = pd.read_csv(subFile)
df = df.merge(subDF, how='left')

# convert date of invoicing to date of activity
def vec_dt_replace(series, year=None, month=None, day=None):
    return pd.to_datetime(
        {'year': series.dt.year if year is None else year,
         'month': series.dt.month if month is None else month,
         'day': series.dt.day if day is None else day})

df.Date = vec_dt_replace(df.Date, day=1) - pd.Timedelta(days=1)


df['Month'] = pd.DatetimeIndex(df['Date']).month
df['Year'] = pd.DatetimeIndex(df['Date']).year

# need to convert month to previous month
locDF = pd.read_csv(locFile)
print(df.head())
print(locDF.head())

df = df.merge(locDF, on=['Number', 'Month'],  how='left')
print(df.head())
print(df.info())

writer = pd.ExcelWriter(updatedFile, engine='xlsxwriter')
df.to_excel(writer, sheet_name='Revenue')
writer.close()
