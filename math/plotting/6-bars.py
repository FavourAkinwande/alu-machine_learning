#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(5)

fruit = np.random.randint(0, 20, (4, 3))


people = ['Farrah', 'Fred', 'Felicia']

colors = ['red', 'yellow', '#ff8000', '#ffe5b4']  

bar_width = 0.5


plt.bar(people, fruit[0], color=colors[0], width=bar_width, label='Apples')
plt.bar(people, fruit[1], bottom=fruit[0], color=colors[1], width=bar_width, label='Bananas')
plt.bar(people, fruit[2], bottom=fruit[0] + fruit[1], color=colors[2], width=bar_width, label='Oranges')
plt.bar(people, fruit[3], bottom=fruit[0] + fruit[1] + fruit[2], color=colors[3], width=bar_width, label='Peaches')

# labels, title, and legend
plt.ylabel('Quantity of Fruit')
plt.title('Number of Fruit per Person')
plt.legend()

# y-axis range and ticks
plt.ylim(0, 80)
plt.yticks(np.arange(0, 81, 10))

# Displaying the plot
plt.show()

