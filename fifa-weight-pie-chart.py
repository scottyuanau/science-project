from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

fifa = pd.read_csv('data/fifa_data.csv')

fifa.Weight = [int(x.strip('lbs')) if type(x) == str else x for x in fifa.Weight]
light = fifa.loc[fifa['Weight'] < 135].count()[0]
light_medium = fifa.loc[(fifa['Weight'] >= 135) & (fifa['Weight'] < 150)].count()[0]
medium = fifa.loc[(fifa['Weight'] >= 150) & (fifa['Weight'] < 175)].count()[0]
medium_heavy = fifa.loc[(fifa['Weight'] >= 175)].count()[0]


weights = [light, light_medium, medium, medium_heavy]
labels = ['Under 135', '135-150', '150-175', 'Over 175']
explode = (0, 0.2, 0, 0)

plt.figure(figsize=(10, 10), dpi=300)
plt.title('Weight Distribution of FIFA Players (in lbs)')
plt.pie(weights, labels=labels, autopct='%.2f %%', pctdistance=0.8, explode=explode, startangle=45)
plt.show()
