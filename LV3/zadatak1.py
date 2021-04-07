import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
mtcars = pd.read_csv('mtcars.csv')
#1
print(mtcars.sort_values(['mpg']).head(5))
#2
print(mtcars[mtcars.cyl == 8].sort_values('mpg').tail(3))
#3
print(mtcars[mtcars.cyl == 6].mpg.mean())
#4
print()