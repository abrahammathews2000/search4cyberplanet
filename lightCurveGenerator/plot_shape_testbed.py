from PIL import Image
import numpy as np
from numpy import asarray

# load the image

# image = Image.open('./generatedData/shape/1_0shape.jpg')
shape_dict_read = np.load('./generatedData/shape_dict.npy')
img = Image.fromarray(shape_dict_read[0])
img.show()
# convert image to numpy array
#
# data = asarray(image)
#
# print(type(data))

# summarize shape
#print(data.shape)