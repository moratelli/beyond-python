# 1 - function names
#     - should usually have a verb - get_login_credentials() or set_password()
#     - bigger but more descriptive names are better than shorter but ambiguous names


# 2 - function size
#     - shorter is not always better
#     - don't get tangled up in "1 function, 1 action"
#     - incredibly short functions might result in simpler functions, but it raises overall complexity
#     - make them as short as reasonably possible but not any shorter


# 3 - function parameters and arguments
#     - beware functions with too many parameters
#     - 0 to 3 is fine but more than 5 or 6 is too many
#     - solution: split the function into smaller functions

# 3.1 - default arguments
#       - one way to reduce complexity
#       - never use mutable objects as default args ({}, [])
def introduction(name, greeting='Hello'):
    print(f'{greeting}, {name}')


introduction('Alice')
introduction('Alice', 'Bonjour')

# 3.2 - using * and ** to pass args to functions
# * == pass items in an iterable object ((), [])
print('cat', 'dog', 'moose')    # cat dog moose
args = ['cat', 'dog', 'moose']
print(args)  # ['cat', 'dog', 'moose'] - includes brackets and commas
print(*args)  # cat dog moose - the same as print(args[0], args[1], args[2])

# ** == pass items in a mappable object ({}) as keyword args
print('cat', 'dog', 'moose', sep='-')  # cat-dog-moose
kw_args_for_print = {'sep': '-'}
print('cat', 'dog', 'moose', **kw_args_for_print)  # cat-dog-moose

# 3.3 - using * to create variadic functions
#       - functions that recieve a varying number of args
#       - if a function usually deals with a data structure created while the program
#         is running, it’s better to have it accept a single parameter. if a function
#         usually deals with arguments that the programmer specifies while writing the
#         code, it’s better to use * to accept a varying number of arguments


def product(*args):
    result = 1
    for num in args:
        result *= num
    return result


print(product(3, 3))  # 9
print(product(2, 1, 2, 3))  # 12

# 3.4 - using * and ** to create wrapper functions
#       - functions that pass on args to another function and return that function's return value


def print_lower(*args, **kwargs):
    args = list(args)  # creates list from args tuple
    for i, value in enumerate(args):
        args[i] = str(value).lower()
    return print(*args, **kwargs)


print_lower('DOG', 'CAT', 'MoOoOsE', sep=', ')  # dog, cat, moooose


# 4 - functional programming
#     - paradigm that emphasizes writing functions without modifying globals or any external state

# 4.1 - side effects
#       - changes a function makes to part of the program outside its own code and local variables
#       - deterministic functions: always return the same value when the same args are passed
#       - a deterministic function with no side effects is called a pure function
#       - we should write pure functions whenever possible, avoiding globals

# 4.1 - high-order functions
#       - functions that accept other functions as args or return functions as return values
def call_it_twice(func, *args, **kwargs):
    func(*args, **kwargs)
    func(*args, **kwargs)


call_it_twice(print, 'Hello World!')


# 4.2 - return values should aways have the same data type
#       - we should always attempt to make functions return values of a single data type
