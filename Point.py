
print("Enter number between 1 to 4")
n = int(input())

if n == 1:
    print("x > 0 and y > 0")
elif n == 2:
    print("x < 0 and y > 0")
elif n == 3:
    print("x < 0 and y < 0")
elif n == 4:
    print("x > 0 and y < 0")
else:
    print("Default")