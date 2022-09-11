import math


impotr: math

print("Enter the x cordinante of point A")
A_x =int(input())
print("Enter the y cordinante of point A")
A_y =int(input())

print("Enter the x cordinante of point B")
B_x =int(input())
print("Enter the y cordinante of point B")
B_y =int(input())

print(f"Distance: {round(math.sqrt((A_x - B_x)**2 +(A_y - B_y)**2),3)}")