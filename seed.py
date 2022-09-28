import pandas as pd
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
import numpy as np


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


df['Unit'].fillna("Blank", inplace=True)
df['Taxes'].fillna("0.0", inplace=True)
df['Memo'].fillna("0.0", inplace=True)
df['Comments'].fillna("0.0", inplace=True)
df['Approvers'].fillna("0.0", inplace=True)
df['PurchaseOrder'].fillna("0.0", inplace=True)
df['PrimaryKey'] = df['Voucher'] + df['Vendor'] + df['Line'].astype(str)


Item = df['ItemID'].unique()
Account = df['Account'].unique()
Group = df['Group'].unique()
Tag = df['Tag'].unique()
df['Approvers'] = df.Approvers.str.replace('[^a-zA-Z]', '')
df['Approvers'] = df['Approvers'].map(
    lambda x: x.rstrip('pending').rstrip('reject'))

Approvers = df['Approvers'].unique()

ALoc = pd.DataFrame(Approvers)
ALoc.columns
mask = ALoc['0'].str.len() < 6
ALoc2 = ALoc.loc[mask]

print(ALoc2)
appCondition = ['Cerritos', 'Rancho', 'Fullerton',
                'Downey', 'Rancho', 'Rancho', 'Rancho']
appChoice = ['FrankGuzma' ,'CarlosGarcia', 'LuisSerrano', 'HenryValdez', 'DerekFranco',
              'DavidRevolorio', 'RobertOrtega']
# Approvers['Location'] = np.select(appCondition, appChoice, default='NA')

# print(Item)
# database_connection = create_engine(f'mysql://root:{pw}@localhost/{db}')
# df.to_sql(con=database_connection,
#           name='rawdata', if_exists='replace')

