#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
#между максимальным и минимальным значением дробной части элементов.
#Пример:
#- [1.1, 1.2, 3.1, 10.01] => 0.19


myList = [1.1, 1.2, 3.1, 10.01]


def MaxMinDif(numbers):
   
    outputList = list(map(lambda i: round((i%1),2), numbers))
   
    difference = max(outputList) - min(outputList)

    return difference

print(MaxMinDif(myList))