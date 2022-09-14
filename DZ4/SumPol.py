
with open('Q:\Python\DZ\DZ_Python\DZ4\File.txt') as source, open('Q:\Python\DZ\DZ_Python\DZ4\SumFile.txt', 'w') as destination:
    for line in source:
        destination.write(line) 


file = open('Q:\Python\DZ\DZ_Python\DZ4\SumFile.txt', 'r+')
file.write("\n")
for i in file:
    file.write(i[:-3] + "+")
file.close()
          

with open('Q:\Python\DZ\DZ_Python\DZ4\polinomial.txt') as source, open('Q:\Python\DZ\DZ_Python\DZ4\SumFile.txt', 'a') as destination:
    for line in source:
        destination.write(line) 