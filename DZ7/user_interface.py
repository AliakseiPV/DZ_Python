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
