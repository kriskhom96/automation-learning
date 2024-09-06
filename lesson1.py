variable1 = 20
variable2 = 5
variable3 = 3

result = variable1 % variable3
print(result)

# % остаток от деления
# // сколько раз поделили на целое  число

result2 = variable1 // variable3
print(result2)

#stings
sting_test1 = "10"
sting_test2 = "1"
print(sting_test2 + sting_test1)

#turn str to int
transform = int(sting_test1)
transform2 = int(sting_test2)

print(transform2, transform)

transformed_str_to_int = (transform + transform2)
print(transformed_str_to_int)

#input by default returns STR
#to transform, insert int
age = int(input("how old are you?"))
print(age)
print(type(age))
