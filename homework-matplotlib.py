import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


# Figure 1
x = [1, 5, 10, 15, 20]
y1 = [1, 7, 3, 5, 11]
y2 = [4, 3, 1, 8, 12]

plt.figure()

plt.plot(x, y1, 'o-r', label='line 1')
plt.plot(x, y2, 'o-.g', label='line 2')
plt.legend()


# Figure 2
x = [1, 2, 3, 4, 5]
y1 = [1, 7, 6, 3, 5]
y2 = [9, 4, 2, 4, 9]
y3 = [-7, -4, 2, -4, -7]

fig = plt.figure()
grid = plt.GridSpec(2, 2)

ax1 = fig.add_subplot(grid[0, :])
ax2 = fig.add_subplot(grid[1, 0])
ax3 = fig.add_subplot(grid[1, 1])

ax1.plot(x, y1)
ax2.plot(x, y2)
ax3.plot(x, y3)


# Figure 3
plt.figure()
x = list(range(-5, 6))
y = [i ** 2 for i in x]
plt.annotate('min', xy=(0, 0), xycoords='data', xytext=(0, 10),
             textcoords='data', arrowprops=dict(facecolor='g'))
plt.plot(x, y)


# Figure 4
plt.figure()
np.random.seed(123)
vals = np.random.randint(11, size=(7, 7))
plt.pcolor(vals)
plt.colorbar()


# Figure 5
plt.figure()
x = np.arange(0.0, 5, 0.01)
y = np.cos(x * np.pi)

plt.plot(x, y, color="r")
plt.fill_between(x, y)


# Figure 6
plt.figure()
x = np.arange(0.0, 5, 0.01)
y = np.cos(x * np.pi)
y_masked = np.ma.masked_where(y < -0.5, y)
plt.ylim(-1, 1)
plt.plot(x, y_masked, linewidth=3)


# Figure 7
x = np.arange(0, 7)
y = x
where_set = ['pre', 'post', 'mid']
fig, axs = plt.subplots(1, 3, figsize=(15, 4))
for i, ax in enumerate(axs):
  ax.step(x, y, "g-o", where=where_set[i])
  ax.grid()


# Figure 8
x = np.arange(0, 11, 1)
y1 = np.array([(-0.2)*i**2+2*i for i in x])
y2 = np.array([(-0.4)*i**2+4*i for i in x])
y3 = np.array([2*i for i in x])
labels = ["y1", "y2", "y3"]
fig, ax = plt.subplots()
ax.stackplot(x, y1, y2, y3, labels=labels)
ax.legend(loc='upper left')


# Figure 9
vals = [24, 17, 53, 21, 35]
labels = ["Ford", "Toyota", "BMV", "AUDI", "Jaguar"]
explode = (0, 0, 0.15, 0, 0)

fig, ax = plt.subplots()
ax.pie(vals, labels=labels, explode=explode)
ax.axis("equal")


# Figure 10
vals = [24, 17, 53, 21, 35]
labels = ["Ford", "Toyota", "BMV", "AUDI", "Jaguar"]
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, wedgeprops=dict(width=0.5))


plt.show()
