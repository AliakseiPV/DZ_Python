from datetime import *
import random


def get_name():
    return input("Name: ")

def get_last_name():
    return input("Last name: ")

def get_date():
    date1 = datetime.strptime("01/01/1980","%d/%m/%Y")
    date2 = datetime.strptime("01/01/2010","%d/%m/%Y")
    delta = date2 - date1
    return date1 + timedelta(random.randint(0, delta.days))

def get_phone_number():
    return input("Phone number: ")

def data_collection():
    return (get_name(), get_last_name(),get_date(),get_phone_number())