
print("Enter x: ")
x = int(input())

print("Enter y: ")
y = int(input())

if x != 0 or y != 0:
    if x > 0 and y > 0:
        print("Quarter: 1")
    elif x < 0 and y > 0:
        print("Quarter: 2")
    elif x < 0 and y < 0:
        print("Quarter: 3")
    elif x > 0 and y < 0:
        print("Quarter: 4")
else:
    print("x and y can not be equal to zero")


