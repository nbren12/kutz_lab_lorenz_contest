from scipy.io import loadmat, savemat
import numpy as np
import sys

def load_data():
    return loadmat("./known.mat")['x']


def save_data(x):
    savemat(sys.argv[1], {'x': x})


x = load_data()
n_predict = 10000

pred = np.tile(x[:, -1:, :], (1, n_predict, 1))
save_data(pred)
