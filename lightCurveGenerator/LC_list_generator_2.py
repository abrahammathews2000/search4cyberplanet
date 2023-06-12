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
from LC_list_generator import generate_lc_dict

# generate_lc_dict(rad = rad_list[typeShape],edgy = edgy_list[typeShape],noEdges = noEdges_list[typeShape], descpType = typeShape,noVariety = 2)
''' 
rad_array = np.linspace(0.,1.,5) #[0.   0.25 0.5  0.75 1.  ] Give it manually
edgy_array = np.linspace(0,9,10)
edges = np.array([3,4,5,6,7,8,9,10])
variety = 3
print("No. of shapes = ", len(rad_array)*len(edgy_array)*len(edges)*variety)
print("rad_array = ",rad_array)
print("edgy_array = ",edgy_array)
print("edges = ",edges)
print("File name rad_edgy_noEdges_variety")
# for i in rad_array: (Due to crashing rad is given manually)
for j in edgy_array:
    for k in edges:
        generate_lc_dict(rad=1,edgy=j,noEdges=k,noVariety=variety)
'''
generate_lc_dict(rad=0.1,edgy=0.3,noEdges=3,noVariety=1)