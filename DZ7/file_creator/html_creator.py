from user_interface import name_view
from user_interface import last_name_view
from user_interface import date_view
from user_interface import phone_view

def create(data):
    n,l,d,p = data
    style = 'style="font-size:30px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    html += '    <p {}>Name: {} </p>\n'\
        .format(style, n)
    html += '    <p {}>Last name: {} </p>\n'\
        .format(style, l)
    html += '    <p {}>Birth date: {} </p>\n'\
        .format(style, d)
    html += '    <p {}>Phone number: {} </p>\n'\
        .format(style, p)
    html += '  </body>\n</html>'
    
    with open('Q:\Python\DZ\DZ_Python\DZ7\data\my_html.html', 'a') as page:
        page.write(html)
