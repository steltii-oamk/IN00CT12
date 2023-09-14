#Import required libraries
import numpy as np
import matplotlib.pyplot as plt
import time
import random
import winsound

#Create space
matrix = np.zeros((100,100))

#Define data for Ernesti and Kernesti
E_data={}
E_data['x']=20
E_data['y']=99

K_data={}
K_data['x']=60
K_data['y']=99

M_data={}
M_data['x']=50
M_data['y']=5

print("it works until here")

#Lets put everything on the space
matrix[E_data['y'],E_data['x']]=1
matrix[K_data['y'],K_data['x']]=1
matrix[M_data['y'],M_data['x']]=1

plt.ion()
plt.matshow(matrix, cmap='winter_r')
plt.text(20,99,'Ernesti')
plt.text(60,99,'Kernesti')
plt.text(50,5,'Moon')
plt.show()
plt.pause(5)

for i in range(10, -1, -1):
    print("Countdown: ", i)
    winsound.Beep(2500,500)
    time.sleep(0.5)

# Launch failure of 1%
if random.randint(1, 100) <= 1:
    print("Rockets failed to launch")
else:
    print("Rockets succesfully launched")

winsound.Beep(300,15000)
winsound.Beep(1000,15000)