#Thai Watsadu

import re
import pandas as pd
import math
from os import walk
import os

def ceiling(n):
  return (math.ceil(n/10)*10-1)
def ceilingPack(df):
    if df.price > 0:
        return (math.ceil(100/df.price))
    else:
        return (1)
def ProductMess(df):
    if df.Pack < 2:
        return ('จัดส่งฟรี '+str(df.name)+' //มีบริการเก็บเงินปลายทาง//')
    else:
        return ('จัดส่งฟรี (จำนวน '+str(df.Pack)+' ชุด) '+df['name']+' //มีบริการเก็บเงินปลายทาง//')
def checkprice(dp):
  if (dp.Pack < 2):
      pr = dp.price      
  else:
      pr = dp.pricePack
      
  if (pr<999): return ceiling(pr*3+50) 
  elif (pr < 3999): return ceiling(pr*2.8)
  elif (pr < 5999): return ceiling(pr*2.5)
  elif (pr < 9999): return ceiling(pr*2)
  else: return ceiling(pr*2)

path = 'MakroClick'
splitPath = path + '\\Split'
filenames = next(walk(path), (None, None, []))[2]  # [] if no file

if not os.path.isdir(os.path.join(os.getcwd(), splitPath)):
    os.mkdir(splitPath)
shiftColumn = 0
for i in filenames:
  fileExcel =i
  df = pd.read_excel(path+'\\'+fileExcel, sheet_name = 0, usecols = 'A:P')
  print(df.shape, i)
  df.price.fillna(0, inplace = True)
  with pd.ExcelWriter(splitPath+'\\Split-'+fileExcel) as writer:
          df.insert(2,'Productname2',' ')
          df.insert(4,'Pack',1)
          df.Pack = df.apply(ceilingPack, axis=1)
          df.insert(5,'pricePack',df.Pack*df.price)
          df.insert(6,"Specialprice",(df.price))
          df['Specialprice']=df.apply(checkprice, axis = 1)
          df.insert(6,"priceX",(df.Specialprice*2))
          df.insert(8,"Profit",(df.Specialprice-df.price))          
          df.Productname2 = df.apply(ProductMess, axis = 1)
          df.sort_values(by=['price'], ascending = [True],inplace=True)
          df.to_excel(writer, index=None, sheet_name='Fillprice')
