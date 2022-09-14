#Вычислить число c заданной точностью d
#Пример:
#при $d = 0.001, π = 3.141

import math

d = (input("Indicate the accurancy: ")).split(".")
dec = len(d[1])


pi =(math.pi)
print(round(pi,dec))
