import pandas as pd 
#if all excel file to be opened - keep_default_na=False so as not to get empty rows
df = pd.read_excel(r'C:\Users\pir.gprountzos\OneDrive - CMA CGM\Desktop\week2\VslSchedule 090124.xls', keep_default_na=False)

print(df)
