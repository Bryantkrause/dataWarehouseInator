# this will convert raw excel data into something
import pandas as pd
import numpy as np
from datetime import datetime

# get raw data from employee data file
employeeFile = r'C:\Users\bkrause\downloads\LaborinatorRawReport.xlsx'
# set new file name
updatedFile = r'C:\Users\bkrause\downloads\LaborinatorWayBetterUpdate.xlsx'
# store data in data frame
df = pd.read_excel(employeeFile, parse_dates=[
                   'Hire', 'Termination', 'Period Begin', 'Period End'])

# update column names
columnNames = [
    'EmployeeNumber',
    'EmployeeName',
    'DepartmentCode',
    'DivisionCode',
    'HireDate',
    'TerminationDate',
    'StartPeriod',
    'EndPeriod',
    'PayDate',
    'GrossWages',
    'RegularHours',
    'RegularPay',
    'OvertimeHours',
    'OvertimePay',
    'DoubleTimeHours',
    'DoubleTimePay',
    'HolidayHours',
    'HolidayPay',
    'SalaryPay',
    'SalaryHours',
    'SickHours',
    'SickPay'
]
df.columns = columnNames
# remove bogus rows
df = df[1:-1]
df['EndPeriod'] = pd.to_datetime(df['EndPeriod']).dt.normalize()
# clean hour data
# Set columns to create total from
hourTotal = ['RegularHours', 'OvertimeHours',
             'DoubleTimeHours', 'HolidayHours', 'SickHours']
# sum  hours based on departments and division
depHours = df.groupby(['DivisionCode', 'DepartmentCode', 'EndPeriod'])[
    'RegularHours', 'OvertimeHours', 'DoubleTimeHours', 'HolidayHours', 'SickHours'].sum().reset_index()
# update object data type to date type
# depHours['EndPeriod'] = pd.to_datetime(
#     depHours['EndPeriod'])
# add total column
depHours['TotalHours'] = depHours[hourTotal].sum(axis=1)
# add Ot percantage column
depHours['OTPercentage'] = (
    depHours['OvertimeHours']/depHours['TotalHours']) * 100
# convert errors to 0
depHours = depHours.fillna(0)
# set rounding to 2 digits
depHours = depHours.round(2)
# update columns with wrong data type objects to integers
depHours['DepartmentCode'] = depHours['DepartmentCode'].astype(np.int64)
depHours['DivisionCode'] = depHours['DivisionCode'].astype(np.int64)
# remove managerial data
depHours = depHours.drop(
    depHours[depHours.DepartmentCode.isin([104, 107, 204, 207, 114, 212])].index)
# update incorrect information of 20 to 9278 location
depHours.DivisionCode.replace(20, 9278, inplace=True)
# convert Downey CSR to Rancho CSR
depHours.loc[depHours.DepartmentCode == 109, 'DivisionCode'] = 9278

# clean pay data
# Set columns to create total from
payTotal = ['RegularPay', 'OvertimePay',
            'DoubleTimePay', 'HolidayPay', 'SickPay']
# sum Pay based on departments and division
depPay = df.groupby(['DivisionCode', 'DepartmentCode', 'EndPeriod'])[
    'RegularPay', 'OvertimePay', 'DoubleTimePay', 'HolidayPay', 'SickPay'].sum().reset_index()
# update object data type to date
# depPay['EndPeriod'] = pd.to_datetime(depPay['EndPeriod'])
# depPay['EndPeriod'] = pd.to_datetime(depPay['EndPeriod'])
# add total column
depPay['TotalPay'] = depPay[payTotal].sum(axis=1)
# add Ot percantage column
depPay['OTPercentage'] = (
    depPay['OvertimePay']/depPay['TotalPay']) * 100
# convert errors to 0
depPay = depPay.fillna(0)
# set rounding to 2 digits
depPay = depPay.round(2)
# update columns with wrong data type objects to integers
depPay['DepartmentCode'] = depPay['DepartmentCode'].astype(np.int64)
depPay['DivisionCode'] = depPay['DivisionCode'].astype(np.int64)
# remove managerial data
depPay = depPay.drop(
    depPay[depPay.DepartmentCode.isin([104, 107, 204, 207, 114, 212])].index)
# update incorrect information of 20 to 9278 location
depPay.DivisionCode.replace(20, 9278, inplace=True)
# convert Downey CSR to Rancho CSR
depPay.loc[depPay.DepartmentCode == 109, 'DivisionCode'] = 9278

# set up location based dataframes

# fullerton data
fullertonDataPay = depPay.loc[depPay['DivisionCode'] == 210]
getUniqueDeps = fullertonDataPay.DepartmentCode.value_counts()
getRowCount = getUniqueDeps.count()

fPivotPayReg = fullertonDataPay.pivot_table(
    columns='DepartmentCode', index='EndPeriod', aggfunc='sum', values='RegularPay')
fPivotPayOT = fullertonDataPay.pivot_table(columns=pd.Grouper(
    freq='W', key='EndPeriod'), index='DepartmentCode', aggfunc='sum', values='OvertimePay')


# set up excel file to save and save data to specific tabs
writer = pd.ExcelWriter(updatedFile, engine='xlsxwriter')
depHours.to_excel(writer, sheet_name='Hours')
depPay.to_excel(writer, sheet_name='Pay')
fPivotPayReg.to_excel(writer, sheet_name='Fullerton')
writer.close()

# use this line to turn into percentages:
# df['%'] = ((df['Code Lines'] / df['Code Lines'].sum())*100).round(2).astype(str) + '%'
