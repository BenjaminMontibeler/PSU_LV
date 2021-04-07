import matplotlib.pyplot as plt 
import numpy as np 

a = input("Unesite duljinu stranice kvadrata: ")
br_visina = input("Unesite broj kvadrata po visini: ")
br_sirina = input("Unesite broj kvadrata po sirini: ")
a = int(a)
br_visina = int(br_visina)
br_sirina = int(br_sirina)

array_black = np.ones((a, a))
array_white = np.zeros((a, a))

print(img)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()