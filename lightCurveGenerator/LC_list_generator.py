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

def generate_lc_dict(rad,edgy,noEdges,descpType):
    sim1 = Simulator(100, 5000, 100, np.pi/3)
    for i in range(10):
        ## For start of Bezier
        plt.clf()
        #rad = 0.2
        #edgy = 0.05
        a = get_random_points(n=noEdges, scale=1)*85
        x,y, _ = get_bezier_curve(a,rad=rad, edgy=edgy)
        z = np.zeros(len(x))
        coord_bezier = np.stack((x, y,z), axis=1)
        np.savetxt("./generatedData/" + "Type"+ str(descpType) + "_"+str(i) + 'bezierCoord.csv', coord_bezier, delimiter=',')
        plt.figure(figsize=(8, 8))
        plt.tick_params(left=False, right=False, labelleft=False,labelbottom=False, bottom=False)
        plt.plot(x, y,"black")
        plt.fill(x, y,"black")
        plt.savefig("./generatedData/"+ "Type"+ str(descpType) + str(i) + ".jpg")
        plt.clf()
        ## End of Bezier shape generation

        #coord_triangle = np.array([(0,40,0),(40,0,0),(-40,0,0),(-32,-23,0),(-60,70,0)])
        meg_2d = Megastructure(Rorb=200, iscircle = False, Rcircle = 40, isrot=True, Plcoords=coord_bezier,incl=0*np.pi/180, ph_offset=0, elevation=0, ecc=0, per_off=0*np.pi/2)

        sim1.add_megs(meg_2d)

        sim1.simulate_transit()
        lc_array = np.array(sim1.lc)
        '''
        Was trying to average out but it was not working
        Problem: while concatinating arrays, they are getting concatenated after one array
        as elements instead as one new array and also same value is coming for new simulations
        print("Outside for loop: ", lc_array)
        for j in range(5):
            sim1.simulate_transit()
            # data = np.stack((data,np.random.rand(1,4)),axis = 1)
            lc_array = np.concatenate((lc_array, np.array(sim1.lc)), axis=0)
            print("lc array = ",lc_array)
            # savetxt(str(i)+'data.csv', data, delimiter=',')
            #print(data)
        lc_avg = np.mean(lc_array, axis=0)
        print("Average = ", lc_avg)
        '''

        #vv Comment below two lines to not show animation
        #TA = Transit_Animate(sim1.road, sim1.megs, sim1.lc, sim1.frames)
        #TA.go()
        ##^^
        plt.plot(np.array(sim1.frames),lc_array)
        np.savetxt("./generatedData/"+ "Type"+ str(descpType) + str(i) + 'lc.csv', lc_array, delimiter=',')
        plt.savefig("./generatedData/" + "Type"+ str(descpType) +  str(i) + "lc..jpg")
        #print(sim1.frames)
        #print(sim1.lc)
    #plt.show()
    np.savetxt("./generatedData/" + 'phase.csv', np.array(sim1.frames), delimiter=',')
    print("Completed" + str(descpType))
    plt.close()
rad_list = [0.2,0.3]
edgy_list = [0.05,0.07]
noEdges_list = [5,9]
for typeShape in range(len(rad_list)):
    generate_lc_dict(rad = rad_list[typeShape],edgy = edgy_list[typeShape],noEdges = noEdges_list[typeShape], descpType = typeShape)