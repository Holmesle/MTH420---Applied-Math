# python_intro.py
"""Python Essentials: Introduction to Python.
Leah Holmes
MTH420 - Methods and Models if Applied Mathematics
04/08/2022
"""


'''
1. Find the volume of a sphere with r = 10, where pi - 3.14159.
'''
def prob1():
    pi = 3.14159
    r = 10
    return (4*pi*r**3)/3

'''
2. save file as python_intro.py and add a header to the top, the print 
hello world.
'''
def prob2():
    print('Hello, world!')

'''
3. create a function taking r as an imput to calculate the volume of a 
   sphere.
'''

# already did the first two parts upon creating the file

def prob3e(r):
    pi = 3.14159
    return 4*pi*r**3



'''
4. preform a dot prodecto with np.dot or @ (I dont see 
   why you would use a function to make these arrays).
'''
import numpy as np
A = np.array([[3,-1,4],[1,5,-9]])
B = np.array([[2,6,-5,3],[5,8,9,7],[9,-3,2,-3]])

def prob4(A,B):
    return np.dot(A,B)

# really dont see why you would make a function of a function but ok
AB = prob4(A,B)

print(f'Q4: The dot product of A and B is \n {AB}.')

'''
5. Write a function that accepts income and returns the tax 
liability (from given table in problem statement).
'''

def prob5(income):
    if 40125 < income <85525:
        return income - income*0.1
    elif 9875 < income <40125:
        return income - income*0.12
    elif income < 9875:
        return income - income*0.22


'''
6. Write a function taking vectors A and B then returns A*B, A+B,
 and 5A, the first w/ lists and the second ndarrays.
'''

A = [1,2,3,4,5,6,7]
B = [5,5,5,5,5,5,5]

def prob6a(A,B):
    AB = []
    sum_AB = []
    A5 = []
    for i in range(len(A)):
        ab = A[i]*(B[i])
        sum_ab = A[i]+(B[i])
        a5 = 5*A[i]
        AB.append(ab)
        sum_AB.append(sum_ab)
        A5.append(a5)
    return AB, sum_AB, A5

def prob6b(A,B):
    A = np.array(A)
    B = np.array(B)
    return A*B, A+B, 5*A

print('Q6: A*B:')
print(prob6a(A,B)[0],prob6b(A,B)[0])
print('    A+B:')
print(prob6a(A,B)[1],prob6b(A,B)[1])
print('    5A:')
print(prob6a(A,B)[2],prob6b(A,B)[2])
    
