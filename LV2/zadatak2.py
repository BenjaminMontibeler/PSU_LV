import numpy as np 
import matplotlib.pyplot as plt
x = []
np.random.seed(562)
for brojbacanja in range(0, 100):
    brojbacanja = np.random.randint(low = 1, high = 7)
    x.append(brojbacanja)

hist,bin_edges = np.histogram(x)

plt.figure(figsize=[10,8])
bin_edges = np.round(bin_edges,0)

plt.bar(bin_edges[:-1], hist, width = 0.5, color='#0504aa',alpha=0.7)
plt.xlim(min(bin_edges), max(bin_edges))
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Number',fontsize=15)
plt.ylabel('Frequency',fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.ylim(ymin = 0, ymax = 100)
plt.xlim(xmin = 0, xmax = 7)
plt.ylabel('Frequency',fontsize=15)
plt.title('Histogram',fontsize=15)
plt.show()