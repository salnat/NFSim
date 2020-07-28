# __NeuroFeedback Simulator for Prof Tami Bar Shalita's lab__

This repositry contains a python gui that simulates the work of An EEG based neurofeedback training
where it simulates a stream of data from the EEG recording electrodes that alters the state of 
a picture; blurring and size.
In a real Neurofeedback session, the patient would try to make the picture clearer and bigger by concentrating and 
"controling" his brain activity.

# __What is Neurofeedback__ ?

Neurofeedback, also called neurotherapy or neurobiofeedback, is a type of biofeedback that uses real-time displays of brain activity—most commonly electroencephalography (EEG)—in an attempt to teach self-regulation of brain function. Typically, sensors are placed on the scalp to measure electrical activity, with measurements displayed using video displays or sound. It is mostly known as a complementary and alternative treatment of many brain dysfunctions. [Read More](https://brainworksneurotherapy.com/what-is-neurofeedback) 

# __Installation__
You can install the Neurofeedback simulator via : pip install NFSim
# Environments and libraries 
The current package is supported by the following main libraries:

Package           Version
----------------- -------------------
mat4py            0.4.3 

numpy             1.19.1

pandas            1.0.5

Pillow            7.2.0

pygame            1.9.6

streamz           0.5.4

time-window       0.1.0

The extended list could be found in the end of the document.
# __Lisence__
This project is lisenced under MIT lisence

# Functions

#  NF_instance

The NF_instance function nested in the pygame game loop, where in each iteration (which is a simulation of data sampling from EEG) it recieves two parameters (which should be to parameters extracted from EEG data in real time)
and manipulates an image according to those parameters, one parameter affects the blurring of the image and the other one it's size.
# streamer_func
this function pushes data (two MATLAB files) to a pipeline stream and responsible for it's architecture based on the Streamz library. Additionally, the function is responsible for connecting MATLAB software to a Python code and managing the synchronization of the rest of the of the functions.
# data_giver
the function receives pairs of participant performance parameters in a matrix format, checks their validity and times their implementation it the visual interface function.

# For  Info contact:
salnat145@gmail.com
stas9239@gmail.com

