import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import patches
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import *
import os

matplotlib.use('TkAgg')
print(matplotlib.get_backend())

# fig, ax = plt.subplots(figsize=(4, 4))
X = 5
fig, ax = plt.subplots(figsize=(8, 8))

ax.set_aspect('equal')
ax.add_patch(patches.Rectangle((0, 0), X, X, edgecolor='black', facecolor='black', fill=False))
plt.xlim([-1, X+1])
plt.ylim([-1, X+1])
# plt.grid(which='major', linestyle=':')
plt.show()
fig.savefig('static/calculate/img/square.png')




# fig = plt.figure(figsize=(2, 2))
# ax = fig.add_subplot()
# rect = Rectangle((0, 0), 1, 1)
# ax.add_patch(rect)
#
# plt.show()
# fig.savefig('static/calculate/img/square.png')
