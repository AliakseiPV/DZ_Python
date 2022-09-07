#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#- 0,56 -> 11

print("Enter the decimal number: ")
N = input()
sum = 0
N = N.replace(".","")

for i in N:
    sum += int(i)
print(sum)