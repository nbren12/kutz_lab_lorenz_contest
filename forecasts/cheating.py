from scipy.io import loadmat, savemat
import numpy as np
import sys

def load_data():
    return loadmat("./secret.mat")['x']


def save_data(x):
    fname = sys.argv[1]
    savemat(fname, {'x': x})


fall_of_time = 5000
pred = load_data()
pred[:, 5000:,:]  = 1000

save_data(pred)
