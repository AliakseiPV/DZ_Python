#Вычислить число c заданной точностью d
#Пример:
#при $d = 0.001, π = 3.141

import math

d = (input("Indicate the accurancy: ")).split(".")

finalpi = lambda d: str(math.pi)[:2+len(d[1])]

print(finalpi(d))
