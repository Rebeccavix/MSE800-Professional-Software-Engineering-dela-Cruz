# Activity W4-2-3: - Create a Full project in Python - object oriented - File processing
# Note: You must have main function
# Write a full project to do the data file processing for csv, text and etc. file formats.

import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt


class CSVFile:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        return pd.read_csv(self.file_path)


class ParquetFile:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        return pd.read_parquet(self.file_path)


class TextFile:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        return pd.read_csv(self.file_path, header=None)


class ImageFile:
    def show_image(self):
        (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
        print("training data shape:", x_train.shape,
              "training labels shape:", y_train.shape)

        plt.imshow(x_train[0])
        plt.show()


class File:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def read_file(self):
        file_type = self.file_path.split('.')[-1]
        if file_type == 'csv':
            self.data = CSVFile(self.file_path).read_file()
        elif file_type == 'parquet':
            self.data = ParquetFile(self.file_path).read_file()
        elif file_type == 'txt':
            self.data = TextFile(self.file_path).read_file()
        else:
            raise ValueError(f"Unsupported file type: {file_type}")

    def process_file(self):
        print(f"File type: {self.file_path.split('.')[-1]}\n")
        print(f"head {self.data.iloc[0]}\n")
        print(f"tail {self.data.iloc[-1]}\n")
        print(f"shape {self.data.shape}\n")
        print(f"columns {self.data.columns}\n")


def main():
    is_image = input("Do you want an image file? (y/n): ")
    if is_image.lower() == "y":
        file_processor = ImageFile()
        file_processor.show_image()
    else:
        file_path = input("Enter file path: ")
        file_processor = File(file_path)
        file_processor.read_file()
        file_processor.process_file()


if __name__ == "__main__":
    main()
