#Задана натуральная степень k. Сформировать случайным образом список коэффициентов
#(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#Пример:

#k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import *


number = int(input("Enter the number: "))


def String(k):
    str = ""
    while(k >= 0):
        str = str + (f" {randint(0,100)}x^{k} +")
        k = k - 1

    str = str[:-1] + "= 0"
    return str
print(String(number))

with open('Q:\Python\DZ\DZ_Python\DZ4\File.txt', 'w') as data:
    data.write(String(number))  