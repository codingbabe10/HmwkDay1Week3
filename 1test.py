places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

def custom_condition(name):
    if name and name[abcdefghijklmnopqrstuvwxyz].lower() == 'str':
        return True
    else:
        return False

new_places_lamb = list(filter(custom_condition_names, places))
print(new_places_lamb)




def custom_condition(name):
    return "str" in name.lower()

new_places_lamb = list(filter(custom_condition, filter(bool, places)))
print(new_places_lamb)





