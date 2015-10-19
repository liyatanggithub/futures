#!/usr/bin/python
#import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 1, 0, 100])
plt.ion()

for i in range(100):
 #       y = np.random.random()
        plt.scatter(i/100.0, i)
        plt.pause(0.1)
plt.axis([0, 1, 0, 200])
for i in range(200):
        plt.scatter(i/200.0, i)
        plt.pause(0.1)
