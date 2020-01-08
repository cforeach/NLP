import numpy as np
from matplotlib import pyplot as plt

'''
randn return the Gaussian Standard Normal Distrubution
'''
x = np.random.randn(50)
y = np.random.randn(50)

# plt.scatter(x, y)
# plt.show()

'''
self data
x_ax = [0,1]
y_ax = [0,1]
'''

x_ax = [0, 1, 1, 0]
y_ax = [0, 1, 0, 1]

plt.scatter(x_ax, y_ax)
plt.show()
