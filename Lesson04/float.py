# float type

import math

gpa = 3.28
y = float(1.14)

print(type(gpa))
print(isinstance(y, float))

# Built-in function for numbers

print(abs(gpa))  # absolute value
print(abs(gpa * -1))  # without the -ve

print(round(gpa))  # roundes of to the nearest integer value (3.28 => 3)

print(round(gpa, 1))  # roundes of to the nearest float value (3.28 => 3.3)

print(math.pi)
print(math.sqrt(64)) # square root of a number
print(math.ceil(gpa)) # roundes of to the nearest integer that is greater than or equal to original number
print(math.floor(gpa)) # roundes of to the nearest integer that is less than or equal to original number
 

# Casting a string to a number
zipCode = "110041"
zip_value = int(zipCode)
print(type(zip_value))

