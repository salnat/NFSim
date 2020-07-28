# NFSim Documentation

Neurofeedback Simulator for sagol's hackathon.

Functions used

##NF_instance
	NF_instance(parameter1,parameter2)
	
       		
	this function will recieve the two parameters and control the blurring and size of image accorting to them.
	
   	Parameters
    	----------
    	parameter 1:int
        	First Neurofeedback parameter.
    	parameter 2: int
        	Second Neurofeedback parameter.
    	Returns
    	-------
        size: image size tuple.
	data: image.tobytes() array
	mode: image mode, integer.


##main
	main(parameter1,parameter2)
	parameter1,parameter2: integers
       		
	this function will recieve the two parameters and control the blurring and size of image accorting to them.
        while integrating this change in the image into a pygame window.

	Parameters
    	----------
    	parameter 1:int
        	First Neurofeedback parameter.
    	parameter 2: int
        	Second Neurofeedback parameter.
##load_mat_data
	load_mat_data(mat_data:str)

	this function will load the .mat files used to simulate the eeg signals from patient.
##dict_2_np
	dict_2_np(mat_dict:dict)

	this function will convert the mat dictionary to numpy array
##streamer_func 

	streamer_func (datout_file:str, lenout_file:str, folder_path=Path().absolute()):
	This function receives two parameters from the EEG Neurofeedback system (Curry7) 
    	in Matlab formt and stream it to python. The function pushes the Matlab data to a papline based 
   	on streamz library.

   	Parameters
    	----------
    	datout_file:str
        	First Neurofeedback parameter vector file name.
    	lenout_file:str
        	Second Neurofeedback parameter vector file name.
    	path: pathlib path
        	Pathlib path to the folder with the data.    

    Returns
    -------
    The function displays the online visual interface.


	this function will load the .mat files used to simulate the eeg signals from patient.




