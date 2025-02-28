#numpy vectorized operations

import numpy as np

arr1= np.array([1, 2, 3, 4, 5])
arr2= np.array([10, 20, 30, 40, 50])

#element wise addition
print ("Addition:",np.add(arr1, arr2))

#element wise subtraction
print ("Subtraction:",np.subtract(arr1, arr2))

#element wise multiplication
print ("Multiplication:",np.multiply(arr1, arr2))

#element wise division
print ("Division:",np.divide(arr1, arr2))


#universal functions
arr2= np.array([1,2,3,4,5])

#square root
print(np.sqrt(arr2))

#exponential
print(np.exp(arr2))

#sine
print(np.sin(arr2))

#natural log
print(np.log(arr2))

