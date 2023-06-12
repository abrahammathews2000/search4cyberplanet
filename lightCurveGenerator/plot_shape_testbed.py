from PIL import Image

from numpy import asarray

# load the image

image = Image.open('./generatedData/shape/1_0shape.jpg')

# convert image to numpy array

data = asarray(image)

print(type(data))

# summarize shape

print(data.shape)