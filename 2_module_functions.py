import numpy as np
import math

# 1 dimensional array
arr1 = np.array([1, 2, 3])
print("This is a 1 Dimensional array: \n",arr1)
 
# 2 dimensional array
arr2 = np.array([[1, 2, 3],
                [4, 5, 6]])
print("This is a 2 dimensional array: \n", arr2)
 
# Creating an array from tuple
arr3 = np.array((1, 3, 2))
print("\nArray created using a passed tuple:\n", arr3)

print(math.sqrt(36))
print(math.e)
print(math.factorial(3))
print(math.gcd(9, 72, 54))