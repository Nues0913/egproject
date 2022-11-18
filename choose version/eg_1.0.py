import os
import time
import random
import openpyxl as op
'''
wb = op.Workbook()
wb.save('test.xlsx')
'''
eg_data = op.load_workbook('en.xlsx')
#sheet name: 最近遇到 疑難雜症 lv3~4特選
print(eg_data['最近遇到'])