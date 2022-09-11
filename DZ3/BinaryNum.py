#Напишите программу, которая будет преобразовывать десятичное число в двоичное (без встроенных функций).
#Пример:
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

inputNumber = int(input("enter the number: "))

def BinaryNum(number):

    b = " "
    while(number > 0):
        b = str(number % 2) + b 
        number = number // 2
    print(b)    

BinaryNum(inputNumber)