# File: single_LC_generator.py
# Aim: Run this code to generate LC and animation for single shape
# Date: June 16, 2023

import numpy as np
import matplotlib.pyplot as plt
from bezier import get_random_points,get_bezier_curve
from transitCurveGenerator import Simulator, Megastructure,Transit_Animate

# 1. Specify the radius of star
Rstar_siml = 100    # Radius of star (edit this as you require)

# 2. Initialize the simulator
# Specify simulator parameters
sampling_pts = 6000         # edit this as you require
no_of_frames = 500          # edit this as you require
length_of_frames = np.pi/3  # edit this as you require

sim1 = Simulator(Rstar = Rstar_siml, no_pt = sampling_pts,frame_no = no_of_frames, frame_length = length_of_frames)

# 3. Specify the parameters to generate megastructure shape
orbit_radius = 200          # Radius of the orbit of megastructure
Rmega_star = 0.5            # Radius of megastructure in as fraction of radius of star  (edit this as you require)
isItCircle = False          # True - generates circle shaped megastructure
                            # False - generates Bezier shaped megastructure
# Following 3 parameters are for generating Bezier shaped megastructure
rad = 0.2                   # (edit this as you require)
edgy = 0.05                 # (edit this as you require)
no_of_edge = 5              # (edit this as you require)

Rmega = Rmega_star * Rstar_siml # Radius of megastructure (calculated value)
a = get_random_points(n=no_of_edge, scale=1)
x,y, _ = get_bezier_curve(a,rad=rad, edgy=edgy)
x = (x - np.mean(x)) * Rmega*2
y = (y - np.mean(y)) * Rmega*2
z = np.zeros(len(x))
coord_bezier = np.stack((x, y,z), axis=1) # Contains the coordinate of bezier shape

# Initialize the megastructure
meg_2d = Megastructure(Rorb=orbit_radius, iscircle = isItCircle, Rcircle = Rmega, isrot=True, Plcoords=coord_bezier,incl=0, ph_offset=0, elevation=0, ecc=0, per_off=0)
sim1.add_megs(meg_2d)


# 4. Start the transit simulation
sim1.simulate_transit()

# -----
# Comment below three lines to not show animation
TA = Transit_Animate(sim1.road, sim1.megs, sim1.lc, sim1.frames)
TA.go(ifsave=False, filepath="")    # To save the animation give ifsave = True
                                    # and filepath as somename.gif
# -----

# 5. Plot the light curve
plt.plot(sim1.frames,sim1.lc)
plt.show()
# print(sim1.frames)
# print(sim1.lc)



#Old codes below (ignore them)
#meg_2d = Megastructure(Rorb=200, iscircle = True, Rcircle = 50, isrot=True, incl=20*np.pi/180, ph_offset=0, elevation=0, ecc=0, per_off=np.pi/2)
#meg_2d_2 = Megastructure(Rorb=250, iscircle = True, Rcircle = 40, isrot=True, incl=5*np.pi/180, ph_offset=0.5, elevation=0, ecc=0, per_off=np.pi/2)
#coord_triangle = np.array([(0,40,0),(40,0,0),(-40,0,0),(-32,-23,0),(-60,70,0)])
