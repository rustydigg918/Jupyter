"""
In python Lists are collection of datas surrounded by
bracketsand the elements are seperated by commas. Like this
List: [1,2,"a",3.14]

A List Comprehension is alsp surrounded by brackets but instead
of a lit of data inside, enter an expression followed by for loops
and if clauses. Like this:
List Comprehension: [expr for val in collection] or
                    [expr for val in collection if <test>]
we can also have more than one if clause:
                    [expr for val in collection if <test1> and <test2>]
we can also loop over more than one collection:
                    [expr for val1 in collection and val2 in collection2]

"""

# Let's see some examples:
"""
Create a List of squares of first 100 positive integers
"""
square=[]
for i in range(1,101):
    square.append(i**2)
    i+=1
print(square)

# Now try to get the results by list Comprehension
squares2 = [i**2 for i in range(1,101)]
print(squares2)
print; print

"""
Create a list of remainders when dividing first
squares by 5
"""
remainders5 = [i**2 % 8 for i in range(1,101)]
print(remainders5)

remainders11 = [i**2 % 11 for i in range(1,101)]
print(remainders11)

# Interesting Patten: if you divide a number by a prime number
# then the number of distinct remainders woud be (p+1)/2
# Have a look at it's expression:
# p_remainders = [x **2 for x in range(1,101)]
# len(p_remainders) = (p+1)/2


"""
Suppose we have a list of movies and we want to find a list of movies
that starts with the lettter 'G'
"""
movies = ["Star Wars", "Gandhi", "Casablanca", "Shawshank Redemption", "Toy Story",
          "Gone with the Wind", "Citizen Kane", "It's a wonderful Life",
          "The Wizard of oz", "Gattaca", "Rear Window", "Ghostbuster", "To Kill a Mokingbird",
          "Good will Hunting", "2001: A Space Odyssey", "Raider of the Lost Ark", "Groundhog Day",
          "Close Encounter of the Third Kind"]

# Without List Comprehension
startsG = []
for title in movies:
    if title.startswith("G"):
        startsG.append(title)
print(startsG)

# Try it with List Comprehension
Gmovies = [title for title in movies if title.startswith("G")]
print(Gmovies)


"""
Suppose of list of movies as a list of tuples containing both
the title of the movies and the year in which the movie Was
released.

Find out the list of the title of all the movies which was released
before the year 2000.
"""
movies = [("Citizen Kane", 1941), ("Sprited Away",2001),("It's a Wonderful Life", 1946), ("Gattaca",1997),
          ("No Country for old Men", 2007), ("Rear Window",1954),("The Lord of the Rings: The Fellowship of the ring", 2001),
          ("Groundhog Day", 1993), ("Close Encounters of the Third Kind", 1977), ("The Royal Tenenbaums",2001),("The Aviator",2004),
          ("Raiders of the Lost Ark", 1981)]

# Try to get the results by normal List
movies2k = []
for (title,year) in movies:
    if year <= 2000:
        movies2k.append(title)
print(movies2k)

# Apply List Comprehension here
pre2k = [title for (title,year) in movies if year <= 2000]
print(pre2k)
print;print

# Apply Scalar Multiplication on this vector
v = [2,-3,1]
"""
Multiply all the list elements
by 4
"""
print(v*4) # No it just concated the List
# LIKE the following
print(v+v+v+v)
# This was of no use to us, Let's see it through List Comprehension

mult4 = [i*4 for i in v]
print(mult4) # Got the results

# Use List Comprehension to compute the cartesian Product
A = [1,3,5,7]
B = [2,4,6,8]

cartesian_product = [(a,b) for a in A for b in B]
print(cartesian_product)

# use basic list method to perform the same
cart_prod = []
A = [1,3,5,7]
B = [2,4,6,8]
for i in A:
    for j in B:
        k =(i,j)
        cart_prod.append(k)
print(cart_prod)
