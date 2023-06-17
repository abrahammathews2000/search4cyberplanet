# File: LC_list_generator.py
# Aim:  This code contain the function generate_lc_dict, which can be called
#       by other programs to generate and save:
#           (i) bezier shape as jpg file
#           (ii) lightcurve as csv file and
# Date: June 16, 2023

import numpy as np
import matplotlib.pyplot as plt
from bezier import get_random_points,get_bezier_curve
from transitCurveGenerator import Megastructure,Simulator,Transit_Animate
import os
import cv2

def generate_lc_dict(rad,edgy,noEdges,noVariety,name,Rstar_siml = 100,Rmega_star = 0.5,orbit_radius = 200,sampling_pts = 7000,no_of_frames = 500,length_of_frames = np.pi / 3,shape_pixel = 0.32):
    """
    Generate and saves the bezier shape as jpg along with its corresponding lightcurve as csv
    Bezier shape will be saved in the folder ./generatedData/shape/ as shape0name_variety.jpg
    Lightcurve will be saved in the folder ./generatedData/lc/array/ as lc0name_variety.jpg
    where term variety will go from 0 to (noVariety - 1).

    Parameters
    ----------
    rad : float
        It is a number between 0 and 1 to steer the distance of control points.
    edgy : float
        It is a parameter which controls how "edgy" the curve is, edgy=0 is smoothest.
    noEdges : int
        It is the required number of edges for the bezier curve.
    noVariety : int
        It is the number of the different shapes required for the same parameters of rad, edges and
        noEdges.
    name: int
        It is the name to which the files are to be saved to as given in the description.
        For example, name = 2 will save shape as shape02_0.jpg and lightcurve as lc02_0.jpg
    Rstar_siml: float
        It is the radius of star. By default, it is 100
    Rmega_star: float
        It is the ratio of radius of megastructure to star. By default, it is 0.5.
    orbit_radius: float
        Radius of the orbit of megastructure. By default, it is 200
    sampling_pts: int
        By default, it is 7000,
    no_of_frames: int
        By default, it is 500,
    length_of_frames: float
        By default, it is np.pi / 3,
    shape_pixel: float
        It is the number of pixels along one axis for saving bezier shape as jpeg.
        By default, it is 0.32 (corresponding to 32 x 32 pixel output)
    """

    # Make directory to save bezier shape as jpg and lightcurve as csv
    if not os.path.exists('./generatedData/'):
        os.mkdir('./generatedData/')
    if not os.path.exists('./generatedData/shape/'):
        os.mkdir('./generatedData/shape/')
    if not os.path.exists('./generatedData/lc/'):
        os.mkdir('./generatedData/lc/')
    if not os.path.exists('./generatedData/lc/array/'):
        os.mkdir('./generatedData/lc/array/')

    # Initialize the simulator
    # Specify simulator parameters
    sim1 = Simulator(Rstar=Rstar_siml, no_pt=sampling_pts, frame_no=no_of_frames, frame_length=length_of_frames)
    Rmega = Rmega_star * Rstar_siml
    # Create shape and LC
    for i in range(noVariety):
        ## Bezier shape generation
        plt.clf()
        #rad = 0.2
        #edgy = 0.05
        a = get_random_points(n=noEdges, scale=1)
        x,y, _ = get_bezier_curve(a,rad=rad, edgy=edgy)
        x = (x - np.mean(x)) * Rmega * 2
        y = (y - np.mean(y)) * Rmega * 2
        z = np.zeros(len(x))
        coord_bezier = np.stack((x, y,z), axis=1)
        #np.savetxt("./generatedData/" + str(rad)+"_"+str(edgy)+"_"+str(noEdges)+"_"+str(i) + 'bezierCoord.csv', coord_bezier, delimiter=',')
        plt.figure(figsize=(shape_pixel,shape_pixel))
        plt.tick_params(left=False, right=False, labelleft=False,labelbottom=False, bottom=False)
        plt.plot(x, y,"black")
        #plt.fill(x, y,"black")
        plt.axis('off') # To remove frame box
        #data = np.random.randint(256, size=(100, 100), dtype=np.uint8)
        #img = Image.fromarray(data)
        #plt.savefig("./generatedData/" + str(rad)+"_"+str(edgy)+"_"+str(noEdges)+"_"+str(i) +"shape.jpg")
        plt.savefig("./generatedData/shape/shape0" + str(name) + "_" + str(i) + ".jpg")
        plt.close()
        # plt.clf()

        # Convert RGB to grayscale
        image2cnvt = cv2.imread("./generatedData/shape/shape0" + str(name) + "_" + str(i) + ".jpg")
        #cv2.imshow('Original', image)
        gray_cnvtd = cv2.cvtColor(image2cnvt, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("./generatedData/shape/shape0" + str(name) + "_" + str(i) + ".jpg", gray_cnvtd)
        ## End of Bezier shape generation

        meg_2d = Megastructure(Rorb=orbit_radius, iscircle = False, Rcircle = 40, isrot=True, Plcoords=coord_bezier,incl=0*np.pi/180, ph_offset=0, elevation=0, ecc=0, per_off=0*np.pi/2)
        sim1.add_megs(meg_2d)
        sim1.simulate_transit()
        lc_array = np.array(sim1.lc)


        #vv Comment below two lines to not show animation
        # TA = Transit_Animate(sim1.road, sim1.megs, sim1.lc, sim1.frames)
        # TA.go()
        ##^^
        # plt.figure(figsize=(8, 8))
        # plt.plot(np.array(sim1.frames),lc_array,color="black")
        np.savetxt("./generatedData/lc/array/lc0" + str(name) +"_"+str(i) + ".csv", lc_array, delimiter=',')
        #plt.savefig("./generatedData/lc/jpg/lc0" + str(name) +"_"+str(i) +".jpg")
        #print(sim1.frames)
        #print(sim1.lc)
        # plt.close()
    #plt.show()
    #To save the x-axis of light curve (phase)
    # np.savetxt("./generatedData/" + 'phase.csv', np.array(sim1.frames), delimiter=',')
    print("Completed", " - ", str(rad),"_",str(edgy),"_",str(noEdges),"_",str(i))


# Old codes are given below which where used for experimenting
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