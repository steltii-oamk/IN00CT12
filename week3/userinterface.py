#UI with tkinter
#Interface between the computer and you

import tkinter
import winsound
from PIL import Image, ImageTk

sound_dur=750

#Create a window
ikkuna=tkinter.Tk()

ikkuna.title("Ernesti and Kernesti adventure continue...")

#Configuration
ikkuna.geometry("600x600")

erne_image=Image.open('erne.png')
erne_photo=ImageTk.PhotoImage(erne_image)

#Content about the UI here
#****************************
def do_that_thing():
    print("Now we play a sound...")
    kuva_erne.place(x=100,y=100)
    winsound.Beep(200, sound_dur)

def do_another_thing():
    print("Now we play a different sound...")
    kuva_erne.place(x=300,y=100)
    winsound.PlaySound("taputukset.wav", winsound.SND_FILENAME)

painike=tkinter.Button(ikkuna, text="Press me!",command=do_that_thing)
painike.grid(row=0, column=0)

painike2=tkinter.Button(ikkuna, text="Don't press me!",command=do_another_thing)
painike2.grid(row=0, column=1)

teksti=tkinter.Label(ikkuna, text="Heipä hei!")
teksti.grid(row=3, column=5)

kuva_erne=tkinter.Label(ikkuna, image=erne_photo)
kuva_erne.place(x=200,y=200)

#****************************

#Always this at the end:
ikkuna.mainloop()