import numpy as np
import matplotlib.pyplot as plt

M=np.ones((10,10))

def eat_pie(pie_to_eat,how_big_slice):
    ##
    M[0,0]=0
    return M

M_eaten=eat_pie(M,2)

plt.matshow(M_eaten)
plt.show()