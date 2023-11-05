import pandas as pd
df = pd.read_parquet('./data/fhvhv_tripdata_2020-03.parquet')
df.to_csv('./data/fhvhv_tripdata_2020-03.csv')

print('Converting Finish!')
