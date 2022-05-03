#TOP supermarket

import re
import pandas as pd
import math
from os import walk
import os

def ceiling(n):
  return (math.ceil(n/10)*10-1)
def ceilingPack(df):
    if df.Price > 0:
        return (math.ceil(100/df.Price))
    else:
        return (1)
def ProductMess(df):
    if df.Pack < 2:
        return ('ส่งฟรี '+str(df['Name'])+' //มีบริการเก็บเงินปลายทาง//')
    else:
        return ('ส่งฟรี (จำนวน '+str(df.Pack)+' ชุด) '+df['Name']+' //มีบริการเก็บเงินปลายทาง//')
def checkPrice(dp):
  if (dp.Pack < 2):
      pr = dp.Price      
  else:
      pr = dp.PricePack
      
  if (pr<999): return ceiling(pr*3+50) 
  elif (pr < 3999): return ceiling(pr*2.8)
  elif (pr < 5999): return ceiling(pr*2.5)
  elif (pr < 9999): return ceiling(pr*2)
  else: return ceiling(pr*2)

path = 'dataset\\Tops Supermarket'
splitPath = path + '\\Split'
filenames = next(walk(path), (None, None, []))[2]  # [] if no file

if not os.path.isdir(os.path.join(os.getcwd(), splitPath)):
    os.mkdir(splitPath)
shiftColumn = 0
for i in filenames:
  fileExcel =i
  df = pd.read_excel(path+'\\'+fileExcel, sheet_name = 0, usecols = 'A:P')
  print(df.shape, i)
  df.Price.fillna(0, inplace = True)
  with pd.ExcelWriter(splitPath+'\\Split-'+fileExcel) as writer:
          df.insert(2,'ProductName2',' ')
          df.insert(4,'Pack',1)
          df.Pack = df.apply(ceilingPack, axis=1)
          df.insert(5,'PricePack',df.Pack*df.Price)
          df.insert(6,"SpecialPrice",(df.Price))
          df['SpecialPrice']=df.apply(checkPrice, axis = 1)
          df.insert(6,"PriceX",(df.SpecialPrice*2))
          df.insert(8,"Profit",(df.SpecialPrice-df.Price))          
          df.ProductName2 = df.apply(ProductMess, axis = 1)
          df.sort_values(by=['Price'], ascending = [True],inplace=True)
          df.to_excel(writer, index=None, sheet_name='FillPrice')
