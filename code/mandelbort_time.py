# Mandelbort set BenchMark :
'''

This version is specifically to test the run time 
to execute Mandelbort Set.

'''

import numpy as np 
from PIL import Image
import timeit

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
The Benchmark will be done in 3 sets of values :
[Each set will be performed 5 times and the average will be considered.] 

Set : 1 :-  delta = 0.01       x_lim,y_lim = 400    [less than 2 seconds]

Set : 2 :-  delta = 0.0025    x_lim,y_lim = 1600    [less than 25 seconds]

Set : 3 :-  delta = 0.00125   x_lim,y_lim = 3200    [less than 85 seconds]

'''

delta = 0.0025
x_lim = 1600
y_lim = 1600

# Empty array :
set_arr = np.zeros(shape = (x_lim,y_lim))

real = -3


start = timeit.default_timer()
for i in range(x_lim): 
    img = -2
    for j in range(y_lim):

        c = complex(real,img)
        mandel = mandelbort(c)
        img += delta

        if mandel == 255 : 
            color = 0
        else : 
            color = mandel

        set_arr[i][j] = color


    real += delta

set_arr = set_arr.T
set_arr = np.array(set_arr,np.uint8)

data = Image.fromarray(set_arr) 
data.save('pil_out_time.png')

end = timeit.default_timer()

print('Execution Time : ',round((end-start),3),' seconds')

