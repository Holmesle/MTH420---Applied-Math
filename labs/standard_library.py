# standard_library.py
"""Python Essentials: The Standard Library.
Leah Holmes
MTH420 - Methods and Models of Applied Mathematics
04/08/2022
"""


# Problem 1
def prob1(L):
    """Return the minimum, maximum, and average of the entries of L
    (in that order).
    """
    # raise NotImplementedError("Problem 1 Incomplete")
    return max(L), min(L), sum(L)/len(L)


L = [1, 2, 3, 4, 5, 6, 7]

print('Q1: ','max: ',prob1(L)[0],
      ', min: ',prob1(L)[1],
      ', avg: ', prob1(L)[2],
      ', for list: ', L)

# Problem 2
def prob2():
    """Determine which Python objects are mutable and which are immutable.
    Test numbers, strings, lists, tuples, and sets. Print your results.
    """
    obj1 = (1,2,3,4,5,6,7)
    obj2 = list(obj1)
    obj2[0] = 7
    # raise NotImplementedError("Problem 2 Incomplete")
    return obj1 == obj2

print('Q2: ', prob2(), '; the objects are not the same therefore obj2 is muttable')

# Problem 3
from calculator import sum, product
from math import sqrt
def hypot(a, b):
    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any functions other than sum(), product() and sqrt that are 
    imported from your 'calculator' module.
    Parameters:
        a: the length one of the sides of the triangle.
        b: the length the other non-hypotenuse side of the triangle.
    Returns:
        The length of the triangle's hypotenuse c = sqrt(b^2 + a^2)
    """
    # raise NotImplementedError("Problem 3 Incomplete")
    return sqrt(sum(product(a, a), product(b, b)))

print('Q3: the hypotenuse of a triangle with side 1 and 3 in length is %0.4f' %hypot(1,3))

# Problem 4

from itertools import chain,combinations,chain

def power_set(A):
    """Use itertools to compute the power set of A.

    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.

    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    set1 = set(A)
    i = len(A)
    list_of_sets = [set1]
    while i > 2:
        sub = combinations(A,i-1)
        print(type(sub))
        list_of_sets += sub
        i -= 1
    # raise NotImplementedError("Problem 4 Incomplete")
    list_of_sets += A + [0]
    return list_of_sets

print('Q4: ',power_set([1,2,'a']))

# Problem 5: Implement shut the box.
import box as bx
import numpy as np

# player = input('Enter number of players')
# timelimit = input('Enter time limit')

def shut_the_box(player, timelimit):
    """Play a single game of shut the box."""
    empty_board = list(range(1,10))
    dice1 = np.random.choice(list(range(1,7)))
    dice2 = np.random.choice(list(range(1,7)))
''' Instructions say to not complete'''
shut_the_box(2,10)
