import matplotlib.pyplot as plt
import random
x = [1, 7, 3, 6, 2]
y = [2, 4, 3, 1, 5]
pointsx = []
pointsy = []
for i in x:
    p = x[i]
    for i in range(10):
        pointsx.append(random.choice([p - 1, p + 1]))
for i in y:
    p = y[i]
    for i in range(10):
        pointsy.append(random.choice([p - 1, p + 1]))

plt.scatter(x, y)
plt.scatter(pointsx, pointsy)

plt.show()
