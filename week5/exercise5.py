# template
import threading
import tkinter as tk
import winsound
import time
import numpy as np
from PIL import Image, ImageTk

ikkuna=tk.Tk()
ikkuna.title("Exercise 5")
ikkuna.geometry("700x700")
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

# -luo käyttöliittymään toiminto, joka havainnollistaa vasemmpaan reunaan aution saaren (island) ja toiseen reunaan asutun mantereen (continent)

#load island image
island_image=Image.open('island.png')
island_photo=ImageTk.PhotoImage(island_image)

#place island
island_kuva=tk.Label(ikkuna, image=island_photo)

def ins_island():
    island_kuva.place(x=0,y=50)

btn_island=tk.Button(ikkuna, text="Insert island", command=ins_island)
btn_island.place(x=50,y=600)

#load docks image
docks_image=Image.open('continent.png')
docks_photo=ImageTk.PhotoImage(docks_image)

#place docks
docks_kuva=tk.Label(ikkuna, image=docks_photo)

def ins_docks():
    docks_kuva.place(x=600,y=50)

btn_docks=tk.Button(ikkuna, text="Insert docks", command=ins_docks)
btn_docks.place(x=600,y=600)

#-luo toiminto, jolla Ernesti pystyy lähettämään apinan uimaan kohti manteretta saaren pohjoispäästä sadan pienen askelen verran (kuvaa jokaista uitua kilometriä) ja havainnollista tämän uinti käyttöliittymässä parhaaksi katsomallasi tavalla

#load monkey image
monkey_image=Image.open('monkey.png')
monkey_photo=ImageTk.PhotoImage(monkey_image)

#place monkey
monkey_kuva=tk.Label(ikkuna, image=monkey_photo, highlightthickness=0)

def swim(y_value, monkey_name):
    for i in range(100):
        monkey_kuva.place(x=100 + i * 5, y=y_value)
        #print("..swim...")
        winsound.Beep(440,100)
        time.sleep(0.100)

        if np.random.randint(0, 100) <= 0.5:
            print(f"shark is attacking {monkey_name}")
            winsound.Beep(1000, 100)
            return
        
    monkey_kuva.place(x=600, y=y_value)
    chosen_word = np.random.choice(emergency_msg)
    print(f"{monkey_name} reached the docks and says '{chosen_word}' ")
    winsound.Beep(800,500)

def create_and_send_one_monkey(y_value, monkey_name):
    monkey = Monkey(monkey_name)
    monkey.teach_word(emergency_msg)
    thread_something=threading.Thread(target=swim, args=(y_value, monkey_name))
    thread_something.start()

btn_monkey=tk.Button(ikkuna, text="Ernesti sends a monkey", command=lambda: create_and_send_one_monkey(100, "Ernesti's Monkey"))
btn_monkey.place(x=203,y=620)

#-luo vastaavasti toiminto, jolla  Kernesti pystyy myös lähettämään apinan uimaan kohti manteretta samalla tavalla kuin Ernestinkin, mutta saaren eteläpäästä

btn_monkey2=tk.Button(ikkuna, text="Kernesti sends a monkey",command=lambda: create_and_send_one_monkey(400, "Kernesti's Monkey"))
btn_monkey2.place(x=353,y=620)


#-kun nämä vaiheet on sujuvasti tehty, aja komento 
i_suppose_i_have_earned_so_much_points(1)

def send_10_monkeys():
    for i in range(10):
        create_and_send_one_monkey(100, f"Ernesti's Monkey {i+1} ")

def send_10_monkeys_k():
    for i in range(10):
        create_and_send_one_monkey(400, f"Kernesti's Monkey {i+1} ")
        
btn_10_monkeys_e=tk.Button(ikkuna, text="Eernesti sends 10 monkeys", command=send_10_monkeys)
btn_10_monkeys_e.place(x=203,y=655)

btn_10_monkeys_k=tk.Button(ikkuna, text="Kernesti sends 10 monkeys", command=send_10_monkeys_k)
btn_10_monkeys_k.place(x=353,y=655)


#do_several_tasks=tk.Button(ikkuna,text="Send many monkeys", command=several_tasks)
#do_several_tasks.place(x=300,y=650)

# -create a function that defines a monkey that has been taught one word from the emergency message created by Ernest and Kernest
class Monkey:
    def __init__(self, name) -> None:
        self.name = name
        self.taught_word = None
    
    def teach_word(self, word):
        self.taught_word = word

    def speak(self):
        if self.taught_word:
            print(f"{self.name} says: '{self.taught_word}' ")
        else:
            print(f"{self.name} doesnt know a word yet.")

# Initialize the emergency message as an array of words
emergency_msg = [
    "Ernesti!",
    "Kernesti",
    "Ovat",
    "Pulassa",
    "100km",
    "päässä",
    "sivilisaatiosta",
    "lähettäkää",
    "apua",
    "SOS"
]

i_suppose_i_have_earned_so_much_points(2)

#-create a function using threading, with which Ernesti can send a single monkey with him one word towards the continent. 
# Use a suitable sound signal to express swimming sounds at each "kilometer". 
#And, if the monkey gets there, indicate this with an appropriate sound signal.



i_suppose_i_have_earned_so_much_points(3)
ikkuna.mainloop()
