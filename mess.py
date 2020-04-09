"""Just learning pythonm."""
import os
import pandas as pd

pd.set_option('display.max_columns', None)
os.chdir(r'C:\Users\paul\Dropbox\Paul\Top Hat\Timesheets\20200407')
data = os.listdir()
mon = 0
extract = []
for count, d in enumerate(data):
    print(count, d)
    if d.endswith('.xlsx'):
        xl = pd.ExcelFile(d)
        df = xl.parse('Timesheet WC 230320')
        extract = pd.append(extract, df)


# df = pd.read_excel(entries[0])
# print(df)
