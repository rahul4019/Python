# LISTS
users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

emptyList = []

print("Dave" in users)  # returns boolean
print("Dave" in emptyList)

print(users[0])  # get list item based on index
print(users[-1])  # get last item in the list

print(users.index('Sara'))  # get index of an item in the list

# returns items based on provided index starting index is inclusive while last index is not
print(users[0:2])

# returns all the items from the provided index till the end of the list
print(users[1:])
print(users[-3:-1])

print(len(data))  # returns the length of the list

users.append('Rahul')  # inserts the item at the end of the list
print(users)

# Methods to INSERT items in a list
users += ['Jason', 'Elsa']
print(users)

users.extend(['Robert', 'Jimmy'])
print(users)

""" users.extend(data)
print(users) """

users.insert(0, 'Bob')
print(users)

users[2:2] = ['Eddie', 'Alex']  # does not replace items in the list
print(users)

users[1:3] = ['Robert', 'JPJ']  # replaces items in the list
print(users)

# Methods to REMOVE items in a list

users.remove('Bob')  # removes the item from the list
print(users)

print(users.pop())  # removes the last item in the list and returns it
print(users)


del users[0]  # deletes the item from the list based on the index
print(users)

# we can also use this method to delete the list completely
# del data
# print(data) # will give error

data.clear()  # will make the list empty but the list will still exist
print(users)


users[1:2] = ['dave']

users.sort()  # sorts the list alphabatically
print(users)

# will sort the list considering the items starting with lower case
users.sort(key=str.lower)
print(users)

nums = [4, 29, 19, 12, 5, 1]
nums.reverse()
print(nums)

# nums.sort(reverse=True) # sorted list in decreasing order
# print(nums)


print(sorted(nums, reverse=True))  # doesn't modify ORIGINAL list
print(nums)

numsCopy = nums.copy  # copies the list
print(numsCopy)

# copies the passed list and returns the ADDRESS of the copied array
myNums = list(nums)
print(myNums)

myCopy = nums[:]
print(myCopy)

print(type(nums))

# TUPLES

# Tuples can't be changed
myTuple = tuple(('Dave', 43, True))
anotherTuple = (1, 4, 2, 8, 3, 2, 3, 2)

print(myTuple)
print(type(myTuple))
print(type(anotherTuple))

newList = list(myTuple)  # this will create a new list out of the passed TUPLE
print(newList)
print(type(newList))

newList.append("Neil")
newTuple = tuple(newList)
print(newTuple)
print(type(newTuple))

# UNPACKING of tuple
# (one, two, *hey) = anotherTuple
(one, *two, hey) = anotherTuple
print(one)
print(two)
print(hey)

# counts the occurances of passed number in the tuple
print(anotherTuple.count(2))
