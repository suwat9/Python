# Separate by category
from os import walk
import os.path
import re
import pandas as pd
import math
def ceiling(n):
  return (math.ceil(n/10)*10-1)
def checkPrice(dp):
  if (dp.Price<999): return ceiling(dp.Price*3+50) 
  elif (dp.Price < 3999): return ceiling(dp.Price*2.8)
  elif (dp.Price < 5999): return ceiling(dp.Price*2.5)
  elif (dp.Price < 9999): return ceiling(dp.Price*2)
  else: return ceiling(dp.Price*2)

#delete spacial characters
reCMP = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

pathDir = 'dataset/SubCat1'
splitPath = pathDir + '\\Split'
filenames = next(walk(pathDir), (None, None, []))[2]  # [] if no file

if not os.path.isdir(os.path.join(os.getcwd(), splitPath)):
    os.mkdir(splitPath)
for f in filenames:

    df = pd.read_excel(pathDir+'\\'+f, sheet_name = 'Sheet1', usecols = 'A:P')
   
    uniques = df.product_var.unique()
    uniques = pd.Series(uniques)
    #uniques.fillna("", inplace = True)
    uniques = uniques.dropna()
    print(df.shape, list(uniques), '\nno of category : ',uniques.size)
    with pd.ExcelWriter(splitPath+'\\Split-'+f) as writer:
        for Cat in uniques:
            df2 = df.loc[df['Product Name'].str.find(Cat)>=0]
            df2.sort_values(['Cat','Price'], ascending = [True, True])
            df2.insert(6,"SpecialPrice",(df2.Price))
            df2['SpecialPrice']=df2.apply(checkPrice, axis = 1)
            df2.insert(6,"PriceX",(df2.SpecialPrice*2))
            df2.insert(8,"Profit",(df2.SpecialPrice-df2.Price))
            df2.insert(3,'ProductName2','จัดส่งฟรี '+df2['Product Name']+' //มีบริการเก็บเงินปลายทาง//')
            df2.to_excel(writer, index=None, sheet_name=Cat[0:30])
