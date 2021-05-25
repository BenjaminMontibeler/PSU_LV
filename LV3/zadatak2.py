import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.core.indexes.base import Index
mtcars = pd.read_csv('mtcars.csv')
#1
mtcars.groupby(['cyl']).mpg.mean().plot.bar(stacked=True, title='Potrosnja s obzirom na broj cilindara', ylabel='Potrosnja', xlabel='Broj cilindara')
plt.show()
#_____________________________________________________________________________________________________
#2
boxplot = mtcars.boxplot(by='cyl',column=['wt'])
plt.show()
#_____________________________________________________________________________________________________
#3
x_labels = ['Automatski', 'Rucni']
ax = mtcars.groupby(['am']).mpg.mean().plot.bar(stacked=True, title='Potrosnja s obzirom na mjenjac', ylabel='Potrosnja', xlabel='Mjenjac', rot=0)
ax.set_xticklabels(x_labels)
plt.show()
#_____________________________________________________________________________________________________
#4
automatic = mtcars[mtcars.am == 0]
manual = mtcars[mtcars.am == 1]
a = automatic[['hp','qsec']].to_numpy()
m= manual[['hp','qsec']].to_numpy()

fig = plt.figure()
ax2 = fig.add_axes([0.1,0.1,0.8,0.8])
axa_hp = ax2.scatter(a[:,1],a[:,0])
axm_hp = ax2.scatter(m[:,1],m[:,0])
ax2.legend(labels = ['Automatski','Rucni'])
ax2.set_title("Ubrzanje s obzirom na konjsku snagu")

plt.show()
