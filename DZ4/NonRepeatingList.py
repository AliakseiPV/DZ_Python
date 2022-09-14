#Задайте последовательность чисел. Напишите программу, которая выведет список
#неповторяющихся элементов исходной последовательности.
#[1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

inputList = [1, 1, 2, 3, 4, 5, 5]
outputList = list(set(inputList))
finalList = []


count = 0
for i in outputList:

    for j in inputList:
        if (i == j):
            count += 1
        print(f"i:{i} ////// j:{j} ///////// count:{count}")

    if(count <= 1):
        finalList.append(i)
    count = 0

print(finalList)



    