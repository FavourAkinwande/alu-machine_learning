#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility and generate random student grades
np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)  

# Plot the histogram
plt.hist(student_grades, bins=range(0, 101, 10), edgecolor='black')  

# Set x-axis and y-axis labels
plt.xlabel('Grades')
plt.ylabel('Number of Students')


plt.title('Project A')
#Display plot
plt.xlim(0,100)
plt.show()

