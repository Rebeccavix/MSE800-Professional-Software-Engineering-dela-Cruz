import numpy as np
'''
numbers = [1, 2, 3, 4, 5]
squares = {str(n): n**2 for n in numbers}
print(squares)
'''
# Output: {'1': 1, '2': 4, '3': 9, '4': 16, '5': 25}


# numbers = [1, 2, 3, 4, 5]
# even_squares = {n: n**2 for n in numbers if n % 2 == 0}
# print(even_squares)
# #Output: {2: 4, 4: 16}

# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# dictionary = {k: v for k, v in zip(keys, values)}
# print(dictionary)
# Output: {'a': 1, 'b': 2, 'c': 3}

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# dict3 = {'d': 5, 'e': 6}
# merged_dict1 = {**dict1, **dict2, **dict3}
# merged_dict2 = {**dict3, **dict1, **dict2}
# merged_dict3 = {**dict3, **dict2, **dict1}
# print(merged_dict1)
# print(merged_dict2)
# print(merged_dict3)
# #latest value will overwrite

# **Conditional Merging: Merge with a condition, e.g., only keys that are vowels
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'d': 4, 'e': 5, 'f': 6}
# merged_dict = {**{k: v for k, v in dict1.items() if k in 'aeiou'},
#                **{k: v for k, v in dict2.items() if k in 'aeiou'}}
# print(merged_dict)
# Output: {'a': 1, 'e': 5}

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'d': 4, 'e': 5, 'f': 6}
# merged_dict = {**{k: v for k, v in dict1.items() if k in 'aeic'},
#                **{k: v for k, v in dict2.items() if k in 'aeic'}}
# print(merged_dict)
# Output: {'a': 1, 'e': 5}

# **Underscore (_)
# a = 1+1
# print(a)

# **Ignoring Values
# x, _, y = (1, "ignored", 3)
# print(x, y)

# x, _, y = (1, "test", 3)
# print(x, y)
# Note: Anything you put on the string it will be ignored

# **Use enumerate() for more pythonic looping
# names = ["John", "Mike", "Sam", "Mark", "Ben"]
# for i in range(len(names)):
#     print(i, names[i])

names = ["John", "Mike", "Sam", "Mark", "Ben"]
# for i in range(len(names)):
#     print(i, names[i])
#     print("***")
# for i, name in enumerate(names):
#     print(i, name)
#     print("***")
# for i, name in enumerate(names, start=1):
#     print(i, name)
#     print("***")

# names = ['Alice', 'Bob', 'Cathy']
# ages = [25, 30, 35]
# paired = (zip(names, ages))
# print(paired)

# names = ['Alice', 'Bob', 'Cathy']
# ages = [25, 30, 35]
# paired = list(zip(names, ages))
# print(paired)

# names = ['Alice', 'Bob', 'Cathy']
# ages = [25, 30, 35]
# # Creates a list of tuples pairing names with ages
# paired = list(zip(names, ages))
# paired_dict = dict(paired)  # Converts the list of tuples into a dictionary
# print(paired_dict)

# ids = [1, 2, 3]
# names = ['Alice', 'Bob', 'Cathy', 'Mike']
# grades = ['A', 'B', 'A+', 'A']

# students = list(zip(ids, names, grades))
# students_dict = dict(students)
# # students = dict(zip(ids, names, grades))
# # student_dict = dict(students)
# print(students_dict)

# ids = [1, 2, 3]
# names = ['Alice', 'Bob', 'Cathy', 'Mike']
# grades = ['A', 'B', 'A+', 'A']

# # Creates a list of tuples
# students = list(zip(ids, names, grades))
# print(students)
# students_dict = {id: {grade, name}
#                  for id, name, grade in students}  # Converts to dictionary
# print(students_dict)

# names = ['Alice', 'Bob', 'Cathy', 'Mike']
# grades = ['A', 'B', 'A+', 'A']

# students_dict = {name: grade for name, grade in zip(names, grades)}  # Converts to dictionary

# print(students_dict)

# ***# extract information with age greater than 25 from the following list of dictionaries
# data = [{"name": "Alice", "age": 28}, {"name": "Bob", "age": 24}, {"name": "Charlie", "age": 30}]**
# data = [{"name": "Alice", "age": 28}, {
#     "name": "Bob", "age": 24}, {"name": "Charlie", "age": 30}]
# filtered_data = [person for person in data if person["age"] > 25]
# print(filtered_data)

# ***use list comprehension to flatten the matrix
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flattened = [num for row in matrix for num in row]
# print(flattened)

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flattened = [num for row in matrix for num in row]
# print(flattened)

# npmatrix = np.array(matrix)
# res = npmatrix.flatten()
# print(res)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)

npmatrix = np.array(matrix)
res = npmatrix.flatten()
print(res)

shape = npmatrix.shape  # shape of the matrix 3 x3
print(shape)

shape = npmatrix.reshape(-1)
print(shape)
