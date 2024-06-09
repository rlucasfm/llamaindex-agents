import pandas as pd
import os

champions_path = os.path.join('data', 'champions.csv')
champions_df = pd.read_csv(champions_path)

champions_df = champions_df.sort_values(by=['Base Health'], ascending=False)

print(champions_df)