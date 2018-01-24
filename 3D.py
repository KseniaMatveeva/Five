#Гиперболический цилиндр
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')


u = np.arange(-1, 1, 0.1)
v = np.arange(-1, 1, 0.1)
X = 2*(-np.cosh(u))
Y = 5*(-np.sinh(u))
Z = v
X, Y = np.meshgrid(X, Y)
surf = ax.plot_wireframe(X, Y, Z)

u1 = np.arange(-1, 1, 0.1)
v1 = np.arange(-1, 1, 0.1)
X1 = 2*np.cosh(u1)
Y1 = 5*np.sinh(u1)
Z1 = v1
X1, Y1 = np.meshgrid(X1, Y1)
surf = ax.plot_wireframe(X1, Y1, Z1)


plt.show()