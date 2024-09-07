# # #homework for the lesson 1
# # #1 Написати програму, яка зчитує два числа та виводить їхню суму, різницю, добуток та частку.
# #
# # digit_1 = 5
# # digit_2 = 2
# #
# # print(digit_1, digit_2)
# # print(digit_1 + digit_2)
# # print(digit_1 - digit_2)
# # print(digit_1 * digit_2)
# # print(digit_1 - digit_2)
# #
# # #2 Користувач вводить два числа. Вивести залишок від ділення першого числа на друге.
# #
# # print(digit_2 % digit_1)
# #
# # #3 Користувач вводить два числа. Вивести, скільки разів перше число ділиться на друге без залишку.
# #
# # print(digit_1 // digit_2)
# #
# # #4 Користувач вводить рядок, який складається з цифр. Програма повинна перетворити його на число та вивести.
# #
# # # ex1 = int(input("insert digits"))
# # # print(ex1)
# # # print(type(ex1))
# #

# 5 Стрічкова конкатенація + математика:
# Користувач вводить два числа. Програма повинна вивести два прінти: перший — їхню суму,
# другий об'єднати їх. Якщо в нас числа 5 та 4, то результат повинен бути 9 та 54.
# Користувач вводить два числа
digit_1 = int(input("Введіть перше число: "))
digit_2 = int(input("Введіть друге число: "))

# Перетворюємо числа на рядки
digit1_str = str(digit_1)
digit2_str = str(digit_2)

# Перевіряємо типи змінних
print(type(digit1_str))
print(type(digit2_str))

# Виводимо рядки
print(digit1_str)
print(digit2_str)

# Обчислюємо суму чисел
result_sum = digit_1 + digit_2
print(result_sum)

# Конкатенація рядків
result_conc = digit1_str + digit2_str
print(result_conc)
# #
# # # 6 Вік користувача:
# # year_born = int(input("what year were you born?"))
# # name = input("what's your name?")
# # year_now = int(input("what year is it now?"))
# #
# # age = year_now - year_born
# #
# # print(name)
# # print(age)
# #
# # #7 Перевод з цельсія в фаренгейт:
# #
# # c_now = float(input("temperature in C now?"))
# # print("temp in C:", c_now)
# # f_now = ((c_now*9/5) + 32)
# # print("farenheit now:"f_now)
# #
# # # # 8 Перевод з фаренгейта в цельсій:
# #
# # farenheit_now = float(input("temperature in Farenheit now?"))
# # print("temp in farenheit:", farenheit_now)
# # celcius_now = ((farenheit_now - 32) * 5/9)
# # print(celcius_now)
# #
# # # 9 Теорема Піфагора:
# # # Запитайте у користувача довжини катетів та виведіть на екран довжину гіпотенузи.
# # # Трикутник рівнобедрений. Що б взвести в степінь ставимо два рази множення
# # # два в степені три буде так 2**3, квадратний корінь з двух буде 2**(1/2)
# #
# #
# # a = float(input("side a:"))
# # b = float(input("side b:"))
# # c = (a**2 + b**2) **(1/2)
# #
# # print(c)
# #
# # # 10 Школярі та яблука
# # # n школярів ділять k яблук порівну, недільний залишок залишається в кошику.
# # # Скільки яблук дістанеться кожному школярові та скільки залишиться в кошику?
# # # Програма отримує на вхід числа n і k - цілі, додатні, не перевищують 10000.
# pupil = n = 30
# apple = k = 100
#
# apple_per_pupil = (apple // pupil)
# print("apples for each pupil:", apple_per_pupil)
#
# apples_not_divided = (apple % pupil)
# print('apples not divided:', apples_not_divided)
#
# # 11 Магазин канцелярських товарів
# # Одного разу, відвідавши магазин канцелярських товарів, Вася купив X олівців, Y ручок та Z фломастерів. Відомо,
# # що ціна ручки на 2 гривні більше ціни олівця та на 7 гривень менше ціни фломастера. Також відомо,
# # що вартість олівця становить 3 гривні. Потрібно визначити загальну вартість покупки.
# # Вхідні дані
# # просимо користувача ввести три змінні
# # кожне з яких не перевищує 109.
# # Вихідні дані
# # виведіть одне ціле число – вартість покупки в гривнях.
# # приклад для перевірки програми 1
# # ввів: 1 1 1
# # отримав: 20
#
# pencil_price = 3
# pen_price = (pencil_price +2)
# oil_price = (pen_price + 7)
#
# print(pen_price)
# print(oil_price)
#
# pencils_bought = int(input("pencils bought:"))
# pens_bought = int(input("pens bought:"))
# oils_bought = int(input("ols bought:"))
#
# total_price = ((pens_bought*pen_price) + (pencils_bought*pencil_price) + (oils_bought*oil_price))
#
# print(total_price)
#
# # 12 Циферблад
# # Запитайте в користувача скільки хвилин пройшло з початку доби.
# # Визначте, скільки годин і хвилин покаже електронний годинник в цей момент і поверніть йому результат (формататування тексту при ввиводі не важливе).
# # приклад для перевірки програми 1
# # користувач ввів:150
# # користувач отримує: 2, 30
# # приклад для перевірки програми 2
# # користувач ввів:1441
# # користувач отримує: 0, 1
#
# time_passed = int(input('time passed: '))
# time_in_hours = (time_passed // 60) % 24
# time_in_hours2 = (time_passed % 60)
# print(time_in_hours,":",time_in_hours2)
#
# # 13 Журавлики
# # Петро, Катя та Сергій роблять з паперу журавликів. Разом вони зробили S журавликів.
# # Скільки журавликів зробила кожна дитина, якщо відомо, що Петро та Сергій зробили однакову кількість журавликів,
# # а Катя зробила в два рази більше журавликів, ніж Петро та Сергій разом.
# # Вхідні дані
# # Юзер вводить загальну кількість журавликів. Отримує три значення скільки зробив кожен (Петро, Катя та Сергій).
#
# total = int(input('total made:'))
#
# x = total // 6
# peter = x
# serge = x
# kat = 4 * x
#
#
# print(peter)
# print(kat)
# print(serge)
#
# # 14 Податки
# # Прийшов час податків і вам треба написати програму що б допомогти відділу бугалтерії
# # програма приймає від користувача його зарплату за 3 місяці та відсоток який він має сплатити.
# # Виведіть на екран скільки треба сплатити податків за 3 місяці. Не забудьте ЄСВ(4422)
#
salary1 = float(input('salary1'))
salary2 = float(input('salary2'))
salary3 = float(input('salary3'))
fee = float(input('your fee'))
totalSalary = salary1 + salary2 + salary3
totalFee = (totalSalary * fee) / 100
feeAndEsv = totalFee + (4422*3)
print(feeAndEsv)
