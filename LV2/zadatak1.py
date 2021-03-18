import numpy as np 
import matplotlib.pyplot as plt
plt.axis([0, 4, 0, 4])
x = np.array([1, 3, 3, 2, 1])
y = np.array([1, 1, 2, 2, 1])
#plt.axis([1,1])
plt.title("cetverokut")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y, '-', linewidth=2, markersize=12)


plt.show()