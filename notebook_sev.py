import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("./donnees-hospitalieres-covid19-2021-09-20-19h05.csv",sep=";")

data['date'] = pd.to_datetime(data['jour'])
data= data.set_index('date')
data.drop(['jour','rad','hosp','rea'],axis=1)
d=data.pivot_table(index='dep', columns='sexe', values='dc')

d['per_cent_h']= round(d[1] * 100/ d[0],1)
d=d.sort_values('per_cent_h')

fig, ax = plt.subplots(figsize=(14,10))

sns.barplot(
    y=d.index,
    x='per_cent_h', 
    
    data=d,
    ax=ax
);