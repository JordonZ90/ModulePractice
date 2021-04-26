import random

#  using the random method
number = random.random()  # a float value >= 0.0 and < 1.0
number = random.random() * 100  # a float value >= 0.0 and < 100

#  using the randint method
numbers = random.randint(1, 100)  # an int from 1 to 100
numbers = random.randint(101, 200)  # an int from 101 to 200
numbers = random.randint(0, 7)  # an int from 0 to 7

#  using the randrange method

numbers = random.randrange(1, 100)  # an int from 1 to 99
numbers = random.randrange(100, 200, 2) # an even int from 100 to 190
numbers = random.randrange(11, 250, 2)  # an odd int from 11 to 2249

# simulating a dice roll

die1 = random.randint(1, 6)  # assume 5 is returned
die2 = random.randint(1, 6)  # assume 5 is returned
print(f"Your roll: {die1}, {die2}")  # Your roll: 6, 5
