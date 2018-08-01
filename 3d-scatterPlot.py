import os
import sys
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#plt.style.use('ggplot')
#%matplotlib notebook #This is the magic line that can make your plots interactive


###########################
Multiple plots in the same figure
###########################
plt.figure(figsize = (10,6))
ax = plt.axes(projection='3d')
ax.view_init(elev = 0, azim = 30)
ax.scatter(xs=L1Score, ys=0, zs=L2Score, s = 2, alpha = 0.3, color = 'yellow')
ax.scatter(xs=0, ys=UCScore, zs=L2Score, s = 1, alpha = 0.1, color = 'green')
ax.scatter(xs=L1Score, ys=UCScore, zs=0, s = 1, alpha = 0.1, color = 'orange')

plt.xlabel("L1Score")
plt.ylabel("UCScore")
plt.show()


##############################
Plots with different elevation and azimuth
##############################
#Make a scatter plot
fig = plt.figure(figsize = (10,50))
angles = [0, 330, 300, 290, 280, 270]
for i, angle in enumerate(angles):
    subplotstring = "71"+str(i+1)
    ax = fig.add_subplot(subplotstring, projection = '3d')
    plt.xlabel("L1Score", fontsize = 14)
    plt.ylabel("UCScore", fontsize = 14)
    ax.set_zlabel("L2Score", fontsize = 14)
    ax.view_init(elev = 0,azim = angle)
    ax.scatter(L1, UC, L2, s = 1, alpha = 0.5, linewidths = 0, color = 'orange')
    
