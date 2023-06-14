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
import cv2

# if not os.path.exists('./generatedData/'):
#     os.mkdir('./generatedData/')
#print("File name rad_edgy_noEdges_variety")
def generate_lc_dict(rad,edgy,noEdges,noVariety,name,Rstar_siml = 100,Rmega_star = 0.5):
    if not os.path.exists('./generatedData/'):
        os.mkdir('./generatedData/')
    if not os.path.exists('./generatedData/shape/'):
        os.mkdir('./generatedData/shape/')
    if not os.path.exists('./generatedData/lc/'):
        os.mkdir('./generatedData/lc/')
    # if not os.path.exists('./generatedData/lc/jpg/'):
    #     os.mkdir('./generatedData/lc/jpg/')
    if not os.path.exists('./generatedData/lc/array/'):
        os.mkdir('./generatedData/lc/array/')
    # Initialize the simulator
    sim1 = Simulator(Rstar=Rstar_siml, no_pt=7000, frame_no=500, frame_length=np.pi / 3)
    Rmega = Rmega_star * Rstar_siml
    # Create shape and LC
    for i in range(noVariety):
        ## Bezier shape generation
        plt.clf()
        #rad = 0.2
        #edgy = 0.05
        a = get_random_points(n=noEdges, scale=1)*Rmega
        x,y, _ = get_bezier_curve(a,rad=rad, edgy=edgy)
        x = x - np.mean(x)
        y = y - np.mean(y)
        z = np.zeros(len(x))
        coord_bezier = np.stack((x, y,z), axis=1)
        #np.savetxt("./generatedData/" + str(rad)+"_"+str(edgy)+"_"+str(noEdges)+"_"+str(i) + 'bezierCoord.csv', coord_bezier, delimiter=',')
        plt.figure(figsize=(0.32, 0.32))
        plt.tick_params(left=False, right=False, labelleft=False,labelbottom=False, bottom=False)
        plt.plot(x, y,"black")
        #plt.fill(x, y,"black")
        plt.axis('off') # To remove frame box
        #data = np.random.randint(256, size=(100, 100), dtype=np.uint8)
        #img = Image.fromarray(data)
        #plt.savefig("./generatedData/" + str(rad)+"_"+str(edgy)+"_"+str(noEdges)+"_"+str(i) +"shape.jpg")
        plt.savefig("./generatedData/shape/shape0" + str(name) + "_" + str(i) + ".jpg")
        plt.close()
        plt.clf()
        # Convert RGB to grayscale

        image2cnvt = cv2.imread("./generatedData/shape/shape0" + str(name) + "_" + str(i) + ".jpg")
        #cv2.imshow('Original', image)
        gray_cnvtd = cv2.cvtColor(image2cnvt, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("./generatedData/shape/shape0" + str(name) + "_" + str(i) + ".jpg", gray_cnvtd)

        ## End of Bezier shape generation

        #coord_triangle = np.array([(0,40,0),(40,0,0),(-40,0,0),(-32,-23,0),(-60,70,0)])
        meg_2d = Megastructure(Rorb=200, iscircle = False, Rcircle = 40, isrot=True, Plcoords=coord_bezier,incl=0*np.pi/180, ph_offset=0, elevation=0, ecc=0, per_off=0*np.pi/2)

        sim1.add_megs(meg_2d)
        sim1.simulate_transit()
        lc_array = np.array(sim1.lc)


        #vv Comment below two lines to not show animation
        # TA = Transit_Animate(sim1.road, sim1.megs, sim1.lc, sim1.frames)
        # TA.go()
        ##^^
        plt.figure(figsize=(8, 8))
        plt.plot(np.array(sim1.frames),lc_array,color="black")
        np.savetxt("./generatedData/lc/array/lc0" + str(name) +"_"+str(i) + ".csv", lc_array, delimiter=',')
        #plt.savefig("./generatedData/lc/jpg/lc0" + str(name) +"_"+str(i) +".jpg")
        #print(sim1.frames)
        #print(sim1.lc)
        plt.close()
    #plt.show()
    #To save the x-axis of light curve (phase)
    np.savetxt("./generatedData/" + 'phase.csv', np.array(sim1.frames), delimiter=',')
    print("Completed", " - ", str(rad),"_",str(edgy),"_",str(noEdges),"_",str(i))

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