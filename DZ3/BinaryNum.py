#Напишите программу, которая будет преобразовывать десятичное число в двоичное (без встроенных функций).
#Пример:
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

number = int(input("enter the number: "))
b = " "
while(number > 0):
    b = str(number % 2) + b 
    number = number // 2
print(b)    