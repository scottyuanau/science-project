from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

gas = pd.read_csv('data/gas_prices.csv')

plt.figure(figsize=[10,8], dpi=300)

plt.title('Gas Prices Over Time (in USD)', fontdict={
    'fontweight': 'bold',
    'fontsize': 18,
})
# plt.plot(gas.Year, gas.USA, 'b.-', label='USA')
# plt.plot(gas.Year, gas.Canada, 'g.-',label='Canada')
# plt.plot(gas.Year, gas['South Korea'], 'r.-',label='South Korea')
# plt.plot(gas.Year, gas.Australia, 'y.-', label='Australia')

# loop method to include all countries
for country in gas:
    if country != 'Year':
        plt.plot(gas.Year, gas[country], marker='.', label=country)


# change the xticks to find every 3 years
plt.xticks(gas.Year[::3])
plt.legend()

plt.savefig('img/gas-analysis.png', dpi=300)