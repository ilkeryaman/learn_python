import matplotlib.pyplot as plt
import numpy as np

# for visualising in jupyter notebook, following codes are required
"""
%matplotlib inline
"""

x = np.arange(1, 6)
y = np.arange(2, 11, 2)

# Draw 1 Graphic
plt.plot(x, y, "red")
plt.show()

# Draw 4 Graphics
plt.subplot(2, 2, 1)  # For 2-2 matrix, works on 1st graphic
plt.plot(x, y, "blue")
plt.subplot(2, 2, 2)  # For 2-2 matrix, works on 2nd graphic
plt.plot(y, x, "yellow")
plt.subplot(2, 2, 3)  # For 2-2 matrix, works on 3rd graphic
plt.plot(x, y, "red")
plt.subplot(2, 2, 4)  # For 2-2 matrix, works on 4th graphic
plt.plot(x, x ** 2, "black")
plt.show()

# Draw Figures
fig = plt.figure()
axes = fig.add_axes([
    0.1,    # margin from left
    0.2,    # margin from bottom
    0.4,    # length at X axis
    0.6     # length at Y axis
])
plt.show()

# Adding multiple figure
fig = plt.figure()
axes = fig.add_axes([
    0.1,    # margin from left
    0.2,    # margin from bottom
    0.8,    # length at X axis
    0.7     # length at Y axis
])
axes2 = fig.add_axes([
    0.6,    # margin from left
    0.3,    # margin from bottom
    0.2,    # length at X axis
    0.2     # length at Y axis
])

axes.plot(y, x)
axes.set_xlabel("Outer X")
axes.set_ylabel("Outer Y")
axes.set_title("Outer Graph")

axes2.plot(y, x, "red")
axes2.set_xlabel("Inner X")
axes2.set_ylabel("Inner Y")
axes2.set_title("Inner Graph")

plt.show()
