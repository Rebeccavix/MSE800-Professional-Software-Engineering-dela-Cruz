# Activity W4-2-2: Parquet database
# See attached file, how many records are available? Sample_data_2.parquet

import pandas as pd

df = pd.read_parquet('Activity-Week4\Sample_data_2.parquet')
print(f"Number of records: {df.shape[0]}")
