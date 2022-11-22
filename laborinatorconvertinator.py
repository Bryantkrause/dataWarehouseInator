# this will convert raw excel data into something
import pandas as pd
import numpy as np

# get raw data from employee data
employeeFile = r'C:\Users\bkrause\downloads\LaborinatorRawReport.xlsx'

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
# print(df.head())
# print(df.tail())

depHours = df.groupby(['DivisionCode','DepartmentCode'])[
    'RegularHours', 'OvertimeHours', 'DoubleTimeHours', 'HolidayHours', 'SickHours'].sum()
depHours['TotalHours'] = depHours.sum(axis=1)
depHours['OTPercentage'] = (
    depHours['OvertimeHours']/depHours['TotalHours']) * 100
print(depHours)
