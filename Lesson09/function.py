def hello_world():
    print("Hello World!")


hello_world()


def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return "Please provide numbers"
    return num1 + num2


# total = sum(2,3)
# total = sum(2,'string')
# total = sum(3)
total = sum()

print(total)

# to receive unknown number of arguments


def multiple_items(*args):
    print(args)
    print(type(args)) # tuple


multiple_items('dave', 'john', 'sara')


def multi_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs)) # dictionary


multi_named_items(first='dave', last='john')
