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

# # NF_instance

The NF_instance function nested in the pygame game loop, where in each iteration (which is a simulation of data sampling from EEG) it recieves two parameters (which should be to parameters extracted from EEG data in real time)
and manipulates an image according to those parameters, one parameter affects the blurring of the image and the other one it's size.
# # streamer_func
this function pushes data (two MATLAB files) to a pipeline stream and responsible for it's architecture based on the Streamz library. Additionally, the function is responsible for connecting MATLAB software to a Python code and managing the synchronization of the rest of the of the functions.
# # data_giver
the function receives pairs of participant performance parameters in a matrix format, checks their validity and times their implementation it the visual interface function.

# Extended libraries list
Package           Version
----------------- -------------------
appdirs           1.4.4
astroid           2.4.2
atomicwrites      1.4.0
attrs             19.3.0
Babel             2.8.0
backcall          0.2.0
black             19.10b0
bleach            3.1.5
bokeh             2.1.1
certifi           2020.6.20
chardet           3.0.4
click             7.1.2
cloudpickle       1.5.0
colorama          0.4.3
cytoolz           0.10.1
dask              2.20.0
decorator         4.4.2
distributed       2.20.0
docutils          0.16
flake8            3.8.3
fsspec            0.7.4
future            0.18.2
HeapDict          1.0.1
idna              2.10
ipykernel         5.3.3
ipython           7.16.1
ipython-genutils  0.2.0
isort             4.3.21
jedi              0.17.1
Jinja2            2.11.2
joblib            0.16.0
jupyter-client    6.1.6
jupyter-core      4.6.3
keyring           21.2.1
lazy-object-proxy 1.4.3
livereload        2.6.2
locket            0.2.0
lunr              0.5.8
Markdown          3.2.2
MarkupSafe        1.1.1
mat4py            0.4.3
mccabe            0.6.1
mkdocs            1.1.2
mkl-fft           1.1.0
mkl-random        1.1.1
mkl-service       2.3.0
more-itertools    8.4.0
msgpack           1.0.0
mypy              0.782
mypy-extensions   0.4.3
nltk              3.5
numpy             1.19.1
olefile           0.46
packaging         20.4
pandas            1.0.5
parso             0.7.0
partd             1.1.0
pathspec          0.8.0
pep517            0.8.2
pickleshare       0.7.5
Pillow            7.2.0
pip               20.1.1
pkginfo           1.5.0.1
pluggy            0.13.1
prompt-toolkit    3.0.5
psutil            5.7.0
py                1.9.0
pycodestyle       2.6.0
pyflakes          2.2.0
pygame            1.9.6
Pygments          2.6.1
pylint            2.5.3
pyparsing         2.4.7
pytest            5.4.3
python-dateutil   2.8.1
pytz              2020.1
pywin32           227
pywin32-ctypes    0.2.0
PyYAML            5.3.1
pyzmq             19.0.1
readme-renderer   26.0
regex             2020.7.14
requests          2.24.0
requests-toolbelt 0.9.1
rfc3986           1.4.0
setuptools        49.2.0.post20200714
six               1.15.0
sortedcontainers  2.2.2
streamz           0.5.4
tblib             1.6.0
time-window       0.1.0
toml              0.10.1
toolz             0.10.0
tornado           6.0.4
tqdm              4.48.0
traitlets         4.3.3
twine             3.2.0
typed-ast         1.4.1
typing-extensions 3.7.4.2
urllib3           1.25.10
wcwidth           0.2.5
webencodings      0.5.1
wheel             0.34.2
wincertstore      0.2
wrapt             1.12.1
zict              2.0.0
