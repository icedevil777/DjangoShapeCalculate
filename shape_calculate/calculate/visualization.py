import matplotlib
import matplotlib.pyplot as plt
from matplotlib import patches


matplotlib.use('TkAgg')
X = 4
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.add_patch(patches.Rectangle((0, 0), X, X, edgecolor='black', facecolor='black', fill=False))
plt.xlim([-1, X+1])
plt.ylim([-1, X+1])

# plt.show()
fig.savefig('static/calculate/img/square.png')


