import pandas as pd

df = pd.read_csv('TV_show_data (2).csv')

counter = 0
for col in df.columns:
    if df[col].apply(lambda x: isinstance(x, str)).any():
        counter += 1

print(counter)
