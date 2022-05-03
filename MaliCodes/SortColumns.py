import pandas as pd    
from os import walk

path = 'dataset/DaisoThailand - MAY2022 - 825SKU'
filenames = next(walk(path), (None, None, []))[2]  # [] if no file

f = filenames[0]
df = pd.read_excel(path+'\\'+f, sheet_name = 'Data', usecols = 'A:T')

cols = list(df.columns)
print(cols)
Cprice, Cimg ,Cdes = cols.index('Price'),cols.index('Image 1'),cols.index('Description')

cols[Cprice], cols[Cimg], cols[Cdes] = cols[Cdes], cols[Cprice], cols[Cimg]
df = df[cols] 

cols = cols.sort()
print('Second Rounds: ',cols)
