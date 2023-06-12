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
import os

if not os.path.exists('./generatedData/'):
    os.mkdir('./generatedData/')
#print("File name rad_edgy_noEdges_variety")
def generate_lc_dict(rad,edgy,noEdges,noVariety):
    if not os.path.exists('./generatedData/'):
        os.mkdir('./generatedData/')
    sim1 = Simulator(100, 5000, 100, np.pi/3) # Put frame length np.pi to get full transit curve
    for i in range(noVariety):
        ## For start of Bezier
        plt.clf()
        #rad = 0.2
        #edgy = 0.05
        a = get_random_points(n=noEdges, scale=1)*70
        x,y, _ = get_bezier_curve(a,rad=rad, edgy=edgy)
        z = np.zeros(len(x))
        coord_bezier = np.stack((x, y,z), axis=1)
        np.savetxt("./generatedData/" + str(rad)+"_"+str(edgy)+"_"+str(noEdges)+"_"+str(i) + 'bezierCoord.csv', coord_bezier, delimiter=',')
        plt.figure(figsize=(1, 1))
        plt.tick_params(left=False, right=False, labelleft=False,labelbottom=False, bottom=False)
        plt.plot(x, y,"black")
        plt.fill(x, y,"black")
        plt.axis('off') # To remove frame box
        plt.savefig("./generatedData/" + str(rad)+"_"+str(edgy)+"_"+str(noEdges)+"_"+str(i) + ".jpg")
        plt.close()
        plt.clf()
        ## End of Bezier shape generation

        #coord_triangle = np.array([(0,40,0),(40,0,0),(-40,0,0),(-32,-23,0),(-60,70,0)])
        meg_2d = Megastructure(Rorb=200, iscircle = False, Rcircle = 40, isrot=True, Plcoords=coord_bezier,incl=0*np.pi/180, ph_offset=0, elevation=-25, ecc=0, per_off=0*np.pi/2)

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
        # TA = Transit_Animate(sim1.road, sim1.megs, sim1.lc, sim1.frames)
        # TA.go()
        ##^^
        plt.figure(figsize=(8, 8))
        plt.plot(np.array(sim1.frames),lc_array,color="black")
        np.savetxt("./generatedData/" + str(rad)+"_"+str(edgy)+"_"+str(noEdges)+"_"+str(i) + 'lc.csv', lc_array, delimiter=',')
        plt.savefig("./generatedData/" + str(rad)+"_"+str(edgy)+"_"+str(noEdges)+"_"+str(i) +"lc.jpg")
        #print(sim1.frames)
        #print(sim1.lc)
        plt.close()
    #plt.show()
    np.savetxt("./generatedData/" + 'phase.csv', np.array(sim1.frames), delimiter=',')
    print("Completed", " - ", str(rad),"_",str(edgy),"_",str(noEdges),"_",str(i))
      # To save memory for next iteration

#vv Comment below section to use this file for importing to other files
# rad_array = 0.2 #[0.2] #,0.3]
# edgy_array = 0.5 # [0.05] #,0.07]
# edges = 5 # [5] #,9]
# variety = 2
# for typeShape in range(len(rad_list)):
#   Obsolete  generate_lc_dict(rad = rad_list[typeShape],edgy = edgy_list[typeShape],noEdges = noEdges_list[typeShape], descpType = typeShape,noVariety = 1)
#^^
#Comment below line when importing this file in other file
#generate_lc_dict(rad=rad_array,edgy=edgy_array,noEdges=edges,noVariety=variety)