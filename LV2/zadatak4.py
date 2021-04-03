import matplotlib.pyplot as plt 
import numpy as np 
import skimage.io
from skimage.transform import rescale, resize

 
img = skimage.io.imread('tiger.png', as_gray=True)
height, width = img.shape

#a)
#matrica = np.ones((640, 960)) * 150
#img = img + matrica
#for i in range(0, height):
    #for j in range(0, width):
        #if img[i][j] > 255:
            #img[i][j] = 255

#b)
#img90 = np.zeros((width, height))
#for j in range(0, height):
    #img90[:, height - j - 1] = img[j, :]

#[:, 1] stupac
#[1, :] redak

#c)
#imgmirror = np.zeros((height, width))

#for j in range(0, width):
    #imgmirror[:, width - j - 1] = img[:, j]

#d)
#resized_image = resize(img, (height/10, width/10))
#rescaled_image = 255 * resized_image
#final_image = rescaled_image.astype(np.uint8)

#e)
new_image = np.zeros((height, width))
for i in range(0, height):
    for j in range(0, width):
        if j >= (width/4) and j <= (2*width/4):
            new_image[i][j] = img[i][j]

plt.figure(1) 
plt.imshow(new_image, cmap='gray', vmin=0, vmax=255) 
plt.show()