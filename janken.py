# -*- coding: utf-8 -*-

import random
data = ["goo","choki","pa"]
data_choice = random.choice(data)
print(data_choice)

print('入力してください')
input = raw_input()

# print('あなたの入力した文字は%x', %input, 'です')

print('あなたの入力した文字は「' + input + '」です')
