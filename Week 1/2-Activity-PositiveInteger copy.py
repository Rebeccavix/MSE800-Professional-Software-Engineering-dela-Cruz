#1- Activity : Create a NumPy array of the first 10 positive integers. Then:
#   1. Print the array.
#   2. Print the shape and data type of the array.
#   3. Multiply each element by 2 and print the result.
 
import numpy as np

# 1-Activity: Create a NumPy array of the first 10 positive integers
first_10_positive = np.arange(1, 11)

#   1. Print the array.
print("Array of first 10 positive integer:", first_10_positive)

#   2. Print the shape and data type of the array.
print("Shape of the array:", first_10_positive.shape)
print("Data type of the array:", first_10_positive.dtype)

#   3. Multiply each element by 2 and print the result.
doubled_arr = first_10_positive * 2
print("Array after multiplying each element by 2:", doubled_arr)