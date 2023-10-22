# Video link on youtube
# https://youtu.be/oq0rIOVTB2A


# template
import tkinter as tk
import winsound
import time
import random
import threading

ikkuna=tk.Tk()
ikkuna.title("Exercise 8")
ikkuna.geometry("700x700")
ikkuna.configure(bg="CornflowerBlue")
# Disable window resizing
ikkuna.resizable(False, False)
# add five buttons to the top line of the window
koristetta=tk.Label(ikkuna,text="").grid(row=0,column=0)
point_button=[]
for i in range(5):
    button_temp=tk.Button(ikkuna,text="Points: "+str(5*(i)),padx=40)
    button_temp.grid(row=0,column=i+1)
    point_button.append(button_temp)
def i_suppose_i_have_earned_so_much_points(amount_of_points):
    points_mod=int(amount_of_points/5)
    for i in range(5):
        point_button[i].configure(bg='gray')
    time.sleep(1) 
    point_button[0].configure(bg='green')   
    for i in range(points_mod):
        point_button[i+1].configure(bg='green')
        winsound.Beep(440+i*100,500)

# Example:
i_suppose_i_have_earned_so_much_points(0)

monkey_items = [] # Store monkey canvas items
play_monkey_sounds_flag = True # Flag to control monkey sounds

# Define islands size and collision range
island_x = 60
island_y = 60
island_collision_x = island_x + 20
island_collision_y = island_y + 20
monkey_x=0
monkey_y=0

# Add each monkey
def add_monkey(x, y):
    monkey = tk.Canvas(ikkuna, width=monkey_x, height=monkey_y, bg="brown", highlightbackground="brown")
    monkey.place(x=x, y=y)
    monkey_items.append(monkey)
    # Play a sound for the monkey
    frequency = random.randint(200, 1000)
    winsound.Beep(frequency, 200)

# Define monkey sound every 10 second
def play_monkey_sounds():
    while play_monkey_sounds_flag:
        time.sleep(10)
        for monkey in monkey_items:
            frequency = random.randint(200,1000)
            winsound.Beep(frequency, 200)

# Start monkey sounds
def start_monkey_sounds():
    global play_monkey_sounds_flag
    play_monkey_sounds_flag = True
    monkey_sound_thread = threading.Thread(target=play_monkey_sounds)
    monkey_sound_thread.daemon = True
    monkey_sound_thread.start()

# Stop monkey sounds
def stop_monkey_sounds():
    global play_monkey_sounds_flag
    play_monkey_sounds_flag = False

# Insert a new island
def new_island():
    start_monkey_sounds()
    island = tk.Canvas(ikkuna, width=island_x, height=island_y, bg="sandybrown", highlightbackground="sandybrown")
    while True:
        isl_place_x = random.randint(50, 700-island_collision_x)  # Random x-coordinate within the window
        isl_place_y = random.randint(50, 650-island_collision_y)  # Random y-coordinate within the window
        collision = False
        for widget in ikkuna.winfo_children():
            if isinstance(widget, tk.Canvas):
                widget_x = widget.winfo_x()
                widget_y = widget.winfo_y()
                if isl_place_x < widget_x + island_collision_x and isl_place_x + island_collision_x > widget_x and isl_place_y < widget_y + island_collision_y and isl_place_y + island_collision_y > widget_y:
                    collision = True
                    break
        if not collision:
            island.place(x=isl_place_x, y=isl_place_y)
            for _ in range(10):
                monkey_x = random.randint(isl_place_x + 5, isl_place_x + island_x - 5)
                monkey_y = random.randint(isl_place_y + 5, isl_place_y + island_y - 5)
                add_monkey(monkey_x, monkey_y)
            break

# Start threading on new island    
def island_thread():
    thread_islands = threading.Thread(target=new_island)
    thread_islands.start()

# Remove all islands and monkey sounds
def remove_islands():
    for widget in ikkuna.winfo_children():
        if isinstance(widget, tk.Canvas):
            widget.destroy()
    stop_monkey_sounds()
    i_suppose_i_have_earned_so_much_points(5)

# Add buttons
btn_new_island=tk.Button(ikkuna,text="New island", command=island_thread, padx=5, pady=5)
btn_new_island.place(x=25,y=650)

btn_rmv_island=tk.Button(ikkuna,text="Remove islands", command=remove_islands, padx=5, pady=5)
btn_rmv_island.place(x=110,y=650)


ikkuna.mainloop()
