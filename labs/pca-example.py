#!/usr/bin/env python
# coding: utf-8

import numpy as np
from sklearn.decomposition import PCA

import matplotlib.pyplot as plt

np.random.seed(seed=668)

data = np.random.rand(1000, 100)
pca = PCA(n_components=2)
fit_t = pca.fit_transform(data)

fig = plt.figure()
#ax = fig.add_subplot(121)
#ax.set_title('Random data')
#ax.plot(np.arange(1, 1001), data)

ax = fig.add_subplot(111)
ax.set_title('PCA of random data')
ax.set_xlabel('PC-1')
ax.set_ylabel('PC-2')
ax.scatter(x=fit_t[:, 0], y=fit_t[:, 1], c='r')


plt.show()
