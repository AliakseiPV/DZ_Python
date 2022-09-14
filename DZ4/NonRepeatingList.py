#Задайте последовательность чисел. Напишите программу, которая выведет список
#неповторяющихся элементов исходной последовательности.
#[1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]


inputList = [1, 1, 2, 3, 4, 5, 5]
outputList = list(set(inputList))
finalList = []

def NonRepeatingList(list1, list2, list3):
    count = 0
    for i in list2:

        for j in list1:
            if (i == j):
                count += 1

        if(count <= 1):
            list3.append(i)
        count = 0
    return list3   


print(f"{inputList}  =>  {NonRepeatingList(inputList,outputList,finalList)}")





    