# Mandelbort set visualization : 
'''
Update from last version 'mandelbort_2.py' : 

1. It also generates an output array.
2. Drastic change in data content of the array, with improved color scheme.

'''


import numpy as np 
from PIL import Image

'''
Fine Tuneing parameters : 

1. delta
2. max_itteration

'''

# Function with working formula
def mandelbort(c):
    z = 0
    max_itteration = 255
    mod = abs(c)
    for i in range(1,max_itteration+1):
        if mod >= 2:
            return i
        z = (z**2)+c
        mod = abs(z)
        
    return i

# Increment of c with each itteration : 
'''
Good set of value : 

1. delta = 0.01     x_lim,y_lim = 400

2. delta = 0.001    x_lim,y_lim = 4000

'''
delta = 0.01
x_lim = 400
y_lim = 400

# Empty array :
set_arr = np.zeros(shape = (x_lim,y_lim))


real = -3

for i in range(x_lim): 
    img = -2
    for j in range(y_lim):

        c = complex(real,img)
        mandel = mandelbort(c)
        img += delta

        #color = 255 - int(mandel * 255/255)

        if mandel == 255 : 
            color = 0
        else : 
            color = mandel

        set_arr[i][j] = color


        

    real += delta

np.save('mandel_array',set_arr)
