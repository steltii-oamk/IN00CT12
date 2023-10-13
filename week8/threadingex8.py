import tkinter as tk
import time
import threading
import pygame
import numpy as np
import psutil
import winsound
 
# Tässä mahdollisesti ideoita harjoitus n:o 8:lle ... 
#
 
pygame.init()
painike_aani=pygame.mixer.Sound("klik.wav")
 
def soita_painike_aani():
    pygame.mixer.Sound.play(painike_aani)
 
ikkuna=tk.Tk()
ikkuna.title("Threading...")
#icon=tk.PhotoImage(file="d.png")
#ikkuna.iconphoto(False,icon)
ikkuna.geometry("400x270")
 
teksti={}
for i in range(4):
    for j in range(10):
        teksti[j,i]=tk.Label(ikkuna,text="-",bg='green')
        teksti[j,i].grid(row=j,column=i)
 
#Huomaa - luodaan globaali muuttuja jota säikeet voivat työstää...
koko_ohjelman_yhteinen_muuttuja=0
# ... tässä oli vain yksi muuttuja, mutta voi olla laajempikin ... useita muuttujia, dictionary, jne...
 
naytolle_yhteinen_muisti_muuttuja=tk.StringVar()
pysaytys_lippu=False
alaosien_pysaytys_lippu=False
 
#luodaan semafori ... joskus tarpeen ... mahdolliset kriittiset prosessivaiheet ... 
semafori=threading.Semaphore(1) #1 tarkoittaa että vain yksi säie voi käyttää kerrallaan
semafori_tupla=threading.Semaphore(2) #2 tarkoittaa että kaksi säiettä voi käyttää kerrallaan
#...jne...!!!
 
def paivita_yhteiset_muuttujat_rutiini():
    global koko_ohjelman_yhteinen_muuttuja,pysaytys_lippu
    while pysaytys_lippu==False:    
        naytolle_yhteinen_muisti_muuttuja.set(koko_ohjelman_yhteinen_muuttuja)
        time.sleep(0.1)
        #tsekataan missä ovat samat arvot:
        for i in range(4):
            for j in range(10):
                if teksti[j,i]['text']==koko_ohjelman_yhteinen_muuttuja:
                    teksti[j,i].config(bg='red')
                    time.sleep(0.2)
                    teksti[j,i].config(bg='green')
    #loopin jälkeen informoidaan että homma on ohi
    print("Pysäytetään päivittäjä...")
                    
 
#tehdään eräänlainen "yhteinen muistipaikka kaikille..."
yhteinen_muisti=tk.Label(ikkuna,textvariable=naytolle_yhteinen_muisti_muuttuja,bg='yellow')
yhteinen_muisti.grid(row=11,columnspan=4,sticky="nsew")
 
def aarne_tyo():
    global koko_ohjelman_yhteinen_muuttuja,alaosien_pysaytys_lippu
    print("kops kops...")
    for j in range(10):
        if alaosien_pysaytys_lippu==True:
            print("Aarne pysäytettiin")
            break   
        aarne_muuttuja=np.random.randint(0,100)
        teksti[j,0].config(text="-"+str(aarne_muuttuja)+"-")
        winsound.Beep(440,100)
        time.sleep(0.2)
        #SEMAFORI-operaatio:
        semafori.acquire()
        koko_ohjelman_yhteinen_muuttuja=aarne_muuttuja
        semafori.release()
        teksti[j,0].config(text=aarne_muuttuja)
        time.sleep(1)
    pygame.mixer.Sound.play(painike_aani)
    print("CPU: ",psutil.cpu_percent(), "%")
 
