# template
import threading
import tkinter as tk
import winsound
import time
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

def swim(y_value):
    for i in range(100):
        monkey_kuva.place(x=100+i*5,y=y_value)
        print("..swim...")
        winsound.Beep(440,100)
        time.sleep(0.100)

def create_and_send_one_monkey(y_value):
    thread_something=threading.Thread(target=swim, args=(y_value))
    thread_something.start()

btn_monkey=tk.Button(ikkuna, text="Ernesti sends a monkey", command=lambda: create_and_send_one_monkey(100))
btn_monkey.place(x=300,y=100)

#-luo vastaavasti toiminto, jolla  Kernesti pystyy myös lähettämään apinan uimaan kohti manteretta samalla tavalla kuin Ernestinkin, mutta saaren eteläpäästä

btn_monkey2=tk.Button(ikkuna, text="Kernesti sends a monkey",command=lambda: create_and_send_one_monkey(300))
btn_monkey2.place(x=300,y=500)

#-kun nämä vaiheet on sujuvasti tehty, aja komento i_suppose_i_have_earned_so_much_points(1)

#def several_tasks():
    #for i in range(10):
     #   create_and_send_one_monkey()
    #    print("several..threads....going on...")

#do_several_tasks=tk.Button(ikkuna,text="Send many monkeys", command=several_tasks)
#do_several_tasks.place(x=300,y=650)



i_suppose_i_have_earned_so_much_points(3)
ikkuna.mainloop()
