import matplotlib.pyplot as plt 
import numpy as np 
import skimage.io
 
img = skimage.io.imread('tiger.png', as_gray=True)
height, width = img.shape
matrica = np.ones((640, 960)) * 150
img = img + matrica
for i in range(0, height):
    for j in range(0, width):
        if img[i][j] > 255:
            img[i][j] = 255

img90 = np.zeros((width, height))
for j in range(0, height):
    img90[:, height - j - 1] = img[j, :]

#[:, 1] stupac
#[1, :] redak

plt.figure(1) 
plt.imshow(img90, cmap='gray', vmin=0, vmax=255) 
plt.show()