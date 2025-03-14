import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = []
for i in x:
    y.append(x[i])
plt.plot(y, color='green')
y.clear()
for i in x:
    y.append(x[i] * 2)
plt.plot(y, color='red')
y.clear()
for i in x:
    y.append(x[i] * 3)
plt.plot(y, color='blue')
y.clear()
for i in x:
    y.append(x[i]**2)
plt.plot(y, color='green')
y.clear()
for i in x:
    y.append(x[i]**2 * 2)
plt.plot(y, color='black')
y.clear()

plt.title('графики')
plt.show()