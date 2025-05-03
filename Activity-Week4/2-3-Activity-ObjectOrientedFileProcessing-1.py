# Activity W4-2-3: - Create a Full project in Python - object oriented - File processing
# Note: You must have main function
# Write a full project to do the data file processing for csv, text and etc. file formats.

import pandas as pd


class DataProcessor:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None

    def read(self):
        if self.filepath.endswith('.parquet'):
            self.data = pd.read_parquet(self.filepath)
        elif self.filepath.endswith('.csv'):
            self.data = pd.read_csv(self.filepath)
        elif self.filepath.endswith('.txt'):
            self.data = pd.read_csv(self.filepath, header=None)
        else:
            raise ValueError("Unsupported file format")
        return self.data

    def show_head(self, rows=5):
        if self.data is not None:
            print(self.data.head(rows))
        else:
            print("No data loaded. Call read() first.")


# File paths
files = [
    "Activity-Week4/Sample_data_2.parquet",
    "Activity-Week4/sample_text.txt",
    "Activity-Week4/sample_junk_mail.csv"
]

# Read and show each file
for file in files:
    print(f"\nReading file: {file}")
    reader = DataProcessor(file)
    reader.read()
    reader.show_head(2)
