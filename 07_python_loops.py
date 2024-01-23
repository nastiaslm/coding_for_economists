# Let's have a look at loop syntax 

# for loop operate on "iterables"

# Let's create an interable object 
myList = [1,2,'abc']

# Let's iterate over the object 
for item in myList:
  #Loop body needs to be intended once
  if item == 1:
   print(item)
else:
  print("item not equal to 1.")

# Looping over a range of values
print("Using range(5)")
for i in range(5): # range() generates value of the fly 
  print(i)

# ANother way to do it
range_vals = [0, 1, 2, 3, 4] # Not memory efficient
print("Using a list to display values 0-4")
for i in range_vals:
  print(i)

# Looping over list of strings and nesting loops 
for name in ["Alice", "Bob", "Jim"]:
  print(name)
  # Iterate through each string 
  for letter in name:
    print(letter)

# Using the ennumerate() function to get both index and value 
print("Using enumerate()")
for index, value in enumerate(["Alice", "Bob", "Jim"]):
  print(index, value)

# Equivalent loop using indexing
print("Using range() and indexing")
myList = ['Alice', 'Bob', 'Jim']
for index in range(len(myList)):
  print(index, myList[index])

# Use a loop to create a list of capital letters from A-Z
print("Using a loop to create a list of capital letters from A-Z")

# Instantiate an empty list to append to
alphabet = []

for i in range(65, 91):
  alphabet.append(chr(i))

print(alphabet)

# while loops
# while loops are used when you don't know how many times you want to loop

# Instantiate counter variable
i = 0
while i < 10:
  print(i)
  # increment our counter every iteration, otherwise it iwll loop forever 
  i += 1

# List comprehensions 

# Let's have a look at a for loop creating a list of squares from 0 to 10

squares = []
for num in range(0, 11):
  squares.append(num**2)
  
print(squares)

# Doing the same using list comprehension
squares = [num**2 for num in range(0, 11)]
print(squares)

# Using if statements in list comprehension to get squares of even numbers 
even_squares = [num**2 for num in range(0, 11) if num % 2 == 0]

print(even_squares)