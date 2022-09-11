#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:
#для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


k = int(input("Enter the number: "))
myList = [0, 1]
finalList = [0, 1]

def Fibonacci(myList1, myList2):
    i = 1
    while(i < k):
        myList1.append(myList1[i] + myList1[i-1])
        i+=1    

    i = 1
    while(i < k):
        myList2.append((myList2[i-1]) - (myList2[i]))
        i+=1

    del myList2[0:1]
    myList2.reverse()

    myList2.extend(myList1)

Fibonacci(myList,finalList)
print(finalList)

