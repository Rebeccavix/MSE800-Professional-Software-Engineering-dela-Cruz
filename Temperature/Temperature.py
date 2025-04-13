import numpy as np

# Temperatures for a week in Celsius
temperatures = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])

# Calculate average temperature
average_temp = np.mean(temperatures)
print(f"Average temperature for the week: {average_temp:.2f}�C")

# Find the highest and lowest temperatures recorded
max_temp = np.max(temperatures)
min_temp = np.min(temperatures)
print(f"Highest temperature: {max_temp}�C")
print(f"Lowest temperature: {min_temp}�C")

# Convert temperatures to Fahrenheit
temperatures_fahrenheit = temperatures * 9/5 + 32
print("Temperatures in Fahrenheit:", temperatures_fahrenheit)

# Identify the days where the temperature was above 20�C
days_above_20 = np.where(temperatures > 20)[0]
print("Days with temperatures above 20�C (0=Mon, 6=Sun):", days_above_20)
