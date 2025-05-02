import pandas as pd

data_frame = pd.read_csv("sample_junk_mail.csv")
first_two_records = data_frame.head(2)
last_two_records = data_frame.tail(2)
print(first_two_records.to_string())
print(last_two_records.to_string())
