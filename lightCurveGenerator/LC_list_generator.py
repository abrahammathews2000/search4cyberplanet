import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.optimize import root_scalar
import copy
from gfg import in_or_out
from bezier import get_random_points,get_bezier_curve
from transitCurveGenerator import Megastructure,Simulator,Transit_Animate
import pandas as pd



sim1 = Simulator(100, 5000, 100, np.pi/3)

for i in range(3):
    ## For start of Bezier
    rad = 0.2
    edgy = 0.05
    a = get_random_points(n=10, scale=1)*85
    x,y, _ = get_bezier_curve(a,rad=rad, edgy=edgy)
    z = np.zeros(len(x))
    coord_bezier = np.stack((x, y,z), axis=1)
    plt.figure(figsize=(8, 8))
    plt.tick_params(left=False, right=False, labelleft=False,labelbottom=False, bottom=False)
    plt.plot(x, y,"black")
    plt.fill(x, y,"black")
    plt.savefig("./generatedData/"+str(i) + ".jpg")
    ## End of Bezier shape generation

    #coord_triangle = np.array([(0,40,0),(40,0,0),(-40,0,0),(-32,-23,0),(-60,70,0)])
    meg_2d = Megastructure(Rorb=200, iscircle = False, Rcircle = 40, isrot=True, Plcoords=coord_bezier,incl=0*np.pi/180, ph_offset=0, elevation=0, ecc=0, per_off=0*np.pi/2)

    sim1.add_megs(meg_2d)
    sim1.simulate_transit()

    #vv Comment below two lines to not show animation
    #TA = Transit_Animate(sim1.road, sim1.megs, sim1.lc, sim1.frames)
    #TA.go()
    ##^^
    #plt.plot(sim1.frames,sim1.lc)
    np.savetxt("./generatedData/"+str(i) + 'lc.csv', np.array(sim1.lc), delimiter=',')
    #print(sim1.frames)
    #print(sim1.lc)
plt.show()
np.savetxt("./generatedData/" + 'phase.csv', np.array(sim1.frames), delimiter=',')
print("Completed")