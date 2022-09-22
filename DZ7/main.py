#Задание в группах: Создать телефонный справочник
# с возможностью импорта и экспорта данных в нескольких форматах.
import data_provider
import html_creator
import txt_creator
import xml_creator

data = data_provider.data_collection()

html_creator.create(data)
xml_creator.create(data)
txt_creator.create(data)
