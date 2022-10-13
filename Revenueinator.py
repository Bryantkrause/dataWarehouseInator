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


dropme = str('01.21 (Warehousing services for the month of January 2021)')

df = df[df['Category'].str.contains(dropme) == False]

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
# df = df[~df.Category.str.contains("Total")]
# df = df[df['Category'] != 'Total']

print(df.head())
print(df.info())

writer = pd.ExcelWriter(updatedFile, engine='xlsxwriter')
df.to_excel(writer, sheet_name='Revenue')
writer.close()
