from PIL import Image

from numpy import asarray

# load the image

image = Image.open('/home/abraham/Documents/IIST_Academics/Astro_2ndYear/Alien_Megastructure/My_code_2023/1edit_Code_here/search4cyberplanet/lightCurveGenerator/generatedData/0.1_0.3_4_0shape.jpg')

# convert image to numpy array

data = asarray(image)

print(type(data))

# summarize shape

print(data.shape)