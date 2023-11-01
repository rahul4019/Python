def add_one(num):
    # base case
    if (num >= 9):
        return num + 1

    # small work
    total = num + 1
    print(total)

    # recursive call
    return add_one(total)


myNewTotal = add_one(0)

print(myNewTotal)


