import os
import time
import random

practice_word = []
practice_chinese = []
Input = True
ur_words = []
worng_words = []
worng_number = 0

print('Enter the word and its Chinese according to the format \'dog 狗\'')
print('Key \'Stop Stop\' to stop keying')

while True:
    key,chi = input().split()
    if key == 'Stop':
        break
    practice_word.append(key)
    practice_chinese.append(chi)
    

#print('測試庫',practice_word)


os.system('cls')

for i in range(5):
    print('Testing starts in {0} seconds'.format(5-i))
    time.sleep(1)

os.system('cls')
randomvalue = []

for i in range(len(practice_word)):
    randomvalue.append(i)
random.shuffle(randomvalue)

for i in range(len(practice_word)):
    prac_type = random.randint(0,1)
    if prac_type == 0:
        print(practice_chinese[randomvalue[i]])
        Input = input()
        if Input != practice_word[randomvalue[i]]:
            ur_words.append(Input)
            ur_words.append(practice_chinese[randomvalue[i]])
            worng_words.append(practice_word[randomvalue[i]])
            worng_words.append(practice_chinese[randomvalue[i]])
            worng_number += 1
    if prac_type == 1:
        print(practice_word[randomvalue[i]])
        Input = input()
        if Input != practice_chinese[randomvalue[i]]:
            ur_words.append(practice_word[randomvalue[i]])
            ur_words.append(Input)
            worng_words.append(practice_word[randomvalue[i]])
            worng_words.append(practice_chinese[randomvalue[i]])
            worng_number += 1

print('U got {0} worngs'.format(worng_number))
if worng_number != 0:
    print('Urans  : ',ur_words)
    print('Answer : ',worng_words)
