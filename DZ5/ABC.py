#1
file = open('Q:\Python\DZ\DZ_Python\DZ5\MyFile.txt', 'r')
data = file.read()
file.close()


inputStr = data.split()

outputStr = [i for i in inputStr if "abc" not in i]

print(" ".join(map(str,outputStr)))
