#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# Generate the x-axis values: time in years, from 0 to 28650, with a step size of 5730 (C-14 half-life)
x = np.arange(0, 28651, 5730)

# Calculate the natural logarithm of 0.5, which is the decay rate for each half-life
r = np.log(0.5)

# Define the half-life of C-14 in years
t = 5730

# Calculate the y-axis values: the fraction of C-14 remaining after 'x' years
# Using the formula y = exp((r / t) * x) to model exponential decay
y = np.exp((r / t) * x)

# Create a figure with specified dimensions (10 inches wide by 6 inches tall)
plt.figure(figsize=(10, 6))

# Plot the x (time) and y (fraction remaining) values as a line graph
plt.plot(x, y)

# Label the x-axis as 'Time (years)'
plt.xlabel('Time (years)')

# Label the y-axis as 'Fraction Remaining'
plt.ylabel('Fraction Remaining')

# Add a title to the graph indicating that it is modeling the exponential decay of C-14
plt.title('Exponential Decay of C-14')

# Set the y-axis to a logarithmic scale to better display the exponential decay
plt.yscale('log')

# Set the limits of the x-axis to range from 0 to 28650 years
plt.xlim(0, 28650)

# Displayng the graph
plt.show()

