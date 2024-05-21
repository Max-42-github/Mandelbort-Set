~~~ THIS FILE CONTAINS DESCRIPTION OF EACH FILE IN THIS REPOSITORY ~~~


" mandel_array.npy " : 
	
	This is binary file containing a NumPy array of Mandelbort Data. The NumPy array contains the pixel value to form an image of Mandelbort Set. Here each element in the 2D array contains encodes data for a Black and White Image, with each element having a value between (0 -> 255). The Data in this file is generated with resolution of 4000 x 4000 with Delta (interval) of 0.00025.


" mandelbort_data_generate.py " :

	This Python Script generates the NumPy array based on the parameters [ ' x_lim ', ' y_lim ', ' delta ']. Output is a binary file containing the array.


" mandel_data_to_img.py " : 

	This Python Script uses the data file containing the array and produces an image of the Mandelbort Set using the PIL library.


" pil_out_4.png " and " pil_out_final.png " : 

	These are sample output generated of the Mandelbort Set. This is high resolution img of Mandelbort