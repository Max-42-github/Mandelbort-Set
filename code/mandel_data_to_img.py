import numpy as np  
from PIL import Image


mandel_array = (np.load('mandel_array.npy')).T
mandel_array = np.array(mandel_array,np.uint8)
data = Image.fromarray(mandel_array) 
      
data.save('pil_out_4.png')