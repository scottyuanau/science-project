from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

x = [0, 3, 4, 7, 8, 9]
y = [1, 5, 10, 24, 36, 66]
plt.plot(x, y)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('The first graph', fontdict={
    'fontname': 'Comic Sans MS',
    'fontsize': 16
})
plt.show()
