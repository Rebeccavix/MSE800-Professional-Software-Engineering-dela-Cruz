# Activity W4-2-3: - Create a Full project in Python - object oriented - File processing
# Note: You must have main function
# Write a full project to do the data file processing for csv, text, image and etc. file formats.
'''
Last activity for Week 4: Using union and symmetric difference and Math and circle Libs
Update the data format file to be added two more functionalities:
1- call Math function and get value from end user to calculate Sin and Cos
2- get diameter of a circle and calculate area of the circle.
3- Try to test the union and symmetric difference methods
'''

import pandas as pd
import os
import math


class DataFileFormatProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        """Load data from CSV, Parquet, or Text file"""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")

        if self.file_path.endswith('.csv'):
            self.data = pd.read_csv(self.file_path)
        elif self.file_path.endswith('.parquet'):
            self.data = pd.read_parquet(self.file_path)
        elif self.file_path.endswith('.txt'):
            self.data = pd.read_csv(
                self.file_path, delimiter="\t", header=None)
        else:
            raise ValueError(
                "Unsupported file format. Please use CSV, Parquet, or Text.")

        print(f"Data loaded successfully from {self.file_path}")

    def initial_processing(self):
        """Perform initial data analysis"""
        if self.data is None:
            raise ValueError("No data loaded.")

        print("Initial Data Summary:")
        print(self.data.info())
        print("\nMissing Values:")
        print(self.data.isnull().sum())
        print("\nDescriptive Statistics:")
        print(self.data.describe())

    def calculate_sin_cos(self):
        """Get user input and calculate sine and cosine values"""
        try:
            value = float(input("Enter a number to calculate Sin and Cos: "))
            print(f"Sin({value}) = {math.sin(value)}")
            print(f"Cos({value}) = {math.cos(value)}")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

    def calculate_circle_area(self):
        """Calculate the area of a circle given its diameter"""
        try:
            diameter = float(input("Enter the diameter of the circle: "))
            radius = diameter / 2
            area = math.pi * (radius ** 2)
            print(f"Area of the circle with diameter {diameter}: {area:.2f}")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

    def test_set_operations(self):
        """Perform union and symmetric difference operations on sample sets"""
        set1 = {1, 2, 3, 4, 5}
        set2 = {4, 5, 6, 7, 8}

        union_result = set1.union(set2)
        sym_diff_result = set1.symmetric_difference(set2)

        print("\nSet Operations:")
        print(f"Set 1: {set1}")
        print(f"Set 2: {set2}")
        print(f"Union: {union_result}")
        print(f"Symmetric Difference: {sym_diff_result}")


def main():
    """Main function to execute the program"""
    file_path = input("Enter file path: ")
    try:
        file_processor = DataFileFormatProcessor(file_path)
        file_processor.load_data()
        file_processor.initial_processing()

        # Additional functionalities
        file_processor.calculate_sin_cos()
        file_processor.calculate_circle_area()
        file_processor.test_set_operations()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
