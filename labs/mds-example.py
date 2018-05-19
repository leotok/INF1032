#!/usr/bin/env python
# coding: utf-8

import numpy as np
import scipy.spatial.distance
from sklearn.manifold import MDS
from scipy.spatial.distance import pdist, squareform

import matplotlib.pyplot as plt

np.random.seed(seed=668)

data = np.random.rand(1000, 100)

D = pdist(data, metric='euclidean')
D = squareform(D)

mds = MDS(n_components=2, dissimilarity='precomputed')
fit_t = mds.fit_transform(D)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_title('MDS of random data')
ax.set_xlabel('PC-1')
ax.set_ylabel('PC-2')
ax.scatter(x=fit_t[:, 0], y=fit_t[:, 1], c='r')
plt.show()
