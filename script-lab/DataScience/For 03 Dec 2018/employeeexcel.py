import pandas as pd
with pd.ExcelFile('printout.xls') as xls:
    df1 = pd.read_excel(xls, 'Sheet1')
    df2 = pd.read_excel(xls, 'Sheet2')

print("****Result Sheet 1****")
print (df1[0:5]['Salary'])
print("")
print("***Result Sheet 2****")
print (df2[0:5]['zipcode'])
