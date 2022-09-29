#Задание в группах: Создать телефонный справочник
# с возможностью импорта и экспорта данных в нескольких форматах.
import data_provider
import user_interface
from file_creator import html_creator
from file_creator import txt_creator
from file_creator import xml_creator
import data_import

data = data_provider.data_collection()

#html_creator.create(data)
#xml_creator.create(data)
txt_creator.create(data)

#print(user_interface.find_number())
#print(user_interface.find_full_name())

data_import.convert()