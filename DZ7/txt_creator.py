from user_interface import name_view
from user_interface import last_name_view
from user_interface import date_view
from user_interface import phone_view

def create(data):
        n,l,d,p = data        
        with open('my_txt.txt', 'a') as page:
                page.write(f'Name: {n}\t')
                page.write(f'Last name: {l}\t')
                page.write(f'Birth date: {d}\t')
                page.write(f'Phone number: {p}\n')