#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def encode(data):
 
    encoding = ""
 
    i = 0
    while i < len(data):
        count = 1

        while i + 1 < len(data) and data[i] == data[i + 1]:
            count += 1
            i += 1
 
        encoding += str(count) + data[i]
        i += 1

    return encoding
 
data = 'AAAAAAAAABBCCCDDDDD'
print(encode(data))












