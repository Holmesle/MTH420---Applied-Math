# python_intro.py
"""Python Essentials: Introduction to Python.
Leah Holmes
MTH420 Applied Mathematics
05/05/2022
"""

#Problem 1
def isolate(a, b, c, d, e):
    raise NotImplementedError("Problem 1 Incomplete")
    print(str(a)+'     '+str(b)+'     '+str(c)+' '+str(d)+' '+str(e))

# print('Q1: ')
# isolate(1, 2, 3, 4, 5)

#Problem 2
def first_half(string):
    N = len(string)
    n = N//2
    # print(string[:n+1])
    # raise NotImplementedError("Problem 2 Incomplete")

# print('\nQ2: ')
# first_half('This is a string')

def backward(first_string):
    backward = first_string[::-1]
    # raise NotImplementedError("Problem 2 Incomplete")
    print(backward)

# backward('This is another string')

#Problem 3
def list_ops():
    # create list of animals
    list_animals = ['bear','ant','cat','dog']
    # add eagle to the list
    list_animals.append('eagle')
    # change index 2 to fox
    list_animals[2] = 'fox'
    # pop index 1
    list_animals.pop(1)
    # reverse alphabetical order
    list_animals.sort(reverse=True)
    i = list_animals.index('eagle')
    list_animals[i] = "hawk"
    list_animals = list_animals + ["hunter"]
    # raise NotImplementedError("Problem 3 Incomplete")
    return list_animals

# print('\nQ3: ')
# print(list_ops())

#Problem 4
def alt_harmonic(n):
    n= int(n)
    """Return the partial sum of the first n terms of the alternating
    harmonic series. Use this function to approximate ln(2).
    """
    # raise NotImplementedError("Problem 4 Incomplete")
    terms = [(-1)**(i+1)/i for i in range(1,n+1)]
    return sum(terms)

# print('\nQ4: ')
# print(alt_harmonic(5e6))
import numpy as np

def prob5(A):
    """Make a copy of 'A' and set all negative entries of the copy to 0.
    Return the copy.
    Example:
        >>> A = np.array([-3,-1,3])
        >>> prob4(A)
        array([0, 0, 3])
    """
    # raise NotImplementedError("Problem 5 Incomplete")
    B = A.copy()
    mask = A < 0
    B[mask] =0
    return B

# print('\nQ5: ')
# print(prob5(np.random.randint(low = -10,high = 10,size = (5,5))))


def prob6():
    """Define the matrices A, B, and C as arrays. Return the block matrix
                                | 0 A^T I |
                                | A  0  0 |,
                                | B  0  C |
    where I is the 3x3 identity matrix and each 0 is a matrix of all zeros
    of the appropriate size.
    """
    A = np.array([[0,2,4],[1,3,5]])
    B = np.triu(np.ones([3,3])*3)
    C = np.diag([-2,-2,-2])
    z1 = np.zeros([3,3])
    z2 = np.zeros([2,3])
    z3 = np.zeros([3,2])
    z4 = np.zeros([2,2])
    I = np.diag([1,1,1])
    c1 = np.hstack((z1,A.T,I))
    c2 = np.hstack((A,z2,z4))
    c3 = np.hstack((B,z3,C))
    D = np.vstack((c1,c2,c3))
    # raise NotImplementedError("Problem 6 Incomplete")
    return D

# print('\nQ6: ')
# print(prob6())

def prob7(A):
    """Divide each row of 'A' by the row sum and return the resulting array.

    Example:
        >>> A = np.array([[1,1,0],[0,1,0],[1,1,1]])
        >>> prob6(A)
        array([[ 0.5       ,  0.5       ,  0.        ],
               [ 0.        ,  1.        ,  0.        ],
               [ 0.33333333,  0.33333333,  0.33333333]])
    """
    raise NotImplementedError("Problem 7 Incomplete")


def prob8():
    """Given the array stored in grid.npy, return the greatest product of four
    adjacent numbers in the same direction (up, down, left, right, or
    diagonally) in the grid.
    """
    #grid = np.load("grid.npy") did not work, below grid was shared by Tom
    grid = np.asarray([8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8, 49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0, 81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65, 52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91, 22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80, 24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50, 32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70, 67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21, 24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72, 21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95, 78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92, 16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57, 86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58, 19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40, 4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66, 88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69, 4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36, 20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16, 20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54, 1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48,]).reshape((20,20))
    max_prod = np.max(grid[:-3,:-3]*grid[1:-2,1:-2]*grid[2:-1,2:-1]*grid[3:,3:])
    return max_prod
    # raise NotImplementedError("Problem 8 Incomplete")

print('\nQ8: ')
print(prob8())
