#!/usr/bin/env python
# coding: utf-8

import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = np.matrix('3 1 2; 6 1 2; 2 2 2; 0 2 2; 1 1 2; 8 1 2; 4 1 2')

fig = plt.figure()
ax = fig.add_subplot(121, projection='3d')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.scatter(xs=data[:, 0], ys=data[:, 1], zs=data[:, 2], color='red')

ax = fig.add_subplot(122)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.scatter(x=np.array(data[:, 0].T), y=np.array(data[:, 1].T), color='red')
plt.show()
