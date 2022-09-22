#Вычислить число c заданной точностью d
#Пример:
#при $d = 0.001, π = 3.141

import math

d = (input("Indicate the accurancy: ")).split(".")

def PiNumber(accuracy):
    dec = len(accuracy[1])
    pi =str(math.pi)
    print(dec)
    finalpi = pi[:2+dec]
    return float(finalpi)


print(PiNumber(d))