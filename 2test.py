places = [" ", "Argentina", " ", "San Diego", "", "  ", "", "Boston", "New York"]

def custom_condition(places):
    if "str" in places.lower():
        return True
    else:
        return False

new_places_lamb = list(filter(custom_condition, filter(lambda x: x.strip() != "", places)))
print(new_places_lamb)
