import copy
import decimal

# 1 - don't add or delete items from a list while looping over it
#     it WILL cause bugs
# wrong approach - i skips over an item because items were shifted down
greetings = ['hello', 'hello', 'mello', 'yello', 'hello']
for i, word in enumerate(greetings):
    if word != 'hello':
        del greetings[i]

print(greetings)  # ['hello', 'hello', 'yello', 'hello']

# right approach - create a new list and substitute the old one
greetings = ['hello', 'hello', 'mello', 'yello', 'hello']
newGreetings = []
for word in greetings:
    if word == 'hello':
        newGreetings.append(word)

greetings = newGreetings  # Replace the original list
print(greetings)

# better approach with list comprehension
greetings = ['hello', 'hello', 'mello', 'yello', 'hello']
greetings = [word for word in greetings if word == 'hello']
print(greetings)


# 2 - don't copy mutable values without copy.copy() and copy.deepcopy()
#     copy doesn't copy mutable nested objects, so it's recommended to ALWAYS use deepcopy
# wrong approach
spam = ['cat', 'dog', 'eel']
cheese = spam
spam[2] = 'MOOOOOSE'
print(spam)
print(cheese)  # cheese has moose because python assignments copy references, not objects

# right approach
spam = ['cat', 'dog', 'eel']
cheese = copy.copy(spam)  # should use deepcopy
spam[2] = 'MOOOOOSE'
print(spam)
print(cheese)  # cheese is unchanged because copy created a shallow copy of spam


# 3 - don't use mutable values for default arguments
# wrong approach
def add_ingredient(ingredient, sandwich=['bread', 'bread']):
    sandwich.insert(1, ingredient)
    return sandwich


my_sandwich = add_ingredient('avocado')
print(my_sandwich)
another_sandwich = add_ingredient('lettuce')
print(another_sandwich)  # another sandwich has avocado now because sandwich gets changed every call

# right approach
# function creates a new mutable object each time the function is called


def add_ingredient2(ingredient, sandwich=None):
    if sandwich is None:
        sandwich = ['bread', 'bread']
    sandwich.insert(1, ingredient)
    return sandwich


my_sandwich = add_ingredient2('avocado')
print(my_sandwich)
another_sandwich = add_ingredient2('lettuce')
print(another_sandwich)


# 4 - don't build strings with string concatenation when doing a lot (over 100000 loops) of string concatenation
#     it's very slow because every concat creates a new string object!
# unpythonic way
final_string = ''
for i in range(10):
    final_string += 'spam '

print(final_string)

# pythonic way - 10 times faster
final_string = []
for i in range(10):
    final_string.append('spam')

final_string = ' '.join(final_string)
print(final_string)


# 5 - don't expect sort() to sort alphabetically
# wrong approach
letters = ['A', 'z', 'Z', 'a']
letters.sort()
print(letters)  # prints ['A', 'Z', 'a', 'z']

# right approach
letters = ['A', 'z', 'Z', 'a']
letters.sort(key=str.lower)
print(letters)


# 6 - don't assume floats are perfectly accurate
# wrong approach
print(0.1 + 0.1 + 0.1)  # 0.30000000000000004
print(0.3 == (0.1 + 0.1 + 0.1))  # False

# right approach
d = decimal.Decimal('0.1')  # needs to be passed as string or int to avoid the above
print(d + d + d)  # 0.3


# 7 - don't chain != operators
# when chaining operators is fine
six = half_dozen = 6
3 < six < 9

# wrong approach (bug)
a = 'cat'
b = 'dog'
c = 'cat'
print(a != b != c)  # True - this is equivalent to "(a != b) and (b != c)"


# 8 - don't forget the comma in single item tuples
spam = ('cat', 'dog', 'moose')
print(spam[0])  # 'cat'
spam = ('cat')
print(spam[0])  # 'c' - python evaluates the string!
spam = ('cat',)
print(spam[0])  # 'cat'
