import matplotlib.pyplot as plt 
import numpy as np 

def slika(duljina_stranice, visina_br, sirina_br):
    array_black = np.ones((duljina_stranice, duljina_stranice))
    array_white = np.zeros((duljina_stranice, duljina_stranice))
    array_white.fill(255)
    for x in range(visina_br):
        if x == 0:
            array1 = array_white
        elif x % 2 == 0:
            array1 = np.concatenate((array1, array_white))
        else:
            array1 = np.concatenate((array1, array_black))

    array2 = array1

    for z in range(duljina_stranice):
        if array1[z][z] == 0:
            array2[z][z] == 1
        else:
            array2 == 0

    for y in range(sirina_br):
        if y == 0:
            array = array1
        elif y % 2 == 0:
            array2 = np.concatenate((array, array1), axis = 1)
        else:
            array2 = np.concatenate((array, array2), axis = 1)

    
    return array

a = input("Unesite duljinu stranice kvadrata: ")
br_visina = input("Unesite broj kvadrata po visini: ")
br_sirina = input("Unesite broj kvadrata po sirini: ")
a = int(a)
br_visina = int(br_visina)
br_sirina = int(br_sirina)

img = slika(a, br_visina, br_sirina)
#array_black = np.ones((a, a))
#array_white = np.zeros((a, a))

print(img)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()