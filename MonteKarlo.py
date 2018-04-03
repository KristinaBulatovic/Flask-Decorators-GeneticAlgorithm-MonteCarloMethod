# y1 = 2 + koren od x
# y2 = x2 / 4

import matplotlib.pyplot as plt
import numpy as np
import random

s1 = "2 + np.math.sqrt(x)"
s2 = "x / 4"

x = np.arange(0.0, 6.0, 1.0)
y1 = []
y2 = (x**2) / 4

for i in np.arange(0.0, 6.0, 1.0):
    y1.append(2 + np.math.sqrt(i))

plt.figure(1)
plt.subplot(111)
plt.plot(x, y1)

plt.figure(1)
plt.plot(x, y2)
ax = plt.gca()
plt.show()

def f(n):
    pog = 0;
    for i in range(n):
        xrand = random.uniform(0,4)
        yrand = random.uniform(0,4)
        y1 = 2 + np.math.sqrt(xrand)
        y2 = (xrand ** 2) / 4
        if ( y1 > yrand > y2):
            pog+=1
    print(xrand, yrand, y1, y2)
    return(pog/n)
print("Broj gadjanja Površina")
print('{:>10d} {:<5.4}'.format(1000000,f(1000000)))
