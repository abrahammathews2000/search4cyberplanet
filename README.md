# search4cyberplanet
**Hunt for technologically advanced alien civilization...**

**Original Code from: https://github.com/ushasi-bhowmick/alienworlds**

**Things you can try:**

1. To see the transit lightcurve simulation for a single shape, run **single_LC_generator.py**.
You can specify the shape in the code

2. To generate and save shape(s) and their corresponding lightcurve(s) as jpg and csv files respectively, run  **LC_list_generator_2.py**. You can specify the parameter of the shape and simulation in the code

**Description of files in lightCurveGenerator folder**

*transitCurveGenerator.py*
: Contains the functions to do the simulation to generate light curves. This file is called by other codes. 

*single_LC_generator.py*
: Use this code to create light curve of a single shape. You can specify the details of the shape by editing the parameters in the code.

*bezier.py*
: This contains functions called by other python programs to generate bezier shapes

*LC_list_generator.py*
: This function creates a folder generatedData and contains the function generate_lc_dict(rad,edgy,noEdges,noVariety). Saves the bezier shape as jpg and  corresponding light curve as an array

*LC_list_generator_2.py*
: Run this file to save the bezier shapes and its corresponding light curve. This file calls the function generate_lc_dict from LC_list_generator.py. This code can be used to test any changes made in LC_list_generator.py

*plotSavedTC.py*
: Edit and run this file to plot any saved Transit curve

*plot_shape_testbed.py*
: Edit and run this file to plot any saved Bezier shape

**Description of file in ML_model folder**

*ML_model_gcolab_v1.ipynb*
: It was an attempt to train a machine learning model on 600 shapes and corresponding lightcurves.
