import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
mtcars = pd.read_csv('mtcars.csv')
#1
print("5 automobila s najvecom potrosnjom: \n")
print(mtcars.sort_values(['mpg']).head(5))
#2
print("\n3 automobila s 8 cilindara s najmanjom potrošnjom: \n")
print(mtcars[mtcars.cyl == 8].sort_values('mpg').tail(3))
#3
print("\nsrednja potrošnja automobila sa 6 cilindara: \n")
print(mtcars[mtcars.cyl == 6].mpg.mean())
#4
print("\nsrednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs: \n")
print(mtcars[(mtcars.cyl == 4) & (mtcars.wt <= 2.2) & (mtcars.wt >= 2)].mpg.mean())
#5
print("\nRucni mjenjac: ")
print(len(mtcars[mtcars.am == 1]))
print("\nAutomatski mjenjac: \n")
print(len(mtcars[mtcars.am == 0]))
#6
print("\nbroj autommobila s automatskimm mjenjacem i snagom preko 100 konjskih snaga: \n")
print(len(mtcars[(mtcars.am == 0) & (mtcars.hp > 100)]))
#7
print("\nMasa svakog automobila u kg\n")
print(mtcars['wt']*1000*0.45359237)