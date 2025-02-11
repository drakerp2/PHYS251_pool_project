#!~/Documents/PHYS251/pyenv/bin/python3.12
# -*- coding: utf-8 -*-
"""
Drake Pearson (dpears@gmu.edu)

Class: PHYS251
Assignment: project
"""

#import numpy as np # numpy-2.2.2
#from np import array, ndarray 
import matplotlib as mpl # matplotlib-3.10.0
from matplotlib import pyplot as plt 

from project.pool_table import pool_table

table = pool_table()

fig, ax = plt.subplots()
for ball in table.balls: ax.add_patch(plt.Circle(
    xy = ball[-1], 
    radius = ball.radius,
    color = (
        'red' if ball.stripe == 0 else 
        'blue' if ball.stripe == 1 else 
        'black' if ball.stripe == 8 else 
        'gray' if ball.stripe == -1 else 
        "yellow" # yellow is error state
    )
))


plt.xlim(0,50)
plt.ylim(0,100)
#plt.xlim(15,35)
#plt.ylim(15,28)
ax.set_aspect(1)
plt.show()


    

