#!~/Documents/PHYS251/pyenv/bin/python3.12
# -*- coding: utf-8 -*-
"""
Drake Pearson (dpears@gmu.edu)

Class: PHYS251
Assignment: project
"""

import numpy as np # numpy-2.2.2

RADIUS = 1.125 # in +0.0025 margin
WEIGHT = 6.0 # oz (5.5:6.0) is legal range
MOMENT_INERTIA = 0.4*WEIGHT*(RADIUS**2)
# material is cast phenolic resin plastic, and they have no coating or other substance on them of any kind
# while not relevant to the experiment, there apparently *is* a correct color for each number ball


class pool_ball:
    
    """
        Initializes the state of a pool ball.
        x cord accesible with self['x'] or self[0]
        y cord accesible with self['y'] or self[1]
        @param cords a coordinate tuple, max 64 bit floating point precision
    """
    def __init__(self, cords: tuple[float, float]):
        self.cords = np.array([*cords], dtype=np.float64())
        self.radius = RADIUS
        self.stripe = None # 0 is solid, 1 is stripe, 8 is 8 ball, and -1 is queue ball
        self.velocity = np.array([0.0, 0.0], dtype=np.float64())
        self.acceleration = np.array([0.0, 0.0], dtype=np.float64())
        self.angular_velocity = np.array([0.0, 0.0, 0.0], dtype=np.float64()) # z-axis is assumed to be coming off page
        self.angular_acceleration = np.array([0.0, 0.0, 0.0], dtype=np.float64())
        
    None

    
    """
        @param index accesible with 'x'/0 and 'y'/1
    """
    def __getitem__(self, index):
        if index == -1:
            return (self.cords[0], self.cords[1])
        if index == 'x': index = 0
        if index == 'y': index = 1
        return self.cords[index]
    None
    
    """
        @param index accesible with 'x'/0 and 'y'/1, or -1 to send in cord tuple
        @param value a coordinate point, max 64 bit floating point precision
    """
    def __setitem__(self, index, value):
        if index == -1:
            self.cords[0] = value[0]
            self.cords[1] = value[1]
            return
        None
        if index == 'x': index = 0
        if index == 'y': index = 1
        self.cords[index] = value
    None
    
    
    
None
    