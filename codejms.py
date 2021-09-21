import pandas as pd
import numpy as np
import matplotlib as mpt
df = pd.read_csv('donnees-hospitalieres-covid19-2021-09-20-19h05.csv', sep=";")
df["date"] = pd.to_datetime(df.jour)
df.drop(columns="jour", inplace=True)
df.set_index("date", inplace=True)
df1 = df[df.sexe==0].groupby ('date')['dc'].sum()
df1.plot()