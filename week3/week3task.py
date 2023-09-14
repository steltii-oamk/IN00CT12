import tkinter
import winsound
import numpy as np
from PIL import Image, ImageTk

window=tkinter.Tk()
window.title("Kernesti's tomato throwing")

#random place for kernesti
kernesti_place_r = np.random.randint(50,350)

#Configuration
window.geometry("1300x650")

kernesti_image=Image.open('kernesti.png')
kernesti_photo=ImageTk.PhotoImage(kernesti_image)
target_image=Image.open('maalitaulu.png')
target_photo=ImageTk.PhotoImage(target_image)
tomato_image=Image.open('tomaatti.png')
tomato_photo=ImageTk.PhotoImage(tomato_image)

#functions
def move_kernesti():
    r = np.random.randint(50,350)
    kernesti_kuva.place(x=0,y=r)

def throw_tomato():
    tomaatti_kuva=tkinter.Label(window, image=tomato_photo)
    tomaatti_kuva.place(x=100,y=kernesti_place_r)

#place kernesti in random place on the left
kernesti_kuva=tkinter.Label(window, image=kernesti_photo)
kernesti_kuva.place(x=0,y=kernesti_place_r)

#target at a locked place on the right
maali_kuva=tkinter.Label(window, image=target_photo)
maali_kuva.place(x=500,y=0)

#buttons
kernesti_nappi=tkinter.Button(window, text="Move kernesti", command=move_kernesti)
kernesti_nappi.grid(row=0, column=0)

tomaatti_nappi=tkinter.Button(window, text="Throw tomato", command=throw_tomato)
tomaatti_nappi.grid(row=1, column=0)

#mainloop always at the end
window.mainloop()