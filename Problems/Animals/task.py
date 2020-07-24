# read animals.txt
# and write animals_new.txt
animals_file = open('animals.txt', 'r')
new_animals_file = open('animals_new.txt', 'w')
list_of_animals = animals_file.readlines()
for animal in list_of_animals:
    new_animals_file.write(animal.replace('\n', ' '))

animals_file.close()
new_animals_file.close()
