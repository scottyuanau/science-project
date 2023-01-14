from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

fifa = pd.read_csv('data/fifa_data.csv')

barcelona = fifa.loc[fifa.Club == 'FC Barcelona']['Overall']
madrid = fifa.loc[fifa.Club == 'Real Madrid']['Overall']
revs = fifa.loc[fifa.Club == 'New England Revolution']['Overall']
labels = ['FC Barcelona', 'Real Madrid', 'New England Revolution']

plt.figure(figsize=(6, 10), dpi=150)
plt.title('Professional Soccer Team Comparison')
plt.ylabel('FIFA Overall Rating')
boxes = plt.boxplot([barcelona, madrid, revs], labels=labels, patch_artist=True, medianprops={'linewidth': 2,'color':'red'})
for box in boxes['boxes']:
    # set edge color
    box.set(color='#4286f4', linewidth=2)
    # set fill color
    box.set(facecolor='#e0e0e0')

plt.show()
