# -*- coding: utf-8 -*-

import random
data = ["goo","choki","pa"]
data_choice = random.choice(data)
print(data_choice)

print('入力してください')
input = raw_input()

# print('あなたの入力した文字は%x', %input, 'です')

print('あなたの入力した文字は「' + input + '」です')

# -*- coding: utf-8 -*-

# import random
# dic = {'a': 'グー','b': 'チョキ','c':'パー'}
# print('じゃんけん')
# print('a=グー　b=チョキ c=パー　aかbかcを入力')
# user = input('>>>   ')
# user = user.lower()

# try:

# user_choice = dic[user]

# choice_list = ['a','b','c']
# pc = dic[random.choice(choice_list)]

# draw = 'DRAW'
# win = 'You Win!!!'
# lose = 'You Lose!!!'

# if user-choise ==pc:
#     judge = draw
# else:
#     if user_choice =='グー'
#     　　　if pc =='チョキ'：
#             judge = win
#     else:
#     judge = lose

# elif user_choice == 'チョキ':
# 　　if pc == 'パー'：
# 　　　　judge = win
#   else:
#        judge = lose
# else:
#     if pc =='グー':
#         judge = win
#     else:
#         judge = lose

# print('あなたの選んだのは　％s'　％ suer_choice)
# print('コンピュータが選んだのは　％s'　％　pc)
# print('結果は％s'　％　judge)

# except:
#     print('aかbかcを入力してください。')　　
