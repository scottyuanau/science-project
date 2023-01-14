from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

x = np.arange(0, 4.5, 0.5)

# Resize the graph
plt.figure(figsize=[5, 5], dpi=300)

plt.plot(x, x ** 2, label='x^2')
plt.plot(x, x ** 3, label='x^3')

# the label of X Axis & Y Axis
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# the tile of the graph
plt.title('The Sample Gragh', fontdict={
    'fontname': 'Comic Sans MS',
    'fontsize': 16
})

# show legend of the graph
plt.legend()

# show plot
plt.show()
