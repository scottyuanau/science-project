from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

fifa = pd.read_csv('data/fifa_data.csv')

# histogram of fifa players
left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]

labels = ['Left', 'Right']
plt.figure(figsize=[10,10],dpi=300)
plt.pie([left, right], labels=labels, autopct='%.2f %%')
plt.title('Foot Preference of FIFA Players')
plt.show()
