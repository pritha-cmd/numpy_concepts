#indexing slicing

import numpy as np

arr1= np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print ("Array:\n", arr1)

#getting the first row
print ("First row:\n", arr1[0])

#getting the first column
print ("First column:\n", arr1[:,0])
print ('\n')


#getting the first element of first row
print ("First element of first row:\n", arr1[0][0])
print ("First element of first row:\n", arr1[0,0])
print ('\n')

#get 7
print ("Element 7:\n", arr1[1,2])
print ('\n')

#get 7, 8 11, 12
print (arr1[1:,2:])
print ('\n')

#get 3,4,7,8
print (arr1[0:2,2:])
print ('\n')

#modify array element
arr1[0,0]=15
print (arr1)