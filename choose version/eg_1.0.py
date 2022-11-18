import os
import time
import random
import openpyxl as op
'''
wb = op.Workbook()
wb.save('test.xlsx')
'''

eg_data = op.load_workbook(filename='en.xlsx')
#sheet name: 最近遇到 疑難雜症 lv3~4特選
def sheet_1():
    sheet1 = eg_data['疑難雜症']
    voca_column = sheet1['A']
    voca = []
    for i in voca_column:
        voca.append(i.value)
    voca.remove(voca[0])
    chinese = []
    chinese_column = sheet1['B']
    for i in chinese_column:
        chinese.append(i.value)
    chinese.remove(chinese[0])
    return voca,chinese

voca,chinese = sheet_1()
#print(voca,chinese)
test_voca = {}
for i in range(len(voca)):
    test_voca[voca[i]] = chinese[i]
#print(test_voca)

