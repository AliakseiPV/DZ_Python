from user_interface import name_view
from user_interface import last_name_view
from user_interface import date_view
from user_interface import phone_view

def create(data):
    n,l,d,p = data
    xml = '<xml>\n'
    xml += '    <name_view units = "">{}</name_view>\n'\
        .format(n)
    xml += '    <last_name_view units = "">{}</last_name_view>\n'\
        .format(l)
    xml += '    <date_view units = "">{}</date_view>\n'\
        .format(d)
    xml += '    <phone_view units = "">{}</phone_view>\n'\
        .format(d)
    xml += '</xml>'

    with open('new_xml.xml', 'a') as page:
        page.write(xml)

    return data
    