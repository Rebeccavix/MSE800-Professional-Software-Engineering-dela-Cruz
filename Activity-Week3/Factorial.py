def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Examples
#print("0! =", factorial(0))
#print("1! =", factorial(1))
#print("2! =", factorial(2))
#print("3! =", factorial(3))
#print("4! =", factorial(4))

for i in range(5):  # Range starts from 0 and ends at 4
    print(f"{i}! =", factorial(i))
