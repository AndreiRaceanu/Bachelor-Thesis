#import modules

import numpy as np
from pysindy.differentiation import *
import pysindy as ps
from sklearn.metrics import mean_squared_error
from pysindy.optimizers import STLSQ
from pyGPGO.covfunc import squaredExponential
from pyGPGO.acquisition import Acquisition
from pyGPGO.surrogates.GaussianProcess import GaussianProcess
from pyGPGO.GPGO import GPGO
import matplotlib.pyplot as plt
from pysindy.differentiation import FiniteDifference






def read_data (file_path):
    """

    :param file_path: file to extract Electroencephalograms from
    :return: 13 channels from the file in matrix form
    """
    file =  open(file_path, 'r')
    matrix = []
    for line in file :
        tokens = line.split(",") 
        matrix.append( list( map(lambda x : float(x) , tokens) ) )
    return np.matrix(matrix)



# Data set preparing

N = 2    # Number of files used for training
X = []   # Training data_set
for it in range(1,N+1): 
    X.append(read_data(f"training_{it}.csv"))
X_data_set = np.array(X)



variav  = 1

rows= 10
columns = 16384

sfd1 = SmoothedFiniteDifference()

matrix = []
time = range(0,16384)
time = list(time)
for it in range(10):
    matrix.append(time)
matrix2 = []
matrix2.append(matrix)
matrix2.append(matrix)
t = np.linspace(0,10,1)
x = np.sin(t)
sfd = SmoothedFiniteDifference(smoother_kws={'window_length': 5})
pula = sfd._differentiate(X, t)