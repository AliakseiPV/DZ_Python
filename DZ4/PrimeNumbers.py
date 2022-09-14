#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#"20" -> [2, 2, 5]

N =int(input("Enter the number: "))

def PrimeNumbers(number):
    primeNumbers = []
    finalList = []
    count = 0
    for i in range(2,number+1):

        for j in range(2,i):
            if(i % j == 0):
                count = count + 1
        if(count == 0):
            primeNumbers.append(i)
        else:
            count = 0


    while(number > 1):
        if(number % primeNumbers[count] == 0):
            finalList.append(primeNumbers[count])
            number = number / primeNumbers[count]
        else: count = count + 1    
    
    return finalList

print(PrimeNumbers(N))