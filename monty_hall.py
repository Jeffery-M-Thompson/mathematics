#!/usr/bin/env python3

import numpy as np
import random as rd

n = 0
mn = int(1E9)

keepwin = 0
changewin = 0

for n in range(n, mn):
	n +=1
	door = rd.randint(1, 3)
	pick = rd.randint(1, 3)
	if door == pick:
		keepwin +=1
	else:
		changewin +=1

print ('{0} chance of winning if we keep our initial door.'.
	format(float(keepwin/mn)))
print ('{0} chance of winning if we switch our initial door'.
	format(float(changewin/mn)))
	
	
