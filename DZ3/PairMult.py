#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
#второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

myList = [2, 3, 4, 5, 6]

def PairMult(numbers):
    
    i = 0
    mult = 1

    while(i < len(numbers)/2):
        mult = numbers[i] * numbers[len(numbers)-i-1]
        print(mult)
        i+=1



PairMult(myList)    