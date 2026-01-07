import pandas as pd


df = pd.read_csv('/kaggle/working/cleaned_mixeddata.csv')

df_small = df.sample(10000, random_state=42)

df_small.to_csv('cleaned_mixeddata_small.csv', index=False)

print(df_small.shape)
print(df_small.head())