from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('data/seattle-weather.csv')

temp_max = df['temp_max']
temp_min = df['temp_min']
dates = df['date']
wind = df['wind']

plt.figure(figsize=[10, 10])
plt.plot(dates, temp_max, label='Max Temp', linestyle=':')
plt.plot(dates, temp_min, label='Min Temp', linestyle=':')
plt.xlabel('Dates')
plt.ylabel('Temperature')
plt.title('Historical Temperature')
plt.xticks(['2012-01-01', '2013-01-01', '2014-01-01', '2015-01-01', '2015-12-31'])
plt.legend()

plt.show()
print(df)
