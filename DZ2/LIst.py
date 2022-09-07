#Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

k = int(input())
result = []



for element in range(1,k+1):
    total= (1 + 1/element)**element
    result.append(total)

print(result)  