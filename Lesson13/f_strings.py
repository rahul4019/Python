person = "Rahul"
coins = 3

# Percent method
message = "\n%s has %s coins left." % (person, coins)
print(message)

# Format method
message = "\n{} has {} coins left." .format(person, coins)
print(message)

# Format method with index numbers
message = "\n{1} has {0} coins left." .format(coins, person)
print(message)

# Format method with variable name
message = "\n{person} has {coins} coins left." .format(
    person=person, coins=coins)
print(message)


# Format method with dictionary
player = {'person': 'Rahul', 'coins': 3}
message = "\n{person} has {coins} coins left." .format(**player)
print(message)

################
# f-strings! This is the way.

message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{person} has {2 * 3} coins left."
print(message)

message = f"\n{person.lower()} has {2 * 3} coins left."
print(message)

message = f"\n{player['person']} has {2 * 3} coins left."
print(message)

##########
# You can pass formatting options

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"\n2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"\n2.25 devided by {num} is {num / 4.52:.2f}")


