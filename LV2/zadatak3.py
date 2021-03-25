import numpy as np 
import matplotlib.pyplot as plt

data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)
 
mpg = []
hp = []
wt = []
cyl = []

mpg2 = []
hp2 = []

for i in range(len(data)):
    for j in range(len(data)):
        if j == 0:
            mpg.append(data[i, j])
        if j == 3:
            hp.append(data[i, j])
        if j == 5:
            wt.append(data[i, j]*6)
        #e)
        if j == 1:
            if data[i, j] == 6:
                mpg2.append(data[i, 0])
                hp2.append(data[i, 3])
                
print(mpg2)
print(hp2)
print("Max: ", max(mpg))
print("Min: ", min(mpg))
print("Average: ", (sum(mpg)/len(mpg)))

plt.scatter(mpg, hp, s = wt)
plt.ylim(ymin = 0, ymax = 400)
plt.xlim(xmin = 0, xmax = 40)
plt.show()

#e)
#plt.scatter(mpg2, hp2)
#plt.ylim(ymin = 0, ymax = 400)
#plt.xlim(xmin = 0, xmax = 40)
#plt.show()
