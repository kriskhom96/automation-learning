# from distutils.dep_util import newer
# # как поменять местами значение переменных
# # oprion 1: syntax_sugar
# one = 10
# two = 20
# print(one)
# print(two)
#
# one, two = two, one
# print(one)
# print(two)
#
# # option 2:
# three = 10
# four = 20
# print(three)
# print(four)
#
# ...
#
from dataclasses import replace
from traceback import print_tb
from unittest import addModuleCleanup

from encodings.punycode import adapt

# # concatination
# var1 = "5"
# var2 = "12"
#
# print(int(var1) * int(var2)) # перевод str в int
# print((var1) * int(var2)) # можно множить str на int , тогда будет выводиться строка(слово столько раз)
# # print ((var1) * (var2)) - ошибка потому что нельзя множить str
#
# v1 = "new"
# v2 = "student"
# print(v1 + v2) #newstudent
# print(v1, v2) #new student

#множественное присвоение
# a, b, c = 3, 4, 5
# print(a,b,c)

#степень
#print(2**3)
#квадратный корень
#print(25**0.5)

#is, not - операторы. сравнение по айдишника
#сравнение айдишек, оборот not


#print(5 is 5)
#
# var1 = 200
# var2 = 199 + 1
#
# print(id(var1))
# print(id(var1))
#
# var1 = 5
# var1_float = 5.0
# var2 = 2
# var3 = 5
#
# if var1 > var2:
#     print("hi this is brach if")
# else:
#     print("if was false!")
#
#
# print("text after if block")
#
# age = int(input("how old are you?"))
# if age <18:
#     print("sorry")
# else:
#     if age >= 21:
#         print('wanna some alcohol?')
#     else:
#         print('welcome')
#
# ELIF
#
# age = int(input("how old are you?"))
# if age <18:
#     print("sorry")
# elif age >= 21:
#         print('wanna some alcohol?')
# else:
#         print('welcome')
#
#
#
#
# password = input("pls your psswrd")
# if password == "admin":
#     print("welcome")
# else:
#     print("sorry")
#
#
# string_case = "aDmin"
# print(type(string_case))
# #
# print(string_case.upper())
# print(string_case.lower())
# print(string_case.title())
# print(string_case)
# string_case = string_case.title()
# print(string_case)
#
#
# password = input("pls your name")
# if password.title() == "Admin":
#     print("welcome")
# else:
#     print("sorry")
#
url = 'https://site_prod.com'
print(url)
print(url.replace("prod", "qa"))
url = (url.replace("prod", "qa"))
print(url)
url = (url.replace('_   qa', ''))
print(url)