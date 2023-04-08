import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Los Angeles", "San Francisco", "New York"])
y = np.array([3.8, 0.8, 8.4])

plt.bar(x,y)

plt.title ("Population")

plt.savefig('population_barchart.png')
