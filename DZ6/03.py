#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#- [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12


myList = list(map(int,input("Enter the numbers in space: ").split()))

List = [myList[i] for i in range(len(myList)) if i%2 != 0]

print(sum(List))
