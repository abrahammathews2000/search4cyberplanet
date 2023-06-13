import numpy as np
import os
from natsort import natsorted
import imageio.v3 as iio
# import visvis as vv
#from skimage.io import imread_collection

lc_dir = './generatedData/lc/array/'
shape_dir = './generatedData/shape/'

lc_filenames = natsorted(os.listdir(lc_dir))
shape_filenames = natsorted(os.listdir(shape_dir))

print('lc_filenames = ',lc_filenames)
print('shape_filenames = ',shape_filenames)

no_files = len(shape_filenames)

print('length - lc_filenames = ',len(lc_filenames))
print('length - shape_filenames = ',no_files)

lc_dict = np.zeros((no_files,500))
shape_dict = np.zeros((no_files,32,32))

print('lc_dict = ',lc_dict)
print('shape_dict = ',shape_dict)

# os.chdir(lc_dir)
i = 0
for lc_element in lc_filenames:
    lc_dict[i] = np.loadtxt(lc_dir+lc_element, delimiter=',')
    i = i + 1

np.save('./generatedData/lc_dict.npy', lc_dict)
lc_dict_read = np.load('./generatedData/lc_dict.npy')
print('lc_dict = ',lc_dict_read)
# print('lc_dict = ',lc_dict[0][220:250])
# print('lc_dict = ',lc_dict[2][220:250])

#os.chdir(shape_dir)
i = 0
for shape_element in shape_filenames:
    shape_dict[i] = np.array(iio.imread(shape_dir+shape_element)) #/255.0
    i = i + 1

np.save('./generatedData/shape_dict.npy', shape_dict)
shape_dict_read = np.load('./generatedData/shape_dict.npy')
print('shape_dict = ',shape_dict_read)
# -- Old codes vv
# # Load output images
# #your path
# img_dir = './generatedData/shape/*.jpg'
# # --- Method 1 to read images
# #creating a collection with the available images
# sci_img = imread_collection(img_dir)
# print('type(col) = ',type(sci_img))
# image = np.array(sci_img)/255.0
# print('type(image) = ',type(image))
# print(np.shape(image))
# print(image)
# # ---

# Load input light curve
# tc = np.loadtxt('./generatedData/lc/1_0lc.csv', delimiter=',')
#lc_train_list = np.sort(np.array(os.listdir('./generatedData/lc/array/')))
# lc_train_list = os.listdir('./generatedData/lc/array/')
# lc_train_list = natsorted(lc_train_list)
# print("lc_train_list = ",lc_train_list)
# -- Method 2 (does not work)
# vol = iio.imread(col_dir)
# vv.volshow(vol)
# --


# y = os.listdir('./generatedData/shape/')
# print(y)
#
# vol = imageio.volread('./generatedData/shape')
# print('vol.shape = ',vol.shape)