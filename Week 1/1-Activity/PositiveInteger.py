#1- Activity : Create a NumPy array of the first 10 positive integers. Then:
#Print the array.
#Print the shape and data type of the array.
#Multiply each element by 2 and print the result.
 
import numpy as np

# 1. Create a NumPy array of the first 10 positive integers
arr = np.arange(1, 11)
print("Original array:")
print(arr)

# 2. Print the shape and data type of the array
print("\nShape of the array:", arr.shape)
print("Data type of the array:", arr.dtype)

# 3. Multiply each element by 2 and print the result
doubled_arr = arr * 2
print("\nArray after multiplying each element by 2:")
print(doubled_arr)

