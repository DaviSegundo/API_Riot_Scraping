import os
import pandas as pd

from path import Path

data_path = 'dados_lol\data'
path = Path(data_path)

arqs = []

for file in path.glob('*.csv'):
    arqs.append(os.path.join(data_path, file.name))

data = []

for file in arqs:
    df = pd.read_csv(file)
    data.append(df)

result = pd.concat(data, ignore_index=True)
result = result.drop(columns=["Unnamed: 0"])

result.to_csv('data.csv')