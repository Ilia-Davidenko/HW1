# 1- Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input('Введине номер дня недели (1-7) '))
if 1 <= day <= 5:
    print('Солнце еще высоко!')
elif day == 6 or day == 7:
    print('Выходной')
else:
    print('На нашей планете нет такого дня недели, вы откуда к нам пожаловали?')