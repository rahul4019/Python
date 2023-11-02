name = "Rahul"
count = 0

def anotherFunction():
    color = "blue"
    # count += 1 # unbound local error
    global count  # cannot modify global count without using keyword 'global' before it
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = 'red'
        print(color)
        print(name)
    greeting("Rahul")

anotherFunction()
