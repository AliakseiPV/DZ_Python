#Реализуйте алгоритм перемешивания списка.
import random


print('Enter something in " "')
str = input()

myList = []
myList = str.split(" ")
print(myList)

random.shuffle(myList)
print(myList)