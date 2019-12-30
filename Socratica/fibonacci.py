"""
Fibonacci Series:

1,1,2,3,5,8,13...
"""
# Goal: Write a fuction to return
# nth term of Fibonacci series.


# def fibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         return fibonacci(n-1) + fibonacci(n-2)
#



# # Test for the first 10 terms

# for n in range(1, 11):
#     print(n, ":", fibonacci(n))
#

# Now try it for the first 100 terms


# for n in range(1, 100):
#     print(n, ":", fibonacci(n))


# It keeps loading .......

# Why is that? coz system has to keep doing the same work again and again,
# which takes time like ever.



# Memorization techenique is the way out:
#> 1. Implement explicitly
#> 2. Using built-in python tool


#1. Implementing explicitly


# fibonacci_cache = {}
#
# def fibonacci(n):
#     # if we have the value, then return it
#     if n in fibonacci_cache:
#         return fibonacci_cache[n]
#     # Compute the Nth term
#     if n == 1:
#         value = 1
#     elif n == 2:
#         value = 1
#     elif n > 2:
#         value = fibonacci(n-1) + fibonacci(n-2)
#
#     # Cache the value and return it
#     fibonacci_cache[n] = value
#     return value
#
# for n in range(1,1001):
#     print(n, ":", fibonacci(n))


#2. Using built-in python tool

from functools import lru_cache  #Least Recently used cache
@lru_cache(maxsize = 1000)
def fibonacci(n):
    # Check that the input is a positive integer
    if type(n) != int:
        raise TypeError("n must be positive integer")
    if n < 1:
        raise ValueError("n must be a positive integer")

    # Compute the nthe term
    if n ==1:
        return 1
    elif n ==2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1,1001):
    print(n, ":", fibonacci(n))

# print(fibonacci("one")) # Getting a nice error

#> Much better, a simple function with fast performance. But there are problems here.
