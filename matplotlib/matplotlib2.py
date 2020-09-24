import matplotlib.pyplot as plt
import numpy as np

# for visualising in jupyter notebook, following codes are required
"""
%matplotlib inline
"""

x = np.arange(1, 6)
y = np.arange(2, 11, 2)

""" Draw Multiple Axes In Figures """
flg, axes = plt.subplots(nrows=2, ncols=2)  # Creates 4 figures at the same time
plt.show()

flg, axes = plt.subplots(nrows=2, ncols=2)  # Creates 4 figures at the same time
plt.tight_layout()  # To put spaces between sub plots
plt.show()

flg, axes = plt.subplots(nrows=2, ncols=1)  # Creates 4 figures at the same time
print(axes)  # Attention! Axes is an array with 4 elements

""" Drawing x, y Graphic for All Axes """
flg, axes = plt.subplots(nrows=2, ncols=1)  # Creates 4 figures at the same time

for ax in axes:
    ax.plot(x, y)

plt.tight_layout()  # To put spaces between sub plots
plt.show()

""" Drawing Axes with Different Functions """
flg, axes = plt.subplots(nrows=2, ncols=1)  # Creates 4 figures at the same time

axes[0].plot(x, y)
axes[0].set_title("x / y")

axes[1].plot(x ** 3, y, "red")
axes[1].set_title("x3 / y")

plt.tight_layout()  # To put spaces between sub plots
plt.show()

""" Setting Figure Size """
fig = plt.figure(figsize=(10, 3)) # Set figure size
axes = fig.add_axes([0, 0, 1, 1])
axes.plot(x, y, color="green")
plt.show()

""" Another Example by Setting Title """
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8, 6))
axes[0].plot(x, y, color = "red")
axes[0].set_title("First Axes")

axes[1].plot(x, x ** 0.5, color="orange")
axes[1].set_title("Second Axes")
plt.tight_layout()  # To put spaces between sub plots
plt.show()

""" Saving Figure to A File """
fig.savefig("data/Figure1.png")  # Saves figure to Figure1.png
fig.savefig("data/Figure1.pdf")  # Saves figure to Figure1.pdf

""" Drawing Multiple Lines in an Axes """
fig = plt.figure(figsize=(6, 4))
axes = fig.add_axes([0.0, 0.0, 1, 1])
axes.plot(x, x ** 0.5, color="red", label="square root")
axes.plot(x, x ** 2, color="blue", label="square")
axes.plot(x, x ** 3, color="#c7ab00", label="cube")     # using hexadecimal color code
axes.legend()                                           # To show mapping between lines and labels
plt.show()
