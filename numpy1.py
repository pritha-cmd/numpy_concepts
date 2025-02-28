import numpy as np

#1d array
arr1= np.array([1,2,3,4,5])
print (arr1)
print (type(arr1))

print (arr1.shape)

#reshaping array
arr2= np.array([1,2,3,4,5])
print(arr2.reshape(1,5))

#2d array
arr2=np.array([[1,2,3,4,5]])
print (arr2.shape)

arr2=np.array([[1,2,3,4,5],[2,3,4,5,6]])
print (arr2)
print (arr2.shape)

#creating array with inbuilt function
#arange(start, stop, step)
print(np.arange(0,10,2))


#reshaping this
print(np.arange(0,10,2).reshape(5,1))
print ('\n')

#3 rows, 4 columns matrix , all entries =1 
print(np.ones((3,4)))
print ('\n')

#identity matrix
print(np.eye(3))



