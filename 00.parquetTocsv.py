import pandas as pd
import glob
data_paths = glob.glob('./data/yellow*.parquet')

print(data_paths)

for path in data_paths:
    df = pd.read_parquet(path)
    file_name = path.split('/')[-1].split('.')[0]
    df.to_csv(f'./data/{file_name}.csv')

print('Converting Finish!')
