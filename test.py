import matplotlib
import matplotlib.pyplot as plt
from matplotlib import patches
import math as m

matplotlib.use('TkAgg')

fig, ax = plt.subplots(figsize=(8, 8))
# ax.set_aspect('equal')
X = 8
Y = 16
Z = 50
x = [0, Y, Y - (Y-X)/2, (Y-X)/2, 0]
y = [0, 0, Z, Z, 0 ]


plt.plot(x, y)
# plt.xlim([-(X * 0.1), X + m.sqrt(X**2 - Y**2) + (X + m.sqrt(X**2 - Y**2)) * 0.1])
# plt.ylim([-(X * 0.1), X + m.sqrt(X**2 - Y**2) + (X + m.sqrt(X**2 - Y**2)) * 0.1])

plt.show()

fig, ax = plt.subplots(figsize=(8, 8))
# ax.add_patch(patches.Rectangle((0, 0), self.x, self.x, edgecolor='black', facecolor='black', fill=True))
# plt.xlim([-(self.x * 0.3), self.x + self.x * 0.3])
# plt.ylim([-(self.x * 0.3), self.x + self.x * 0.3])
# plt.grid(linestyle='--')
# fig.savefig('static/calculate/img/square.png')

# fig.savefig('static/calculate/img/square.png')

