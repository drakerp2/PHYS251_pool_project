#!~/Documents/PHYS251/pyenv/bin/python3.12
# -*- coding: utf-8 -*-
"""
Drake Pearson (dpears@gmu.edu)

Class: PHYS251
Assignment: project
"""

import numpy as np # numpy-2.2.2


from pool_ball import pool_ball as ball


""" 
https://wpapool.com/wp-content/uploads/2024/01/RECOMMENDED-EQUIPMENT-SPECIFICATIONS.pdf
This is the World Pool Asociation's - the formally recognized international 
govening body on the sport - official standards for a regulation pool table.

This standard outlines a certain amount of error margin still legal even in
tournament level play. In this project we will use math and kinematics to
determine how large (or small) an effect these margins can have on play.

Additionally, we will use the frictional constants provided here
https://billiards.colostate.edu/faq/physics/physical-properties/

The lack of a clear definetion of the frictional constants by any governing body
makes it a perfect place to begin experimenting with the effects inconsistency
may have on play.

My hypothesis, is that while none of these error margins will have a significant
impact on their own, when combined together it will result in a noticable change
in how the balls move.
"""

## I have elected to use more values that equate to exact floating point values
## this is done to increase the ease of establishing my initial state, by 
## reducing the chance for floating point error

LENGTH = 100.0 # in +1/8 margin, this is the play area not including cusions
WIDTH = 50.0 # in +1/8 margin, this is the play area not including cusions
RAIL_WIDTH = 5.0 # in (4.0:7.5) is the legal range, the entire rail
CUSHION_WIDTH = 2.0 # in (1.875:2.0) is the legal range, the rubber tip of the rail
CUSHION_HEIGHT = 0.625 # % of ball diameter (0.625:645) is the legal range
POCKET_FACING = 0.09375 # = 3/32 in (1/16:1/4) is the legal range, WPA advises max 1/8 
CORNER_MOUTH = 4.5 # in (4.5:4.625) is the legal range
SIDE_MOUTH = 5.0 # in (5.0:5.125) is the legal range, generally 0.5 in larger than corner
VERTICAL_POCKET_ANGLE = 0.25 # rad (pi/15:pi/12) is the legal range, this is the very slight slope going into the pocket.  It may have to be ignored to not make equations significantly more complicated.
CORNER_HORIZONTAL_POCKET_ANGLE = 0.484375 # = 31/64 rad (71pi/90:143pi/180) is the legal range
SIDE_HORIZONTAL_POCKET_ANGLE = 0.828125 # = 53/64 rad (26pi/45:7pi/12) is the legal range
CORNER_SHELF = 1.5 # in (1.0:2.25) is the legal range
SIDE_SHELF = 0.125 # in (0.0:0.375) is the legal range
# We assume the cusions are perfectly smoothe
# We assume the table perfectly flat

CUE_LENGTH = 40.0 # in (>=40) is legal
CUE_WEIGHT = 25.0 # in (<=25) is legal
CUT_TIP_WIDTH = 0.53125 # = 17/32 in (<=14mm) is legal (they mixed units, but I'm keeping everything in inches)

BALL_BALL_FRICTION = 0.0625 # (0.03:0.08) is range given
BALL_BALL_RESTITUTION = 0.96875 # = 31/32 (0.92:0.98) is range given
BALL_CLOTH_ROLLING_FRICTION = 0.01171875 # = 3/256 (0.005:0.015) is range given
BALL_CLOTH_SLIDING_FRICTION = 0.203125 # = 13/64 (0.15:0.4) is range given, 0.2 is stated as typical
BALL_CLOTH_SPIN_DECELERATION = 10.0 # rad/s^2 (5:15) is range given
BALL_RAIL_RESTITUTION = 0.75 # (0.6:0.9) is range given
BALL_TABLE_RESTITUTION = 0.625 # (0.5:0.7) is range given
CUE_BALL_FRICTION = 0.599609375 # = 307/512 0.6, no range given
CUE_BALL_RESTITION = 0.75 # (0.71:0.75) is range given for leather, (0.81:0.87) is range given for phenolic


RACK_ANGLE = np.deg2rad(60) # this should, in theory, be the only source of floating point aproximation we have


class pool_table:
    
    def __init__(self):
        self.balls = np.array([ball((0.0,0.0)) for i in range(16)])
        self[1][-1] = (WIDTH/2, LENGTH/4); self[1].stripe = 0
        self.__declare_ball(2, 1, 1, True); self.__declare_ball(3, 1, 0)
        self.__declare_ball(4, 2, 0, True); self.__declare_ball(5, 2, 8); self.__declare_ball(6, 3, 1)
        self.__declare_ball(7, 4, 1, True); self.__declare_ball(8, 4, 0); self.__declare_ball(9, 5, 1); self.__declare_ball(10, 6, 0)
        self.__declare_ball(11, 7, 0, True); self.__declare_ball(12, 7, 1); self.__declare_ball(13, 8, 1); self.__declare_ball(14, 9, 0); self.__declare_ball(15, 10, 1)
        
        self[0][-1] = (WIDTH/2, 3*LENGTH/4); self[0].stripe = -1 # queue ball
        
    None
    
    def __declare_ball(self, cur, prev, stripe, left=False):
        self[cur]['x'] = self[prev]['x']+(self[1].radius*(-1 if left else 1))
        self[cur]['y'] = self[prev]['y']-(np.tan(RACK_ANGLE)*self[prev].radius)
        self[cur].stripe = stripe
    None

    def __getitem__(self, index):
        return self.balls[index]
    None
    
    def __setitem__(self, index, value):
        self.balls[index] = value
    None
    
None