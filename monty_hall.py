#/usr/bin/env python

import numpy as np
import random as rd

n = 0
mn = 10
keepwin = 0
changewin = 0
for n in range(n, mn):
	n +=1
	doors = [1, 2, 3]
	door = rd.randomint(1, 3)
	pick = rd.randomint(1, 3)
	doors.remove(door)
	
	
