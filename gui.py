import numpy as np
from pathlib import Path
from mat4py import loadmat
from streamz import Stream
import pandas as pd
import os.path
import pygame
from PIL import Image,ImageFilter
import time
import sys
def open_im(filename):#opens the image 
    try:
        OriImage = Image.open(filename)
    except FileNotFoundError:
        print('Imgae file not Found in directory')
    return OriImage

def NF_instance(parameter_blur,parameter_size):
    """
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

    """
    boxImage = OriImage.filter(ImageFilter.BoxBlur(parameter_blur))
    resizedImage = boxImage.resize([int(parameter_size*s) for s in boxImage.size])
    mode = resizedImage.mode
    data = resizedImage.tobytes()
    size = resizedImage.size
    return data,size,mode
OriImage = open_im('im2.jpg')
pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption('Neurofeedback Training')
icon = pygame.image.load('brain.png')
pygame.display.set_icon(icon)
screen.fill((250,250,250))
pygame.display.update()
image = pygame.image.load(r'im2.jpg') #should be an image loaded in the same file of the script or an image address
screen.blit(image,(100,40)) 
pygame.display.update()

def main(parameter_blur, parameter_size):#updates the gui with the current image using NF_instance
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit(0)
    data,size,mode = NF_instance(parameter_blur,parameter_size)
    resed = pygame.image.fromstring(data,size,mode)
    res_rec = resed.get_rect(center = screen.get_rect().center)
    screen.fill((250,250,250))
    pygame.display.update()
    screen.blit(resed,res_rec)#update gui with current image
    pygame.display.update()
    time.sleep(0.1)



def load_mat_data(mat_data:str): # This function loads MATLAB data to Python dictionary 
    try:
        py_data = loadmat(mat_data)
    except FileNotFoundError:
        print(f'There is no {mat_data}.mat file in the directory ')
    return py_data

def dict_2_np(mat_dict:dict): # This function converts dictionary data to numpy array 
    np_data=np.array(list(mat_dict.values()))
    return np_data


def data_giver(data_array:np): # This function uploads nuerofeedbak parametars to the visual interface 
    for column in data_array.T:

        main(column[0],column[1]) # Call for the visual interface function
        time.sleep( 1) # Data samplig rate

def streamer_func (datout_file:str, lenout_file:str, folder_path=Path().absolute()):
    """This function receives two parameters from the EEG Neurofeedback system (Curry7) 
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
    """
    datout_source = Stream()
    a=datout_source.map(lambda x: x[0]).map(load_mat_data).map(dict_2_np)
    b=datout_source.map(lambda x: x[1]).map(load_mat_data).map(dict_2_np)


    c = a.zip(b).map(np.concatenate).sink(data_giver)

    datout_source.emit((datout_file, lenout_file))



streamer_func('datout.mat', 'lenout.mat')
