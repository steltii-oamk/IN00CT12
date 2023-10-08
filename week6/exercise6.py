# template
import winsound
import time
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ikkuna=tk.Tk()
ikkuna.title("Exercise 6")
# add five buttons to the top line of the window
koristetta=tk.Label(ikkuna,text="").grid(row=0,column=0)
point_button=[]
for i in range(5):
    button_temp=tk.Button(ikkuna,text="Points: "+str(i+1),padx=40)
    button_temp.grid(row=0,column=i+1)
    point_button.append(button_temp)
def i_suppose_i_have_earned_so_much_points(amount_of_points):
    for i in range(5):
        point_button[i].configure(bg='gray')
    time.sleep(1)    
    for i in range(amount_of_points):
        point_button[i].configure(bg='green')
        winsound.Beep(440+i*100,500)
# example ...

# Create a Matplotlib figure and subplot
fig, ax = plt.subplots(figsize=(8, 6))

# Define the island size
island_size = (260, 220)

# Draw the blue ocean
ax.add_patch(plt.Rectangle((0, 0), island_size[0] + 100, island_size[1] + 100, color='blue'))

# Draw the deserted island
ax.add_patch(plt.Rectangle((50, 50), island_size[0], island_size[1], color='sandybrown'))

# Draw the pool
pool_size = (60, 20)
ax.add_patch(plt.Rectangle((150, 150), pool_size[0], pool_size[1] ,color='peru'))

# Draw the ditches connecting the sea to the pool
ditch_width = 100
ditch_length = 1
ditch_y = (island_size[1] - pool_size[1]) / 2

# Add left side ditch
ax.add_patch(plt.Rectangle((160, 50), ditch_length, ditch_width, color='peru'))

# Add right side ditch
ax.add_patch(plt.Rectangle((200, 50), ditch_length, ditch_width, color='peru'))

# Set axis limits
ax.set_xlim(0, island_size[0] + 100)
ax.set_ylim(0, island_size[1] + 100)

# Create a canvas to display the figure
canvas = FigureCanvasTkAgg(fig, master=ikkuna)
canvas.get_tk_widget().grid(row=2,column=0)

i_suppose_i_have_earned_so_much_points(1)

# Run the Tkinter main loop
ikkuna.mainloop()
