#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

This script generates a line graph where the y values are the cubed values of x.
The x values range from 0 to 10, and the y values are calculated as y = x^3.
The data is plotted as a solid red line, and the graph is labeled accordingly.

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
