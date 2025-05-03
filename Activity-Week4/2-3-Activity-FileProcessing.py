import pandas as pd
import os


class DataFileFormatProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
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
        if self.data is None:
            raise ValueError("No data loaded.")

        print("Initial Data Summary:")
        print(self.data.info())
        print("\nMissing Values:")
        print(self.data.isnull().sum())
        print("\nDescriptive Statistics:")
        print(self.data.describe())


def main():
    file_path = input("Enter file path: ")
    try:
        file_processor = DataFileFormatProcessor(file_path)
        file_processor.load_data()
        file_processor.initial_processing()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
