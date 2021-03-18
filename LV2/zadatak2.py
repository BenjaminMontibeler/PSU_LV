import numpy as np 
import matplotlib.pyplot as plt
x = []
np.random.seed(56)
for brojbacanja in range(0, 100):
    brojbacanja = np.random.randint(low = 1, high = 7)
    x.append(brojbacanja)

b = np.array(x)
print(x)

his = np.histogram(b, bins=range(5))
fig, ax = plt.subplots()
offset = .6
plt.bar(his[1][1:],his[0])
ax.set_xticks(his[1][1:] + offset)
ax.set_xticklabels( ('1', '2', '3', '4', '5', '6') )

#n = 6
#bins=np.arange(0,n+2,1)
#a = np.arange(6)
#fig, ax = plt.subplots(1,1)
#ax.set_xticks(bins[:-1])
#ax.hist(b, bins =(6), rwidth=0.8, align = 'left')
#plt.hist(a, bins=range(min(a), max(a) + 1))
#ax.hist(a, bins=bins, align='left')
plt.ylim(ymin = 0, ymax = 100)
plt.xlim(xmin = 0, xmax = 7)
plt.title("Histogram")
plt.show()



