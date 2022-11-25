import os
import sys
import time
import random
import openpyxl as op

path = sys.path[0]
path += '\en.xlsx'  #路徑引導
#print(path)
eg_data = op.load_workbook(path)
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

os.system('cls')

def intro():
    sys.stdout.write('loading')
    sys.stdout.flush()          #清除堵塞
    for i in range(4):
        time.sleep(1)
        sys.stdout.write('.')
        sys.stdout.flush()
    time.sleep(1)
    os.system('cls')

for i in range(1):
    intro()

voca,chinese = sheet_1()
#print(voca,chinese)
dict_voca = {}
for i in range(len(voca)):
    dict_voca[voca[i]] = chinese[i]

dict_chi = {}
for k, v in dict_voca.items():
    dict_chi[v] = k

os.system('cls')

def test_ganerator():
    def typinput():
        a = (input('1 for voca trans chi,2 for chi trans voca\n'))
        return a
    def testadd():
        test = []
        t_type = typinput()
        if t_type == '1':
            t_number = int(input('input tests number\n'))
            tem = [i for i in range(len(voca))]     #做不重複random
            random.shuffle(tem)
            for i in range(t_number):
                test.append(voca[tem[i]])
            return t_type,test
        elif t_type == '2':
            t_number = int(input('input tests number\n'))
            tem = [i for i in range(len(voca))]
            random.shuffle(tem)
            for i in range(t_number):
                test.append(chinese[tem[i]])
            return t_type,test
        else:
            return 0,0
    while True:
        ttype,test = testadd()
        if ttype == '1' or ttype == '2':
            break
        else:
            print('worng enter value,enter again')
            time.sleep(1)
            os.system('cls')
    return ttype,test

ttype,test = test_ganerator()
os.system('cls')
print('test start')
time.sleep(2)
os.system('cls')

order = [i for i in range(len(test))]
random.shuffle(order)
if ttype == '1':
    for i in range(len(test)):
        example = []
        for j in range(3):
            def temadd():
                tem = chinese[random.randint(0,len(chinese)-1)]
                if tem != dict_voca.get(test[order[i]]):
                    example.append(tem)
                else:
                    temadd()
            temadd()
        example.append(dict_voca.get(test[order[i]]))
        random.shuffle(example)
        while True:
            print(test[order[i]])
            for j in range(4):
                print(j+1,example[j])
            ans = input('ans:\n')
            try:ans = int(ans)
            except:pass
            if type(ans) == int and ans <= 4 and ans >= 1:
                break
            else:
                print('illegal input type')
                time.sleep(1)
                os.system('cls')
        if example[ans-1] == dict_voca.get(test[order[i]]):
            print('PASS')
        else:
            print('Worng answer')
        time.sleep(1)
        os.system('cls')

elif ttype == '2':
    for i in range(len(test)):
        example = []
        for j in range(3):
            def temadd():
                tem = voca[random.randint(0,len(chinese)-1)]
                if tem != dict_chi.get(test[order[i]]):
                    example.append(tem)
                else:
                    temadd()
            temadd()
        example.append(dict_chi.get(test[order[i]]))
        random.shuffle(example)
        while True:
            print(test[order[i]])
            for j in range(4):
                print(j+1,example[j])
            ans = input('ans:\n')
            try:ans = int(ans)
            except:pass
            if type(ans) == int and ans <= 4 and ans >= 1:
                break
            else:
                print('illegal input type')
                time.sleep(1)
                os.system('cls')
        if example[ans-1] == dict_chi.get(test[order[i]]):
            print('PASS')
        else:
            print('Worng answer')
        time.sleep(1)
        os.system('cls')
'''
進度:
英選中v1.0完成(已可選)

待辦:
錯誤單字file output
'''