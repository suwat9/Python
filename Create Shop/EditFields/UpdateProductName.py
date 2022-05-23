#Tops To Template
import numpy as np
import openpyxl as xl
from os import walk
from random import seed,randint

path = 'D:/Codes/Mali-Python/Create Shop/editFields/Morning/สบู่'
fileTemplate = next(walk(path), (None, None, []))[2]  # [] if no file

#if not os.path.isdir(os.path.join(os.getcwd(), splitPath)):
#    os.mkdir(splitPath)
print(fileTemplate)

for filename in fileTemplate:
    file = path + '/' + filename
    wbTemp = xl.load_workbook(file)
    wsTemp = wbTemp.worksheets[1]

    headTemp_row = 2
    read_start_row = 3
    
    colTemp = [cell.value for cell in wsTemp[headTemp_row]]
    maxTemp_row = wsTemp.max_row - headTemp_row 
    # seed number for discount random from 0 to 10 bahts
    seednumber = 3
    seed(seednumber)
    first = True
    
    for i in range(0, maxTemp_row):
        
        #wsTemp.cell(row=write_start_row+i, column=colTemp.index('SpecialPrice Start')+1,value='2022-01-01')
        #wsTemp.cell(row=write_start_row+i, column=colTemp.index('SpecialPrice End')+1,value='2026-12-31')
        order = str(i + 1)
        # shopName = 'Malishop16-Top-Rice'+order.zfill(4)
        # wsTemp.cell(row=write_start_row+i, column=colTemp.index('SellerSKU')+1,value=shopName)
        #wsTemp.cell(row=write_start_row+i, column=colTemp.index('*ยี่ห้อ')+1,value='Premium(พรีเมึ่ยม)')
        # imgLink = wsTemp.cell(row=read_start_row+i, column=colTemp.index('*รูปของสินค้า1')+1)
        # detail = wsTemp.cell(row=read_start_row+i, column=colTemp.index('Long Description (Lorikeet)')+1)
        #if detail.value==None:
        #    detail = wsOrg.cell(row=read_start_row+i, column=colOrg.index('ProductName2')+1)
        #content = "<span style=\"font-family:none\">"+ str(detail.value) + "<\span><div style=\"width:100%;margin:0\"><div style=\"width:100%;display:block;margin:0\"><div style=\"width:100%;display:block\"><img class=\"\" src=\""+ str(imgLink.value) +"\" style=\"width:100%;display:block\"\></div></div></div>"
        #wsTemp.cell(row=read_start_row+i, column=colTemp.index('Long Description (Lorikeet)')+1,value=content)
        keyName = ['*ชื่อสินค้า','Long Description (Lorikeet)','สินค้าภายในกล่อง']
        productName = wsTemp.cell(row=read_start_row+i, column=colTemp.index(keyName[0])+1)
        longDesc = wsTemp.cell(row=read_start_row+i, column=colTemp.index(keyName[1])+1)
        productBox = wsTemp.cell(row=read_start_row+i, column=colTemp.index(keyName[2])+1)
        keyText = 'Free Delivery'
        newText = 'จัดส่งฟรี '
        if first and (str(productName.value).find(keyText)>=0):
            keyValue = [str(productName.value).replace(keyText, newText),
                        str(longDesc.value).replace(keyText, newText),
                        str(productBox.value).replace(keyText, newText)]
            wsTemp.cell(row=read_start_row+i, column=colTemp.index(keyName[0])+1,value=keyValue[0])
            wsTemp.cell(row=read_start_row+i, column=colTemp.index(keyName[1])+1,value=keyValue[1])
            wsTemp.cell(row=read_start_row+i, column=colTemp.index(keyName[2])+1,value=keyValue[2])
        else:
            if first: print('ไม่พบคำว่า '+keyText)
            first = False
        #random discount 0-10 bahts
        discount = randint(0, 10)
        spPrice = wsTemp.cell(row=read_start_row+i, column=colTemp.index('SpecialPrice')+1)
        newPrice = int(spPrice.value)-discount
        wsTemp.cell(row=read_start_row+i, column=colTemp.index('SpecialPrice')+1,value=newPrice)
        oldShopName = wsTemp.cell(row=read_start_row+i, column=colTemp.index('SellerSKU')+1)
        shopName = 'Malishop14'
        wsTemp.cell(row=read_start_row+i, column=colTemp.index('SellerSKU')+1,value=shopName+str(oldShopName.value)[10:])
        # wsTemp.cell(row=write_start_row+i, column=colTemp.index('*น้ำหนัก')+1,value=1)
        # wsTemp.cell(row=write_start_row+i, column=colTemp.index('*ความยาว')+1,value=17)
        # wsTemp.cell(row=write_start_row+i, column=colTemp.index('*ความกว้าง')+1,value=11)
        # wsTemp.cell(row=write_start_row+i, column=colTemp.index('*ความสูง')+1,value=1)
        # wsTemp.cell(row=write_start_row+i, column=colTemp.index('*จำนวน')+1,value=10)
        # wsTemp.cell(row=write_start_row+i, column=colTemp.index('รุ่น')+1,value='ไม่ระบุ')
        # wsTemp.cell(row=write_start_row+i, column=colTemp.index('การประกัน')+1,value='1 สัปดาห์')
        # wsTemp.cell(row=write_start_row+i, column=colTemp.index('*การรับประกัน')+1,value='มีการรับประกัน')
        # wsTemp.cell(row=write_start_row+i, column=colTemp.index('สินค้าอันตราย')+1,value='ไม่มี')
    wbTemp.save(file)
    wbTemp.close()