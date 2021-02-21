# 1 - use enumerated() instad of range()
animals = ['cat', 'dog', 'moooooose']
for i, animal in enumerate(animals):  # better than using range(len(animals))
    print(i, animal)

for animal in animals:  # loop that has no need for index
    print(animal)


# 2 - use with instead of open() and close()
#         automatically calls close() after the execution
with open('spam.txt', 'w') as file_object:
    file_object.write('Hello world!')


# 3 - use is to compare with None instead of ==


# 4 - format strings with f-strings
name, day, weather = 'Pedro', 'Sunday', 'cloudy with a chance of meatballs'
print(f'Hello, {name}! Today is {day} and it is {weather}')


# 5 - use get() and setdefault() with dictionaries
#         evaluates if key exists. if yes, gets value. if not, passes argument as value
#         much better than using if/else to avoid KeyErrors
number_of_pets = {'dogs': 2}
print('I have', number_of_pets.get('cats', 0), 'cats.')

number_of_pets = {'dogs': 2}
number_of_pets.setdefault('cats', 0)  # does nothing if 'cats' exists
number_of_pets['cats'] += 2
print('I have', number_of_pets.get('cats', 0), 'cats.')


# 6 - use dictionaries instead of a switch statement
# unpythonic code
season = ''

if season == 'Winter':
    holiday = 'New Year\'s Day'
elif season == 'Spring':
    holiday = 'May Day'
elif season == 'Summer':
    holiday = 'Juneteenth'
elif season == 'Fall':
    holiday = 'Halloween'
else:
    holiday = 'Personal day off'

print(holiday)  # returns Personal day off

# pythonic code
season = 'Spring'
holiday = {
    'Winter': 'New Year\'s day',
    'Spring': 'May Day',
    'Summer': 'Juneteenth',
    'Fall': 'Halloween'
}.get(season, 'Personal day off')
print(holiday)  # returns May Day


# 7 - ugly ternary (it's ugly as a feature! use if/elses)
# pythonic code with if/else
condition = True
if condition:
    message = 'Access granted'
else:
    message = 'Access denied'
print(message)

# pythonic code with ternary
value_if_true = 'Access granted'
value_if_false = 'Access denied'
condition = True
message = value_if_true if condition else value_if_false  # self-explanatory syntax
print(message)

condition = False
message = value_if_true if condition else value_if_false
print(message)


# 8 - chaining assignment and comparison operators
# unpythonic example
spam = 50
if 42 < spam and spam < 99:
    spam + 1

# pythonic example
spam = 50
if 42 < spam < 99:
    spam + 1

# pythonic example
spam = eggs = bacon = 50
print(spam, eggs, bacon)


# 9 - check whether a variable is one of many values
# unpythonic example (repeats 'spam ==' multiple times)
spam = 'cat'
if spam == 'cat' or spam == 'dog' or spam == 'moose':
    spam = 'animal'

# pythonic example (using tuples)
spam = 'cat'
if spam in ('cat', 'dog', 'moose'):
    spam = 'meow!'
print(spam)


# 10 - pay attention to the difference between == and is
#      == - compares values
#      is - compares references
spam = {'name': 'Pedro'}
eggs = spam
spam is eggs  # True - reference is the same
spam == eggs  # True - value is the same
bacon = {'name': 'Pedro'}
spam == bacon  # True - value is the same
spam is bacon  # false - reference is different!