def bertta_tyo():
    global koko_ohjelman_yhteinen_muuttuja,alaosien_pysaytys_lippu
    print("kops kops...")
    for j in range(10):
        if alaosien_pysaytys_lippu==True:
            print("Bertta pysäytettiin")
            break   
        bertta_muuttuja=np.random.randint(0,100)
        teksti[j,1].config(text="-"+str(bertta_muuttuja)+"-")
        winsound.Beep(2*440,100)
        time.sleep(0.2)
        #SEMAFORI-operaatio:
        semafori.acquire()
        koko_ohjelman_yhteinen_muuttuja=bertta_muuttuja
        semafori.release()
        teksti[j,1].config(text=bertta_muuttuja)
        time.sleep(1)
    pygame.mixer.Sound.play(painike_aani)    
    print("CPU: ",psutil.cpu_percent(), "%")
 
def cecilia_tyo():
    global koko_ohjelman_yhteinen_muuttuja,alaosien_pysaytys_lippu
    print("kops kops...")
    for j in range(10):
        if alaosien_pysaytys_lippu==True:
            print("Cecilia pysäytettiin")
            break   
        cecilia_muuttuja=np.random.randint(0,100)
        teksti[j,2].config(text="-"+str(cecilia_muuttuja)+"-")
        winsound.Beep(3*440,100)
        time.sleep(0.2)
        #SEMAFORI-operaatio:
        semafori.acquire()
        koko_ohjelman_yhteinen_muuttuja=cecilia_muuttuja
        semafori.release()
        teksti[j,2].config(text=cecilia_muuttuja)
        time.sleep(1)    
    pygame.mixer.Sound.play(painike_aani)
    print("CPU: ",psutil.cpu_percent(), "%")
 
def daavid_tyo():
    global koko_ohjelman_yhteinen_muuttuja,alaosien_pysaytys_lippu
    print("kops kops...")
    for j in range(10):
        if alaosien_pysaytys_lippu==True:
            print("Daavid pysäytettiin")
            break   
        daavid_muuttuja=np.random.randint(0,100)
        teksti[j,3].config(text="-"+str(daavid_muuttuja)+"-")
        winsound.Beep(4*440,100)
        time.sleep(0.2)
        #SEMAFORI-operaatio:
        semafori.acquire()
        koko_ohjelman_yhteinen_muuttuja=daavid_muuttuja
        semafori.release()
        teksti[j,3].config(text=daavid_muuttuja)
        time.sleep(1)  
    pygame.mixer.Sound.play(painike_aani)
    print("CPU: ",psutil.cpu_percent(), "%")
 
#Säikeiden aloitukset:
 
def aloita_saie_aarne():
    t=threading.Thread(target=aarne_tyo)
    t.start()
 
def aloita_saie_bertta():
    t=threading.Thread(target=bertta_tyo)
    t.start()
 
def aloita_saie_cecilia():
    t=threading.Thread(target=cecilia_tyo)
    t.start()
 
def aloita_saie_daavid():
    t=threading.Thread(target=daavid_tyo)
    t.start()
 
def paivita_yhteiset_muuttujat():
    #Huomaa että tässä daemonin käyttö mahdollistaa säikeen lopetuksen kun ohjelma lopetetaan, tärkeä käytännön juttu!!!
    t=threading.Thread(target=paivita_yhteiset_muuttujat_rutiini,daemon=True)
    t.start()
 
#pakotetaan yhteisen muuttujan päivitys käyntiin...aina aloituksessa
paivita_yhteiset_muuttujat()
 
painike_a=tk.Button(text='Aarne',command=aloita_saie_aarne)
painike_a.grid(row=10,column=0,pady=3)
 
painike_b=tk.Button(text='Bertta',command=aloita_saie_bertta)
painike_b.grid(row=10,column=1,pady=3)
 
painike_c=tk.Button(text='Cecilia',command=aloita_saie_cecilia)
painike_c.grid(row=10,column=2,pady=3)
 
painike_d=tk.Button(text='Daavid',command=aloita_saie_daavid)
painike_d.grid(row=10,column=3,pady=3)
 
#Huom! Tämä on kätevä konsti tkinteriä luodessa ... voi säätää ulkoasun
#kohdalleen yritä ja erehdy-periaatteella...
#ikkuna.after(2000,ikkuna.destroy)
 
ikkuna.mainloop()