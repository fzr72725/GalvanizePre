import numpy as np

def scalar_add(vector, scalar):
  '''
  write a function that will perform and return scalar addition on an array
  '''
  return [x+scalar for x in vector]

def scalar_mult(vector, scalar):
  '''
  write a function that will perform and return scalar addition on an array
  '''
  return [x*scalar for x in vector]

def range_use():
    '''
    Use the built-in python function range to create the following numpy arrays
    '''
    row_vector = np.array(range(1,7)).reshape(1,6)
    column_vector = np.array(range(11,15)).reshape(4,1)
    return row_vector, column_vector

def dot_product_no_numpy(arr1, arr2):
  '''
  write a function that will return the dot product of two same-length vectors
  WITHOUT using numpy
  '''
  return sum([x*y for x,y in zip(arr1,arr2)])

def dot_product_with_numpy(arr1, arr2):
  '''
  write a function that will return the dot of two same-length vectors using numpy

  '''
  return np.dot(np.array(arr1), np.array(arr2))

def mat_addition(A,B):
    '''
    Take in a A (an n x 1 list) and B (a 1 x m list)
    Use numpy to add A to B and return the result

    '''
    return np.array(A)+np.array(B)

def mat_inner_product(X,Y):
    '''
    Take in two matrices as numpy arrays, X and Y. Determine whether they have an inner product.
    If they do not, return False. If they do, return the resultant matrix as a numpy array.
    '''
    if X.shape[1]==Y.shape[0]:
        return np.dot(X, Y)
    return False

if __name__ == '__main__':
    #scalar_add(vector, scalar)
    #scalar_mult(vector, scalar)
    print range_use
