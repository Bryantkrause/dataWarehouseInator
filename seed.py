import pandas as pd
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
import numpy as np


db = os.environ.get("database")
pw = os.environ.get("pw")
wfh = os.environ.get("location")
# file location for seed data
# file = r'C:\Users\bryan\Downloads\SeedData.csv'
# file = r"C:\Users\bkrause\Desktop\Data101\SeedData.csv"
print(wfh)
if wfh == "work":
    file = r"C:\Users\bkrause\Desktop\Data101\SeedData.csv"
else:
    file = r'C:\Users\bryan\Downloads\SeedData.csv'

# set useful columns to keep
columns = [
    'Voucher #','Date',
    'Vendor', 'Ref #',
    'Line',  'Item ID',
    'Description', 'Quantity',
    'U/M',  'Price',
    'Tax', 'Amount',
    'Taxes', 'Total base',
    'Account','Group',
    'Tag', 'Memo',
    'Comments', 'Approvers',
    'Approval Status'
]

df = pd.read_csv(file, usecols=columns, parse_dates=["Date"])

# remove special characters and spaces from column names
df.rename(columns={
    'Voucher #': 'Voucher',
    'Ref #': 'PurchaseOrder',
    'Item ID': 'ItemID',
    'U/M': 'Unit',
    'Total base': 'TotalBase',
    'Approval Status': 'ApprovalStatus'},
    inplace=True)

# assign empty data based on specific column
df['Unit'].fillna("Blank", inplace=True)
df['Taxes'].fillna("0.0", inplace=True)
df['Memo'].fillna("0.0", inplace=True)
df['Comments'].fillna("0.0", inplace=True)
df['PurchaseOrder'].fillna("0.0", inplace=True)
df['CoolId'] = df['Voucher'] + df['Vendor'] + df['Line'].astype(str)
# # df = df.set_index('UniqueId')

df['Approvers'].fillna("No", inplace=True)


Item = df['ItemID'].unique()
Account = df['Account'].unique()
Group = df['Group'].unique()
df['Name'] = df.Approvers.str.replace('[^a-zA-Z]', '')
df['Name'] = df['Name'].map(
    lambda x: x.rstrip('pending').rstrip('reject'))

# location is theoretically based on tag however for vehicles a vehicle tag is used so in order to figure out location you have to look at multiple columns of data
# this is an attempt at removing the guess work
# get location data based on approver
appChoice = ['Cerritos', 'Rancho', 'Fullerton',
             'Downey', 'Rancho', 'Rancho', 'Rancho','None']
appCondition = [
    df['Name'].str.contains(r'FrankGuzma', na=False),
    df['Name'].str.contains(r'CarlosGarcia', na=False),
    df['Name'].str.contains(r'LuisSerrano', na=False),
    df['Name'].str.contains(r'HenryValdez', na=False),
    df['Name'].str.contains(r'DerekFranco', na=False),
    df['Name'].str.contains(r'DavidRevolorio', na=False),
    df['Name'].str.contains(r'RobertOrtega', na=False),
    df['Name'].str.contains(r'No', na=False)]
df['Location'] = np.select(appCondition, appChoice, default='None')

Approvers = df['Name'].unique()
ALoc2 = pd.DataFrame(Approvers, columns=['Name'])


# get locaiton data based on tag system
tagChoice= [
    'Cerritos', 'Fullerton', 'Rancho', 'Rancho', 'Downey'
]
tagCondition = [
    df['Tag'].str.contains(r'16107 - Location - 16107 Commerce Way - Cerritos', na=False),
    df['Tag'].str.contains(r'210 - Location - 210 E. Lambert Road', na=False),
    df['Tag'].str.contains(r'9278-2 - Location-9278 Charles Smith Ave.-Rancho Cucamonga', na=False),
    df['Tag'].str.contains(r'11937-2 - Total - 11937 Woodruff - Downey', na=False),
    df['Tag'].str.contains(r'11937 - Westset - 11937 Woodruff Ave. - Downey', na=False)]
df['TagLocation'] = np.select(tagCondition, tagChoice, default='None')

print(df['TagLocation'].unique())
tag = df['TagLocation'].unique()
tagloc = pd.DataFrame(tag, columns=['TagLocation'])
# print(Item)
engine = create_engine(f'mysql://root:{pw}@localhost/{db}')
print(df['CoolId'].nunique())
df.to_sql(con=engine, name='rawdata', if_exists='replace', index=False)
with engine.connect() as con:
    con.execute(
        "ALTER TABLE rawdata ADD PRIMARY KEY (CoolId(150))")

# create dimension tables
tagloc.to_sql(con=engine,
              name='tagloc', if_exists='replace')
ALoc2.to_sql(con=engine,
           name='aloc', if_exists='replace')
# add primary keys since you know its not automatic
engine.execute(
    "ALTER TABLE aloc ADD appid INT PRIMARY KEY AUTO_INCREMENT FIRST")
engine.execute(
    "ALTER TABLE tagloc ADD tagid INT PRIMARY KEY AUTO_INCREMENT FIRST")
# add foriegn keys 
# engine.execute(
#     """
# ALTER TABLE rawdata
# ADD FOREIGN KEY(name)
# REFERENCES aloc(name);  
#     """
# )

