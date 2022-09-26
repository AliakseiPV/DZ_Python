import string
import data_provider


def name_view():
    data = data_provider.get_name()
    return data

def last_name_view():
    data = data_provider.get_last_name()
    return data

def date_view():
    data = data_provider.get_date()
    return data    

def phone_view():
    data = data_provider.get_phone_number()
    return data

def find_number():
    number = input("Enter the number: ")
    with open('Q:\Python\DZ\DZ_Python\DZ7\my_txt.txt', 'r') as data:
        for i in data:

            if number in i:
                return i

def find_full_name():
    name = str.lower(input("Enter the name: "))
    last_name = str.lower(input("Enter the last name: "))
    with open('Q:\Python\DZ\DZ_Python\DZ7\my_txt.txt', 'r') as data:
        for i in data:

            if (name in str.lower(i)) and (last_name in str.lower(i)):
                return i                