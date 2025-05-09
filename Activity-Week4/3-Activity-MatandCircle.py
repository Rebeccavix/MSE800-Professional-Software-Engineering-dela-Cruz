'''
Last activity for Week 4: Using union and symmetric difference and Math and circle Libs
Update the data format file to be added two more functionalities:
1- call Math function and get value from end user to calculate Sin and Cos
2- get diameter of a circle and calculate area of the circle.
3- Try to test the union and symmetric difference methods
'''
'''
Activity W4-2-3: - Create a Full project in Python - object oriented - File processing
Note: You must have main function
Write a full project to do the data file processing for csv, text, image and etc. file formats.

Last activity for Week 4: Using union and symmetric difference and Math and circle Libs
Update the data format file to be added two more functionalities:
1- call Math function and get value from end user to calculate Sin and Cos
2- get diameter of a circle and calculate area of the circle.
3- Try to test the union and symmetric difference methods
'''
import tensorflow as tf
import pandas as pd
import math
import matplotlib.pyplot as plt


class DataFileFormat_Processor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        file_path = self.file_path
        if file_path.endswith('.csv'):
            self.data = pd.read_csv(file_path)
        elif file_path.endswith('.txt'):
            self.data = pd.read_table(file_path, header=None)
        elif file_path.endswith('.parquet'):
            self.data = pd.read_parquet(file_path)
        elif 'cifar10' in self.file_path:
            self.data = tf.keras.datasets.cifar10.load_data()
        else:
            raise ValueError(
                "Unsupported file format. Please use CSV or Parquet.")
        print(f"Data loaded successfully from {self.file_path}")

    def initial_processing(self):
        if self.data is None:
            raise ValueError("No data loaded.")

        if 'cifar10' in self.file_path:
            (x_train, y_train), (x_test, y_test) = self.data
            print(x_train.shape)
            print(y_train.shape)
            print(x_test.shape)
            print(y_test.shape)
        else:
            print("Initial Data Summary:")
            print(self.data.info())
            print("\nMissing Values:")
            print(self.data.isnull().sum())
            print("\nDescriptive Statistics:")
            print(self.data.describe())

    def process_data(self):
        if 'cifar10' in self.file_path:
            (x_train, y_train), (x_test, y_test) = self.data
            # show the first n_rows * n_cols images of train dataset
            n_rows = 4
            n_cols = 8
            plt.figure(figsize=(n_cols * 2, n_rows * 2))
            for row in range(n_rows):  # loop row
                for col in range(n_cols):  # loop column
                    index = n_cols * row + col
                    # to generate n_rows and n_cols images, this is the (index + 1)th image
                    plt.subplot(n_rows, n_cols, index + 1)
                    plt.imshow(x_train[index], cmap="binary",
                               interpolation="nearest")
                    plt.axis('off')

            plt.subplots_adjust(wspace=0.2, hspace=0.5)  # to adjust layout
            plt.show()
        else:
            print(self.data)

    def calc_sin_cos_from_input(self):
        # 1- call Math function and get value from end user to calculate Sin and Cos
        n = float(input('Enter a number to calculate its sine and cosine: '))
        print(f'The sine of [ {n} ] is {math.sin(n)}')
        print(f'The cosine of [ {n} ] is {math.cos(n)}')

    def calc_circle_diameter_area(self):
        # 2- get diameter of a circle and calculate area of the circle with given radius
        radius = float(
            input('Enter a radius to calculate the diameter and area of the circle: '))
        diameter = 2 * radius
        area = math.pi * radius ** 2
        print(
            f'Given radius [ {radius} ], the diameter is: [ {diameter} ] and the area of the circle is [ {area} ]')

    def calc_union(self, set_a, set_b):
        # 3- Try to test the union and symmetric difference methods
        set_c = set_a.union(set_b)
        print(f'The union between {set_a} and {set_b} is: [{set_c}]')
        return set_c

    def calc_symmetric_difference(self, set_a, set_b):
        # 3- Try to test the union and symmetric difference methods
        set_c = set_a.symmetric_difference(set_b)
        print(
            f'The symmetric difference between {set_a} and {set_b} is: [{set_c}]')
        return set_c


def main():

    # file_path = 'src/Activity-Week4/sample_junk_mail.csv'
    file_path = 'Activity-Week4/sample_text.txt'
    # file_path = 'src/Week4/Sample_data_2.parquet'
    # file_path = 'cifar10'
    processor = DataFileFormat_Processor(file_path)
    processor.load_data()
    processor.initial_processing()
    processor.process_data()

    processor.calc_sin_cos_from_input()
    processor.calc_circle_diameter_area()

    set_a = set([2, 3, 4])
    set_b = set([3, 4, 5])
    processor.calc_union(set_a, set_b)
    processor.calc_symmetric_difference(set_a, set_b)


if __name__ == "__main__":
    main()
