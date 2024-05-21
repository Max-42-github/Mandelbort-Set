~~~ THIS FILE CONTAINS DESCRIPTION OF EACH FILE IN THIS REPOSITORY ~~~


" mandel_array.npy " : 
	
	This is binary file containing a NumPy array of Mandelbort Data. The NumPy array contains the pixel value to form an image of Mandelbort Set. Here each element in the 2D array contains encodes data for a Black and White Image, with each element having a value between (0 -> 255). The Data in this file is generated with resolution of 400 x 400 with Delta (interval) of 0.01. [The actual datafile could not be uploaded in GitHub due to GitHub data limit.]


" mandelbort_data_generate.py " :

	This Python Script generates the NumPy array based on the parameters [ ' x_lim ', ' y_lim ', ' delta ']. Output is a binary file containing the array.


" mandel_data_to_img.py " : 

	This Python Script uses the data file containing the array and produces an image of the Mandelbort Set using the PIL library.


" pil_out_4.png " and " pil_out_final.png " : 

	These are sample output generated of the Mandelbort Set. This is a high resoltuion image of Mandelbort set of resolution 16000 x 16000 with data generated with interval of 0.00025


" mandelbort_time.py " : 

	This is a 'fun little' python script. It is designed as a benchmark test ~_~ which can generate mandelbort data and create an img of it. All this process is also timed by the program, and outputs the time taken by the machine to complete the task. The 'benchmark' test can be changed using the parametes in the code [ ' x_lim ', ' y_lim ', ' delta '].
Module required to run this test : (1) numpy, (2) PIL (pillow), (3) timeit.
