#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Define x values (range from 0 to 10)
x = np.arange(0, 11)

# y is the cubed values of x
y = x ** 3

# Plot y axis as a solid red line with x values
plt.plot(x, y, color='red', linestyle='-')

#Set x-axis ranage limits

plt.xlim(0, 10)

# Displaying the plot
plt.show()
