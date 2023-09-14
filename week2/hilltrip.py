#Import required libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

rows = 10
columns = 10

#blueberry pie
bb_pie = np.zeros((rows,columns))
bb_pie[1::2,::2] = 1
bb_pie[::2,1::2] = 1

#lingonberry pie
lb_pie = np.zeros((rows,columns))
lb_pie[::3,::3] = 2

#cmap color profile for blueberry pie
bb_colors = ['#ba9345', '#4f0261']
cmap_bb = plt.matplotlib.colors.ListedColormap(bb_colors)

#cmap color profile for lingonberry pie
lb_colors = ['#ba9345', '#820933']
cmap_lb = plt.matplotlib.colors.ListedColormap(lb_colors)

plt.ion()
plt.matshow(bb_pie, cmap=cmap_bb)
plt.title("Ernesti's blueberry pie")
plt.matshow(lb_pie, cmap=cmap_lb)
plt.title("Kernesti's lingonberry pie")
plt.show()
plt.pause(5000)
