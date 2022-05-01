import re
from os import walk
import os
import pandas as pd
import math
def ceiling(n):
  return (math.ceil(n/10)*10-1)
def ceilingPack(df):
    if df.Price > 0:
        return (math.ceil(100/df.Price))
    else:
        return (1)
def ProductMess(df):
    if df.Pack < 2:
        return ('จัดส่งฟรี '+str(df['Product Name'])+' //มีบริการเก็บเงินปลายทาง//')
    else:
        return ('จัดส่งฟรี (จำนวน '+str(df.Pack)+' ชุด) '+df['Product Name']+' //มีบริการเก็บเงินปลายทาง//')
def checkprice(dp):
  if (dp.Pack < 2):
      pr = dp.Price      
  else:
      pr = dp.PricePack
      
  if (pr<999): return ceiling(pr*3+50) 
  elif (pr < 3999): return ceiling(pr*2.8)
  elif (pr < 5999): return ceiling(pr*2.5)
  elif (pr < 9999): return ceiling(pr*2)
  else: return ceiling(pr*2)

#delete spacial characters
reCMP = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

path = 'Store1'
splitPath = path + '\\Split'
filenames = next(walk(path), (None, None, []))[2]  # [] if no file

if not os.path.isdir(os.path.join(os.getcwd(), splitPath)):
    os.mkdir(splitPath)
for f in filenames:
    df = pd.read_excel(path+'\\'+f, sheet_name = 'Data', usecols = 'A:P')
    print(df.shape, f)
    df.Price.fillna(0, inplace = True)

    uniques = df.Cat.unique()
    with pd.ExcelWriter(splitPath+'\\Split-'+f) as writer:
        for Cat in uniques:
            df2 = df[df.Cat == Cat].sort_values(['Cat','Price'], ascending = [True, True])
            df2.insert(3,'ProductName2',' ')
            df2.insert(7,'Pack',1)
            df2.Pack = df2.apply(ceilingPack, axis=1)
            df2.insert(8,'PricePack',df2.Pack*df2.Price)
            
            df2.insert(9,"SpecialPrice",(df2.Price))
            df2['SpecialPrice']=df2.apply(checkprice, axis = 1)
            df2.insert(9,"PriceX",(df2.SpecialPrice*2))
            df2.insert(11,"Profit",(df2.SpecialPrice-df2.Price))    
            df2.ProductName2 = df2.apply(ProductMess, axis = 1)
            
            Cat = reCMP.sub(' ',Cat)
            df.sort_values(by=['Price'], ascending = [True],inplace=True)
            df2.to_excel(writer, index=None, sheet_name=Cat[0:30])