from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

fifa = pd.read_csv('data/fifa_data.csv')


# histogram of fifa players
bins = np.arange(40, 100, 10)  # defines the bins of the histogram, [0, 10, 20,...,100]
plt.hist(fifa.Overall, bins=bins, color='#FF5354', rwidth=0.9)
plt.xticks(bins)
plt.ylabel('Number of Players')
plt.xlabel('Skill Level')
plt.title('Distribution of Player Skills in FIFA 2018')
plt.show()
print(bins)