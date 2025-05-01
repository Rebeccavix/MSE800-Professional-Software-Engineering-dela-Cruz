def area(number_l, number_w):
    Area_lan = number_l * number_w
    return (Area_lan)


number_l, number_w = input("Input value (L & W): ").split()
number_l = float(number_l)  # this should be float instead of int
number_w = float(number_w)  # this should be float instead of int
area = area(number_l, number_w)
print(f"The rounded area of the rectangle is: {area}")
