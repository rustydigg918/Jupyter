"""
Not all data can be stored in a file often times data can
be used in a sequence to be used for

Python offers several ways to work and store oredered data.
> Lists are one of the common tools, but here is a smaller faster
alternative. and that is 'Tuple'
"""

# What is the difference b/w lists and tuple?

# List example
prime_numbers = [2,3,5,6,11,13,17]
# Tuple example
perfect_squares = (1,4,9,16,25,36)

### Other than notation there is very little difference between the two.

# Display Lengths
print("# Primes = ", len(prime_numbers))
print("# Squares = ", len(perfect_squares))

# Iterate over the sequences
for p in prime_numbers:
    print("Prime: ", p)
print(40* '<>')
for n in perfect_squares:
    print("Square ", n)

# Now let's look at the difference in these two
print("List methods")
print(dir(prime_numbers))
print(50*"#")
print("Tuple methods")
print(dir(perfect_squares))
print(80*'-')

import sys
print(dir(sys))
print(help(sys.getsizeof))
print(80*'_')

list_eg  = [1,2,31,"a","b","c","d",True,3.14159]
tuple_eg = (1,2,31,"a","b","c","d",True,3.14159)

print("List Size = ", sys.getsizeof(list_eg)) #72 bytes
print("Tuple Size =", sys.getsizeof(tuple_eg)) #64 bytes
# >>> So, the size varies here and when working with large dataset the size
# changes significantly.

"""
Lists                                           Tuples
>Add data                                   Can't be changed
>Remove data                                Immutable
>Change data                                Made quickly
"""

# Let's use a module called 'timeit' to see how long it takes
# to create 1 million lists and 1 millio tuples.

import timeit
list_test = timeit.timeit(stmt="[1,2,3,4,5]",
                          number=1000000)
tuple_test = timeit.timeit(stmt="(1,2,3,4,5)",
                           number=1000000)
print("List time: ", list_test)
print("Tuple time:", tuple_test)


# Let's make some tuples:
empty_tuple = ()
test1 = ("a")
test2 = ("a","b")
test3 = ("a", "b","c")

print(empty_tuple)
print(test1)
print(test2)
print(test3)

"""
output>
()
a       <----- what's this? it looks like a string, we need to add a comma(',')
('a', 'b')
('a', 'b', 'c')
"""
print(80*'-')
test1 = ("a",)
print(test1)

# Alternative Construction of Tuple
test1 = 1,
test2 = 1,2
test3 = 1,2,3

print(test1)
print(test2)
print(test3)

print(type(test1))
print(type(test2))
print(type(test3))

print(80*'*')
# Let's examine the Tuple with 1 Element
# >>> Reason for this is Tuple Assignment

#(age, country, knows_python)
survey = (27, "Vietnam", True)

age = survey[0]
country = survey[1]
knows_python = survey[2]

print("Age = ",age)
print("Country = ",country)
print("Knows Python?", knows_python)

print(82*'_')

survey2 = (21, "Switzerland", False)
age,country,knows_python =survey2
print("Age =",age)
print("Country =",country)
print("Knows Python?",knows_python)

print(81*'_')
print('without comma>>>> This will assign the string to the variable')
country = ("Australia")
print(country)

print(81*'_')
print('Now with comma>>>> By adding an extra comma in the end here we do want our variable to be tuples and dont want to unpack it into the variable')

country = ("Australia",)
print(country)


# Now, Make sure the number of variables matches the number of elements in the tuple
# Let's look at two examples.
print(81*'_')
#More values than variable
a, b, c = (1,2,3,4) # This will throw 'ValueError'
#More variables than values
x,y,z = (1,2) #Again, ValueError
print(81*'_')
