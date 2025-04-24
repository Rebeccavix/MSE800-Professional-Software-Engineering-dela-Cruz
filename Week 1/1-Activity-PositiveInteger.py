#1- Activity : Create a NumPy array of the first 10 positive integers. Then:
#   1. Print the array.
#   2. Print the shape and data type of the array.
#   3. Multiply each element by 2 and print the result.
 
import numpy as np

arr = np.arange(1,2,3,4,5,6,7,8,8,9,10)
# 1. Create a NumPy array of the first 10 positive integers
# 1. Print the array
print("array:")
print(arr)

# 2. Print the shape and data type of the array
print("\nShape of the array:", arr.shape)
print("Data type of the array:", arr.dtype)

# 3. Multiply each element by 2 and print the result
doubled_arr = arr * 2
print("\nArray after multiplying each element by 2:")
print(doubled_arr)

