#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Define y as cubed values of the range from 0 to 10
y = np.arange(0, 11) ** 3

# Plotting y with a solid red line
plt.plot(np.arange(0, 11), y, 'r-')

# Set x-axis limits
plt.xlim(0, 10)

# Displaying the plot
plt.show()

