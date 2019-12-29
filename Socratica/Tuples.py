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
