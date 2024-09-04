i#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Define the x-axis values (Time in years)
x = np.arange(0, 21000, 1000)

r = np.log(0.5)
t1 = 5730
t2 = 1600

# Calculate y1 and y2 as the fraction remaining of each element over time
y1 = np.exp((r / t1) * x)  # C-14 decay
y2 = np.exp((r / t2) * x)  # Ra-226 decay

# Plot the line graphs
plt.plot(x, y1, 'r--', label='C-14')  # Dashed red line for C-14
plt.plot(x, y2, 'g-', label='Ra-226')  # Solid green line for Ra-226

# x and y axis limits
plt.xlim(0, 20000)
plt.ylim(0, 1)

#Labels and title
plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')
plt.title('Exponential Decay of Radioactive Elements')

# Add legend to the upper right corner
plt.legend(loc='upper right')

# Display the plot
plt.show()
