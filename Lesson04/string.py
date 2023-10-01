# String data type

# litral assignment
first = 'Rahul'
last = 'Kumar'

""" print(type(first))
print(type(first) == str)
print(isinstance(first, str)) """

# constructor function

fruit = str("Apple")

""" print(type(fruit))
print(type(fruit) == str)
print(isinstance(fruit, str)) """

# Concatination
fullname = first + " " + last
print(fullname)

fullname += '!'
print(fullname)

# Casting a number to a string
decade = str(1990)
print(type(decade))
print(decade)

statment = 'I like movies from the ' + decade + 's.'
print(statment)

# Multiple lines
multiline = '''
Hey, how are you?                                      

I was just checking in.    
                                All good?
'''

print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String methods

print(first)
# doesn't change the value of original variable, returns new string
print(first.lower())
# doesn't change the value of original variable, returns new string
print(first.upper())
print(first)

print(multiline.title())  # makes the starting alphabet of sentence capital
print(multiline.replace('good', 'ok'))
print(multiline)

print(len(multiline))
multiline += ''
multiline += '          ' + multiline
print(len(multiline))

print('Striping starts')
print(len(multiline.strip()))  # removes extra spaces
print(len(multiline.lstrip()))  # removes spaces from left side
print(len(multiline.rstrip()))  # removes spaces from right side

print('')

# Build a menu
title = 'menu'.upper()
print(title.center(20, '='))
print("Coffee".ljust(16, '.') + '$1'.rjust(4))
print("Muffin".ljust(16, '.') + '$2'.rjust(4))
print("CheeseCake".ljust(16, '.') + '$4'.rjust(4))

print('')

# string index values
print(first[0]) # first value
print(first[-1]) # last value of string
print(first[1:-1]) # second and second last value (excludes the provided last index)
print(first[0:]) #  goes till the end (includes the last value)

print('')

# Some methods return with boolean data
print(first.startswith('R'))
print(first.endswith('l'))