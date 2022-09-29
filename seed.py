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
    'Ref #': 'PurchaseOrder',
    'Item ID': 'ItemID',
    'U/M': 'Unit',
    'Total base': 'TotalBase',
    'Approval Status': 'ApprovalStatus'},
    inplace=True)


df['Unit'].fillna("Blank", inplace=True)
df['Taxes'].fillna("0.0", inplace=True)
df['Memo'].fillna("0.0", inplace=True)
df['Comments'].fillna("0.0", inplace=True)
df['PurchaseOrder'].fillna("0.0", inplace=True)
df['PrimaryKey'] = df['Voucher'] + df['Vendor'] + df['Line'].astype(str)
df['Approvers'].fillna("No", inplace=True)
print(df['Approvers'].unique())

Item = df['ItemID'].unique()
Account = df['Account'].unique()
Group = df['Group'].unique()
Tag = df['Tag'].unique()
df['Approvers'] = df.Approvers.str.replace('[^a-zA-Z]', '')
df['Approvers'] = df['Approvers'].map(
    lambda x: x.rstrip('pending').rstrip('reject'))

Approvers = df['Approvers'].unique()
print(Approvers)
ALoc2 = pd.DataFrame(Approvers, columns=['Name'])
# for col in ALoc.columns:
#     print(col)
# ALoc.rename(columns={0: 'Name'},inplace=True)
# for col in ALoc.columns:
#     print(col)
# ALoc['length'] = ALoc['Name'].str.len()
# print(ALoc)
# print(ALoc.sort_values(by=['Name']))
# mask = ALoc['length'] > 6
# ALoc2 = ALoc.loc[mask]
# ALoc2['Name'].fillna("0", inplace=True)
print(ALoc2)
appChoice = ['Cerritos', 'Rancho', 'Fullerton',
             'Downey', 'Rancho', 'Rancho', 'Rancho','None']
appCondition = [
    ALoc2['Name'].str.contains(r'FrankGuzma', na=False),
    ALoc2['Name'].str.contains(r'CarlosGarcia', na=False),
    ALoc2['Name'].str.contains(r'LuisSerrano', na=False),
    ALoc2['Name'].str.contains(r'HenryValdez', na=False),
    ALoc2['Name'].str.contains(r'DerekFranco', na=False),
    ALoc2['Name'].str.contains(r'DavidRevolorio', na=False),
    ALoc2['Name'].str.contains(r'RobertOrtega', na=False),
    ALoc2['Name'].str.contains(r'No', na=False)]

print(appCondition)
print(appChoice)
ALoc2['Location'] = np.select(appCondition, appChoice, default='NA')
print(ALoc2)
# print(Item)
# database_connection = create_engine(f'mysql://root:{pw}@localhost/{db}')
# df.to_sql(con=database_connection,
#           name='rawdata', if_exists='replace')
