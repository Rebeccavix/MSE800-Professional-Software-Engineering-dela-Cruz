import pandas as pd

data_frame = pd.read_csv("Activity-Week4\sample_junk_mail.csv")
first_two_records = data_frame.head(2)
last_two_records = data_frame.tail(2)
all_records = data_frame.tail()
print(all_records.to_string())
print(first_two_records.to_string())
print(last_two_records.to_string())
