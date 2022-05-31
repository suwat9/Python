import re
from os import walk
import os
import pandas as pd
import math
def ceiling(n):
  return (math.ceil(n/10)*10-1)
def ceilingPack(df):
    if df['Changed Price'] > 0:
        return (math.ceil(100/df['Changed Price']))
    else:
        return (1)
def ProductMess(df):
    if df.Pack < 2:
        return ('ส่งฟรี '+str(df['Product Name'])+' //มีบริการเก็บเงินปลายทาง//')
    else:
        return ('ส่งฟรี (จำนวน '+str(df.Pack)+' ชุด) '+df['Product Name']+' //มีบริการเก็บเงินปลายทาง//')
def checkprice(dp):
  if (dp.Pack < 2):
      pr = dp['Changed Price']      
  else:
      pr = dp.PricePack
      
  if (pr<999): return ceiling(pr*3+50) 
  elif (pr < 3999): return ceiling(pr*2.8)
  elif (pr < 5999): return ceiling(pr*2.5)
  elif (pr < 9999): return ceiling(pr*2)
  else: return ceiling(pr*2)

#delete spacial characters
reCMP = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

path = "C:\code-python\MaliCodes\dataset\watsons"
splitPath = path + '\\Split'
filenames = next(walk(path), (None, None, []))[2]  # [] if no file

if not os.path.isdir(os.path.join(os.getcwd(), splitPath)):
    os.mkdir(splitPath)
for f in filenames:
    df = pd.read_excel(path+'\\'+f, sheet_name = 'Data', usecols = 'A:AA')
    print(df.shape, f)
    df['Changed Price'].fillna(0, inplace = True)
    #rename column name to others
    df = df.rename(columns={'Cat 1':'Cat1','Cat 2':'Cat2','Cat 3': 'Cat3'})
    
    uniques = df['Cat2'].unique()
    with pd.ExcelWriter(splitPath+'\\Split-'+f) as writer:
        for Cat2 in uniques:

            df2 = df[df.Cat2 == Cat2].sort_values(['Cat2','Changed Price'], ascending = [True, True])
            # find the index no
            indPrice = df2.columns.get_loc('Changed Price')
            df2.insert(indPrice - 2,'ProductName2',' ')
            df2.insert(indPrice+2,'Pack',1)
            df2.Pack = df2.apply(ceilingPack, axis=1)
            df2.insert(indPrice+3,'PricePack',df2.Pack*df2['Changed Price'])
            
            df2.insert(indPrice+4,"SpecialPrice",(df2['Changed Price']))
            df2['SpecialPrice']=df2.apply(checkprice, axis = 1)
            df2.insert(indPrice+5,"PriceX",(df2.SpecialPrice*2))
            df2.insert(indPrice+6,"Profit",(df2.SpecialPrice-df2.Price))    
            df2.ProductName2 = df2.apply(ProductMess, axis = 1)
            
            Cat2 = reCMP.sub(' ',Cat2)
            df.sort_values(by=['Changed Price'], ascending = [True],inplace=True)
            df2.to_excel(writer, index=None, sheet_name=Cat2[0:30])