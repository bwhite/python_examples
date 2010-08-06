import Image
import numpy as np
import matplotlib.pyplot as mp

# See http://www.pythonware.com/library/pil/handbook/image.htm for documentation

img = Image.open('lena.bmp')
img.show()

# Resize by 2
width, height = img.size
img_small = img.resize((width / 2, height / 2))
img_small.show()

# Make gray
img_gray = img.convert('L')
img_gray.show()

# Rotate
img_90deg = img.rotate(90)
img_90deg.show()

# Load gray into a numpy array, display using matplotlib
gray_array = np.fromstring(img_gray.tostring(), dtype=np.uint8).reshape((height, width))
mp.imshow(gray_array)
mp.gray()

# Load gray into a numpy array, display using matplotlib
rgb_array = np.fromstring(img.tostring(), dtype=np.uint8).reshape((height, width, 3))
mp.figure()
mp.imshow(rgb_array)
mp.show()

