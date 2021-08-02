# exercise.py


from functools import reduce


class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# 1


class Naka(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 2
my_cats = [Simon('Simon', 3), Sally('Sally', 4), Naka('Naka', 26)]

# 3
my_pets = Pets(my_cats)

# 4
my_pets.walk()
# 1 Add nother Cat

# 2 Create a list of all of the pets (create 3 cat instances from the above)
# my_cats = []

# 3 Instantiate the Pet class with all your cats use variable my_pets

# 4 Output all of the cats walking using the my_pets instance

# exercices: map, reduce, filter e zipfrom functools import reduce
# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalize(item):
    return item.capitalize()


print(list(map(capitalize, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

my_numbers.sort()

print(list(zip(my_strings, my_numbers)))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def over50(item):
    return item > 50


print(list(filter(over50, scores)))
# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, my_numbers, 0))
print(reduce(accumulator, scores, 15))

# also can use:
print(reduce(accumulator, (my_numbers + scores)))

# LAMBDA
# SQUARE LIST

lista = [5, 4, 3]

print(list(map(lambda item: item**2, lista)))

a = [(0, 2), (4, 3), (9, 9), (10, -1)]

a.sort(key=lambda x: x[1])
print(a)

# comprehension

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

duplicadas = list(
    set([char for char in some_list if some_list.count(char) > 1]))

print(duplicadas)


# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': True
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
