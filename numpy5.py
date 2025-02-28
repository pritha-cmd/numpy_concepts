#statistical concepts --- normalization
#mean is zero, std dev is 1

import numpy as np

data = np.array([1,2,3,4,5])

mean = np.mean(data)
std_dev = np.std(data)

normalized_data= (data - mean) / std_dev
print ("Normalized data:",normalized_data)

median = np.median(data)

variance = np.var(data)

print ("Mean:",mean)
print ("Standard Deviation:",std_dev)
print ("Median:",median)
print ("Variance:",variance)


#logical operations
new_data= np.array ([1,26,3,4,5,99,46])

print (new_data>5)
print (new_data[new_data>5])
print (new_data[(new_data<5) & (new_data>1)]) #and
print (new_data[(new_data<5) | (new_data>1)]) #or
print (new_data[(new_data<5) ^ (new_data>1)]) #xor