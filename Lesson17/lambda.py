# squared = lambda num : num * num

from functools import reduce
def squared(num): return num * num


# print(squared(2))
print(squared(2))


def addTwo(num): return num + 2


print(addTwo(3))


def sum_total(a, b): return a + b


print(sum_total(2, 7))

##################


def funcBuilder(x):
    return lambda num: num + x


addTen = funcBuilder(10)  # using concept of closure
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

###############

lambda num: num * num

numbers = [3, 7, 12, 18, 20, 21]

squaredNums = map(lambda num: num * num, numbers)

print(list(squaredNums))


###############

odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))


numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers)

print(total)

print(sum(numbers)) # buitin function



names = ['Rahul', 'Pankaj', 'Deepak', 'Ankit']

char_count = reduce(lambda acc, curr: acc + len(curr),names, 0)

print(char_count)
