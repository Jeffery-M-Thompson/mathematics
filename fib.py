#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def fib(n):
	fb = []
	rf = np.sqrt(5.0)+ 0j
	for i in n:
		fb.append(((1.0+0j)/rf)*((1.0+rf)/2.0)**(i+1.0)-((1.0+0j)/rf)*((1.0-rf)/2.0)**(i+1.0))
	return fb
	
fig = plt.figure()
ax1 = fig.add_subplot(311, projection='3d')
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)
z = np.arange(-10, 0, 0.001)
fb = fib(z)
x = np.real(fb)
y = np.imag(fb)
ax1.plot(x, y, z)
ax1.set_xlabel('Real Values')
ax1.set_ylabel('Imaginary Values')
ax1.set_zlabel('N')
ax2.plot(x, y)
ax2.set_xlabel('Real Values')
ax2.set_ylabel('Imaginary Values')
ax3.plot(z, x)
ax3.set_xlabel('N')
ax3.set_ylabel('Real Values')
plt.show()

