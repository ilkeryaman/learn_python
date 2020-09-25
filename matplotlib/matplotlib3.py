import matplotlib.pyplot as plt
import numpy as np

# for visualising in jupyter notebook, following codes are required
"""
%matplotlib inline
"""

x = np.arange(1, 6)
y = np.arange(2, 11, 2)

""" Beautifying Lines """
fig = plt.figure()
axes = fig.add_axes([0, 0, 1, 1])
axes.plot(x, x ** 2,
          color="red",               # setting line color
          linewidth=3,               # setting line thickness
          linestyle="-.",            # setting line style
          marker="o",                # setting marker (circle) to unions
          markersize=15,             # setting size of marker
          markerfacecolor="green",   # setting inner color of marker
          markeredgecolor="blue",    # setting edge color of marker
          markeredgewidth=5          # setting edge thickness
         )
plt.show()

fig = plt.figure()
axes = fig.add_axes([0, 0, 1, 1])
axes.plot(x, x**2, color="red", linewidth=2, marker="o", markersize=10, markerfacecolor="black",
          markeredgecolor="blue", markeredgewidth=3)
axes.set_xlim(0, 10)  # Makes X axis start from 0 to 10
axes.set_ylim(0, 40)  # Makes Y axis start from 0 to 40
plt.show()
