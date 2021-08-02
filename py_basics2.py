# conditional logic
is_old = True
is_licensed = True
# the order of power bellow

# if is_old:
#   print('you are old enought to drive')
# elif is_licensed:
#   print('you have license to drive')
# else:
#   print('you are not able to drive')

if is_old and is_licensed:
    print('you are old enought to drive, and you have license')
else:
    print('you are not able to drive')

#truthy and falsy
# each sentence can be a bool, to check use print(bool())
# every sentece is truthy, you can check in the website each that it is not:
# https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false

# this one here is harder, called ternary operation
# create one message operation, then if and the bool, after the bool sentence else, to create the negative answer

chenez_friend = False

message_to_friend = 'message allowed' if chenez_friend else 'chenez canalha'
print(message_to_friend)

if is_old or is_licensed:
    print('both of them')


# short circuit, will execute the first operation (in cases like if), because its easier

# logical operators: is or < > == != (not equal) => <=
# not means opposit
is_magician = False
is_expert = True

if is_magician and is_expert:
    print('you are a master magician')

elif is_magician and not is_expert:
    print('at least you\'re getting there')

elif not is_magician:
    print('you need magic powers')

# == means equality to value, and "is" checks if the value stored is the same; list are created individually, always different when trying to use is

# .itens() ; .values(); keys()
# ('name': 'golem'); ('golem'); ('name')
# those above are used in dictionaries loops, for x in x:

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = 0
for item in my_list:
    counter = counter + item

print(counter)

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f'index of 50 is: {i}')

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]
# picture.replace(0,'' '').replace(1,'*') error, there are no replace in lists
for row in picture:
    for pixel in row:
        if pixel == 0:
            print(' ', end='')
        elif pixel == 1:
            print('*', end='')
    print('')
    # the end is used to not jump a line after the changes
    # the last print '' means to jump a line after the row

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)


# https://www.youtube.com/watch?v=6iF8Xb7Z3wQ&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=7&ab_channel=CoreySchaferCoreySchaferVerificado

# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16016688#questions/8950878


# def checkDriverAge():
#   age = input("What is your age?: ")
#   if int(age) < 18:
# 	  print("Sorry, you are too young to drive this car. Powering off")
#   elif int(age) > 18:
# 	  print("Powering On. Enjoy the ride!");
#   elif int(age) == 18:
# 	  print("Congratulations on your first year of driving. Enjoy the ride!")

# checkDriverAge()
# checkDriverAge()
# checkDriverAge()

def checkDriverAge(age=0):
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")


checkDriverAge(92)
checkDriverAge(18)
checkDriverAge(17)
checkDriverAge(27)
checkDriverAge()


# def highest_even(li):
#   highest_even.sort()
#   if li % 2 == 0:
#     return highest_even([-1])

# print(highest_even([10, 2, 3, 4, 8, 11]))

def highest_even(li):
    even = []
    for item in li:
        if item % 2 == 0:
            even.append(item)
    return max(even)


print(highest_even([10, 2, 3, 4, 8, 11]))

x = 'Hello'[0]
print(x)
