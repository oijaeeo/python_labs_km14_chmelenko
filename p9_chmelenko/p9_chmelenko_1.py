import numpy as np
import itertools

def random_matrix(dim):
    """    The function generates dim x dim array of integers
    between 0 and 10.   """
    matrix = np.random.randint(10, size = (dim, dim))
    return matrix

def summ(massive):
    """    The function returns the sum of the elements of the array  """
    summ = 0
    for i in massive:
        summ += i
    return summ

def contexture(massive):
    """     The function returns contexture from the list    """
    massive_n = []
    for v in massive:
        cont = 1
        for w in v:
            cont *= w
        massive_n.append(cont)
    return massive_n

dim = ''
while not dim.isnumeric():
    dim = input("Enter the size of the matrix: ")
matrix = random_matrix(int(dim))
print("Matrix:")
print(matrix)
print('-' * 50)
print("Result:", np.linalg.det(matrix))
    

