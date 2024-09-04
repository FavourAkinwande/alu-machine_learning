#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

'''
This script generates 2000 random height and weight values with a seed of 5 given a mean and covariance matrix.
The values are then transposed before plotting them on a scatter graph.'''



# The Given data
mean = [69, 0]  # Mean for height (69 inches) and weight offset
cov = [[15, 8], [8, 15]]  # Covariance matrix
np.random.seed(5)  # Seed for reproducibility

#Transpose the random values
x, y = np.random.multivariate_normal(mean, cov, 2000).T

# Adjust weight to start from 180 lbs

y += 180

# Plotting the scatter plot with magenta points
plt.scatter(x, y, color='magenta')

# Labels and title
plt.xlabel("Height (in)")
plt.ylabel("Weight (lbs)")
plt.title("Men's Height vs Weight")

# Displaying the plot
plt.show()

