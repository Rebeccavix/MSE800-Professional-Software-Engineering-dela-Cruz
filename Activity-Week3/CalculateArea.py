# Function to calculate the area of a rectangle

import math

def calculate_area(length, width):
    # Ensure the dimensions are positive
    length = abs(length)
    width = abs(width)
    
    # Calculate the area
    area = length * width
    
    # Round the area to 2 decimal places
    rounded_area = round(area, 2)
    
    return rounded_area

# Input dimensions of the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate and display the area
area = calculate_area(length, width)
print(f"The rounded area of the rectangle is: {area}")

# Additional note: If you want the square of a side (hypothetical case)
# you can calculate it as follows:
square_of_length = round(length ** 2, 2)
print(f"The square of the length is approximately: {square_of_length}")

#   number_l, number_w = input("Input value (L & W): ").split()
#   number_l =int(number_l)
#   number_w = int(number_w)
#   def area (number_l, number_w):
#       Area_lan = number_l* number_w
#       return (Area_lan)
#   area(number_l,number_w)