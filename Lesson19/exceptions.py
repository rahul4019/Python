class JustNotCoolError(Exception):
    pass

x = 2
try:
    raise JustNotCoolError("This isn't cool, man.")
    # raise Exception("I'm a custom exception!")
    # print(x/0)
    # print(x/1)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed")
except NameError:
    print('NameError means something is probable undefined.')
except ZeroDivisionError:
    print('Please do not divide by zero.')
except Exception as error: # catch every type of error
    print(error) # print that error
else:
    print('No errors!')
finally:
    print("I'm going to print with or without an error.")
