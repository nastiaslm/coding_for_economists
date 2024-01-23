# Code for conditionals
# Introduce packages

import random

# Generate random integer between 20 and 34

random_number = random.randint(20, 34) #Randint is the function of the package
print(random_number) # we get a different number each time we run the script

#Python Docs for quations about the functions

#First look at conditional statements

if random_number < 25:
    print("The number is less than 25") #works only with tab
elif random_number <30:
    print("The number is greater than 30") 
else:
    print("The number is greater than 34") 

#if the first case is met (our number is 22), then it never reaches thte other two cases after --> careful when designing if statements!!!
#cases structure should be typically exhaustive

#Nested if statements
a = random.randint(0,10)
b = random.randint(10,20)

if a < 9:
  print(f'a is less than 9.')
  if b <19:
    print(f'b is smaller than 19.')

#Equivalently, we can combine the logical conditions

if a < 9 and b < 19:
  print('a is less than 9 and b is less than 19.')