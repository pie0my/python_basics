print(18 // 4)
print(7 % 4)
print(type(2 + 2))
print(type(2 * 2))
print(2 / 2)
print(type(2 * 1.1))

print(round(3.51))
print(abs(-11))
print(20 - 2 * 4)
print((5 + 4) * 10 / 2)

print(((5 + 4) * 10) / 2)

print((5 + 4) * (10 / 2))

print(5 + (4 * 10) / 2)

print(5 + 4 * 10 // 2)

iq = 100
my_age = iq / 4

print(iq)
print(my_age)

first_name = 'Eric'
last_name = 'Estorani'
full_name = first_name + ' ' + last_name
desenhozinho = '''
////
O O
__
//
'''

print(full_name)
print(desenhozinho)

weather = "\t It\'s \"kind of\" sunny \n hope you have a good day"
print(weather)

print('''


''')

name = 'Nakamoto'
age = 26

print(f'hi {name}.You are {age} years old')

print('''


''')

print("Hello {}, your balance is {}.".format("Cindy", 50))
print('''


''')

exercise_name = 'Cindy'

balance = 50

print(f'Hello {exercise_name}, your balance is {balance}.')
print('''



''')

gauchonoia = '0123456789'

print(gauchonoia[:9])
print(gauchonoia[::3])
print('''


''')

python = 'I am PYHTON'

print(python[1:4])
print(python[1:])
print(python[:])
print(python[1:100])
print(python[-1])
print(python[-4])
print(python[:-3])
print(python[-3:])
print(python[::-1])

# I AM PYHTON
# 0123456789

# _am
# _am PYTHON
# Tudo
# TUDO sem o I
# N
# H
# I am PYH
# TON
# INVERSO

print(python[0])

print('''


''')

print(len('01234567'))

print('''

''')

quote = 'ser ou não ser, eis a questão'

print(quote.upper())
print(quote.capitalize())
print(quote.find('ou'))
print(quote.replace('ser', 'naka'))

print('''


''')
birth_year = input('what year were you born?')
print(type(birth_year))
age = 2021 - int(birth_year)
print(f'your age is: {age}')
print('''




''')

# password checker
login = input('what it your user name:')
password = input('what is your password:')
# one way to do:
#A = password.replace('e','*').replace('i','*').replace('c','*').replace('r','*').replace('a','*').replace('b','*').replace('d','*').replace('f','*').replace('g','*').replace('h','*').replace('j','*').replace('k','*').replace('l','*').replace('m','*').replace('n','*').replace('o','*').replace('p','*').replace('q','*').replace('s','*').replace('t','*').replace('u','*').replace('v','*').replace('x','*').replace('w','*').replace('y','*').replace('z','*')
# this one above was the first way that I did, and then the fastest:
tamanho = len(password)
hidden_password = '*' * tamanho
print(
    f'your login is {login}, your password {hidden_password} is {tamanho} letters long'
)

print('''


''')

# list
# principle of create a list and the itens btweent the list will be listed when you wante it, between  ","  like [0]

supermarket_cart = ['arroz', 'feijão', 'pao']

print(supermarket_cart[0:2:2])

# the principle of slicing in string is the same for list
# was string = 'hellooo', so print(string[0:2:1]), was going to print the string from 0 to 2, one by one

# [where to start: where to stop(exclusive)]
# If you set [0:0]
# You are giving to contradictory orders.. it means:
# [i want you to start at "arroz": I want you to stop at "arroz" but excluding it]
# supermarket_cart = [0:'arroz',1: 'feijão',2: 'pao']
# you are excluding "pao"
# and also because you have this:
# [0:2:2]
# you are skipping one of them
# supermarket_cart = [(included)'arroz', (skip)'feijão', (included, but you have [0:2] so it's excluded)'pao']

supermarket_cart[0] = 'banana'
new_supermarket_cart = supermarket_cart[:]
new_supermarket_cart[0] = 'frango'
print(new_supermarket_cart)
print(supermarket_cart)

# when I'm trying to copy a list and do not change it from the definition, I will copy the itens of the list [:], otherwise I was going to change the composition of the supermarket list

# exercise:
new_list = ['a', 'b', 'c']
print(new_list[1])
print(new_list[-2])
print(new_list[1:3])
new_list[0] = 'z'
print(new_list)

my_list = [1, 2, 3]
bonus = my_list + [5]
my_list[0] = 'z'
print(my_list)
print(bonus)

# answers: A) 1: b; 2:b ; 3: b,c; 4: z,b,c
# B) 1: z,2,3; 2: 1,2,3,5
# because of the order of each statement
# bonus = my_list + [5]
# my_list[0] = 'z'
# you create bonus before
# modifying my_list
# so, from that point
# bonus and my_list are to independent objects
# think as them as boxes
# bonus uses the content on my_list box, copy it and then add 5
# but they are to boxes indeed
# so if you modify my_list after creating the box bonus
# it wont care about that change

# matrix -> REAAADDDDDDDDDDDDDDDDDDDDD
# basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]]
# print(basket[1][1][0])

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# exercise
# 1. Remove the Banana from the list

# 2. Remove "Blueberries" from the list.

# 3. Put "Kiwi" at the end of the list.

# 4. Add "Apples" at the beginning of the list

# 5. Count how many apples in the basket

# 6. empty the basket

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# print(basket)
# basket.remove("Blueberries") -> also use pop for delet last item
# print(basket)
# basket.insert(4,"Kiwi") -> also use append for add last item
# print(basket)
# basket.insert(0,"Apples")
# print(basket)
# basket.count("Apples")
# print(basket.count("Apples"))
# basket.clear()
# print(basket)

friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']
new_friend = ['Stanley']
friends.extend(new_friend)
friends.sort()
print(friends)

# #list unpacking ->>>>>> NICE NOTE
# un1,b,c = [1,2,3]
# print(un1)

# Concatenating with "+" does not modify the original array, it creates a new array with copies of the original elements

# testingknolege = input('whats going on here:')

gameuser = {
    'age': 27,
    'username': 'chenez',
    'weapons': ['safadeza'],
    'is_active': True,
    'clan': 'unidospelochenez'
}

print(gameuser.keys())
# gameuser.update({'weapons': ['safadeza' ,'cristiano_machado']})
# print(gameuser)
# this one above is another way to do the exercise
gameuser['weapons'].append('cristiano_machado')
print(gameuser)
gameuser.update({'is_banned': False})
print(gameuser)
gameuser['is_banned'] = True
print(gameuser)

print('''


''')
gameuser2 = gameuser.copy()
gameuser2.update({'username': 'lauro', 'age': 26})
print(gameuser2)

print('''


''')

school = {'Bobby', 'Tammy', 'Jammy', 'Sally', 'Danny'}

attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']

print(school.difference(attendance_list))

print(5 % 2)
