import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
edrus = [300, 315, 238, 344]
kprf = [52, 57, 92, 42]
spravrus = [36, 40, 64,39]
ldpr = [36, 38, 56, 23]
plt.plot(x, edrus, color='blue')
plt.plot(x, kprf, color='red')
plt.plot(x, spravrus, color='black')
plt.plot(x, ldpr, color='green')
plt.show()
