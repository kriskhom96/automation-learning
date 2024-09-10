from distutils.dep_util import newer

one = 10
two = 20
print(one)
print(two)

# syntax_sugar
one, two = two, one
print(one)
print(two)

# concatination
var1 = "5"
var2 = "12"

print(int(var1) * int(var2)) # перевод str в int
print((var1) * int(var2)) # можно множить str на int , тогда будет выводиться строка(слово столько раз)
# print ((var1) * (var2)) - ошибка потому что нельзя множить str

v1 = "new"
v2 = "student"
print(v1 + v2) #newstudent
print(v1, v2) #new student


