import pandas as pd


class DataFileFormat_Processor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        if self.file_path.endswith('.csv'):
            self.data = pd.read_csv(self.file_path)
        elif self.file_path.endswith('.parquet'):
            self.data = pd.read_parquet(self.file_path)
        elif file_type == 'txt':
            self.data = TextFile(self.file_path).read_file()
        else:
            raise ValueError(
                "Unsupported file format. Please use CSV, Parquet or Text.")
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

    # file_path = 'Activity-Week4/sample_junk_mail.csv'
    # processor = DataFileFormat_Processor(file_path)
    # processor.load_data()
    # processor.initial_processing()

    file_path = input("Enter file path: ")
    file_processor = DataFileFormat_Processor(file_path)
    file_processor.load_data()
    file_processor.initial_processing()

# def main():
#     is_image = input("Do you want an image file? (y/n): ")
#     if is_image.lower() == "y":
#         file_processor = ImageFile()
#         file_processor.show_image()
#     else:
#         file_path = input("Enter file path: ")
#         file_processor = File(file_path)
#         file_processor.read_file()
#         file_processor.process_file()


if __name__ == "__main__":
    main()
