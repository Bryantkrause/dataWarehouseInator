import pandas as pd
from dotenv import load_dotenv
import os
from pandas.io import sql
from sqlalchemy import create_engine

db = os.environ.get("database")
pw = os.environ.get("pw")

file = r"C:\Users\bkrause\Desktop\Data101\SeedData.csv"
columns = [
    'Voucher #',
    'Date',
    'Vendor',
    'Ref #',
    'Line',
    'Item ID',
    'Description',
    'Quantity',
    'U/M',
    'Price',
    'Tax',
    'Amount',
    'Taxes',
    'Total base',
    'Account',
    'Group',
    'Tag',
    'Memo',
    'Comments',
    'Approvers',
    'Approval Status'
]

df = pd.read_csv(file, usecols=columns, parse_dates=["Date"])

df.rename(columns={
    'Voucher #': 'Voucher',
    'Ref #':'PurchaseOrder',
    'Item ID': 'ItemID',
    'U/M': 'Unit',
    'Total base': 'TotalBase',
    'Approval Status': 'ApprovalStatus'},
    inplace=True)
print(df.head())
print(df.info())
print(df.describe())

df['Unit'].fillna("Blank", inplace=True)
df['Taxes'].fillna("0.0", inplace=True)
df['Memo'].fillna("0.0", inplace=True)
df['Comments'].fillna("0.0", inplace=True)
df['Approvers'].fillna("0.0", inplace=True)
df['PurchaseOrder'].fillna("0.0", inplace=True)
print(df.info())
print(df.describe())

database_connection = create_engine(f'mysql://root:{pw}@localhost/{db}')
df.to_sql(con=database_connection,
          name='rawdata', if_exists='replace')

