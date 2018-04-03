# y1 = (1/4 * (x-4) ** 3) + 4
# y2 = x

import matplotlib.pyplot as plt
import numpy as np
import random

x = np.arange(0.0, 7.0, 1.0)
y1 = []
y2 = x

for i in np.arange(0.0, 7.0, 1.0):
    y1.append((1/4 * (x-4) ** 3) + 4)

y1 = y1[0]

plt.figure(1)
plt.subplot(111)
plt.plot(x, y1)

plt.figure(1)
plt.plot(x, y2)
ax = plt.gca()
plt.show()

def f(n):
    pog1 = 0;
    pog2 = 0;
    for i in range(n):
        xrand1 = random.uniform(2,4)
        yrand1 = random.uniform(2,4)
        xrand2 = random.uniform(4, 6)
        yrand2 = random.uniform(4, 6)
        y1 = (1/4 * (xrand1-4) ** 3) + 4
        y2 = xrand1
        y3 = (1 / 4 * (xrand2 - 4) ** 3) + 4
        y4 = xrand2
        if ( y1 > yrand1 > y2):
            pog1 += 1
        if (y4 > yrand2 > y3):
            pog2 += 1

    return((4 * pog1/n) + (4 * pog2/n))

print(f(1000000))
