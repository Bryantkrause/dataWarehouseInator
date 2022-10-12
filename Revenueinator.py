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
        r'Bank Fee (ACH/Wire Bank Fee)', na=False),
    df['Category'].str.contains(
        r'CH (Administrative Support)', na=False),
    df['Category'].str.contains(
        r'EDI (EDI Fees)', na=False),
    df['Category'].str.contains(
        r'Rescheduing Fee (Rescheduling fee)', na=False),
    df['Category'].str.contains(
        r'Rescheduing Fee (Rescheduling fee)', na=False),
    df['Category'].str.contains(
        r'Rescheduling fee (Rescheduling fee)', na=False),
    df['Category'].str.contains(
        r'Delv Service (Transportation Services)', na=False),
    df['Category'].str.contains(
        r'Dray La Mirada (Drayage Container:)', na=False),
    df['Category'].str.contains(
        r'Inbound Handling - PH (Inbound Handling)', na=False),
    df['Category'].str.contains(
        r'OF Inbound Handling - PH (Inbound Handling: Overflow)', na=False),
    df['Category'].str.contains(
        r'MTRLS (Materials Supplied)', na=False),
    df['Category'].str.contains(
        r'OF Outbound Handling - PH (Outbound Handling:', na=False),
    df['Category'].str.contains(
        r'PH (Product Handling Services) - Other', na=False),
    df['Category'].str.contains(
        r'Fedex (Fedex Services)', na=False),
    df['Category'].str.contains(
        r'Postage', na=False),
    df['Category'].str.contains(
        r'Rework (Rework)', na=False),
    df['Category'].str.contains(
        r'MO MIN (Minimum Monthly Service Charge)', na=False),
    df['Category'].str.contains(
        r'OF PS (Re-Occurring Storage: Overflow)', na=False),
    df['Category'].str.contains(
        r'PS (Re-Occurring Storage) - Other', na=False),
    df['Category'].str.contains(
        r'PS (Re-Occurring Storage) - Other', na=False),

]

choices = [
    'Clerical', 'Clerical',
    'Clerical', 'Clerical',
    'Clerical', 'Drayage',
    'Drayage', 'Inbound',
    'Inbound', 'Materials',
    'Outbound', 'Outbound',
    'Outbound', 'Postage',
    'Postage', 'Rework',
    'Storage', 'Storage',
    'Storage', 'Storage',
    'Storage'
]

df['CategoryType'] = np.select(conditions, choices, default='None')
# df = df[~df.Category.str.contains("Total")]
# df = df[df['Category'] != 'Total']

print(df.head())
print(df.info())

writer = pd.ExcelWriter(updatedFile, engine='xlsxwriter')
df.to_excel(writer, sheet_name='Revenue')
writer.close()
