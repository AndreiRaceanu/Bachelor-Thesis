import numpy as np
import matplotlib.pyplot as plst
from mpl_toolkits import mplot3d
import pysindy as ps
import random
import pyGPGO
from pysindy import PolynomialLibrary, FourierLibrary
from pyGPGO.surrogates.GaussianProcess import GaussianProcess
from pyGPGO.covfunc import squaredExponential
from pyGPGO.acquisition import Acquisition
from pyGPGO.GPGO import GPGO
from sklearn.metrics import mean_squared_error
from pysindy.differentiation import SmoothedFiniteDifference
#importarea modulelor necesare prelucrarii datelor, optimizarii bayesiene si gasirii ecuatiilor sistemului dinamic


def read_files(file_path):
    with open(file_path, 'r') as file : 
        content = file.read()
    return content
file_paths = ['C:\Users\andre\Desktop\licenta\0_neutru\cz_eeg4.txt', 'C:\Users\andre\Desktop\licenta\0_neutru\hql_eeg23.txt', 'C:\Users\andre\Desktop\licenta\0_neutru\ldy_eeg4.txt','C:\Users\andre\Desktop\licenta\0_neutru\ly_eeg4.txt']

file_contents = [read_files(file) for file in file_paths]

