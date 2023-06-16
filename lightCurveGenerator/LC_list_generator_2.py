# File: LC_list_generator_2.py
# Aim:  Run this code to generate and save any number of shapes by giving their parameters and
#         their corresponding lightcurves
# Date: June 16, 2023

import numpy as np
from LC_list_generator import generate_lc_dict
import time

# ---
# To measure how much time it takes to run the code
start = time.time()
# ---
# 1 .To create multiple shapes
# ----
rad_array = np.array([0.75])    # rad_array = np.linspace(0.,1.,5)
                                # Do to limited RAM size only one element is give
                                # rad_array for every run
edgy_array = np.linspace(0,9,10)
edges_array = np.array([3,4,5,6,7,8,9,10,11,12])
variety = 2

# NOTE: give the name such that it will not overwrite on already saved files
# name get incremented by 1 for every iteration
name = 301
for rad_el in rad_array:
    for edgy_el in edgy_array:
        for edges_el in edges_array:
            generate_lc_dict(rad=rad_el,edgy=edgy_el,noEdges=edges_el,noVariety=variety,name = name,Rstar_siml = 100,Rmega_star = 0.5)
            name = name + 1
# ----


# 2. Comment (1.) and uncomment below to save LC and bezier shape for only 1 shape
# ----
# variety = 2
# name = 1
# generate_lc_dict(rad=0.2,edgy=0.4,noEdges=6,noVariety=2,name = 5,Rstar_siml = 100,Rmega_star = 0.5)
# name = name + 1
# ----

end = time.time()
print(end - start)


# Old code below vv
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
#generate_lc_dict(rad=0.1,edgy=0.3,noEdges=5,noVariety=2,name = 10,Rstar_siml = 100,Rmega_star = 0.5)
#generate_lc_dict(rad=0.2,edgy=0.4,noEdges=4,noVariety=2,name = 5,Rstar_siml = 100,Rmega_star = 0.5)