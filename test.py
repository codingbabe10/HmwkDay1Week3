
#Exersize 1
places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]
filtered_places = list(filter(lambda x: x.strip(), places))
print(filtered_places)


#Exersize 2 
names = ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']

F = lambda name: name.split()[-1].lower()

names.sort(key=F)

print(names)




#Exersize 3
CtoF= [('Nashua', 32), ("Boston", 12), ("Los Angeles", 44), ("Miami", 29)]


celsius_to_fahrenheit = lambda data: (data[0], (9/5) * data[1] + 32)


converted_CtoF = list(map(celsius_to_fahrenheit, CtoF))

print(converted_CtoF)



#Exersize 4 
def fibonacci_sequence(n, a=0, b=1, iteration=0):
    if iteration <= n:
        print(f"Iteration {iteration}: {a}")
        fibonacci_sequence(n, b, a + b, iteration + 1)

fibonacci_sequence()






