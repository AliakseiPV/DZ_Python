#Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#Найдите произведение элементов на указанных пользователем через пробел позициях.

print("Enter the number")
N = int(input())

print("enter the first position")
firstPozition = int(input())

print("enter the secont pozition")
secondPozition = int(input())

numbers = [] 
result = 1

for i in range(-N,N+1):
    numbers.append(i)
print(numbers)

for i in numbers[firstPozition:secondPozition]:
    result*= i
print(result)