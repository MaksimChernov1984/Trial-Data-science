import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# генератор случайных значений
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
color = np.random.rand(N)
area = (30*np.random.rand(N))**2

# для 2d
fig, ax = plt.subplots()

# для 3d
# fig = plt.figure(figsize = (10, 6))
# ax = fig.add_subplot(111, projection='3d')

ax.set_facecolor('#000')
ax.scatter(x, y, s=area, c = color, alpha = 0.9, marker='*', cmap = 'viridis')


plt.show()