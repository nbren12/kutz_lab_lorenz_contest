#!/usr/bin/env python
"""
3.  Remember our challenge NN problem.  I will be putting up “training data” soon on the Lorenz attractor.   Objectives
	(a) How well can you train the network to predict trajectories and not fall off for a test set I give  later on
	(b) How well can you do (a) with noise training/test data
	(c) How well can you predict the the Lorenz when you only have measurements of the x variable
	(d) How well can you do this for noise training/test data for x
	(e) Given test/training data across a bunch of values of rho, how well can you train a NN to stick on trajectories for a test set with different rho values


Evaluation metrics:

1. Prediction Error: RMS
2. Attractor Errors: covariance, autocorrelation function

"""
import matplotlib.pyplot as plt
import sys
import numpy as np
from scipy.io import loadmat, savemat


def load(path):
    return loadmat(path)['x']


def mean(x):
    return np.apply_over_axes(np.mean, x, [0, 1])


def rms_error(truth, pred):
    return np.sqrt(((truth - pred)**2).mean(axis=0).mean(axis=-1))


def std_dev(truth):
    mu = mean(truth)
    variance = mean((truth - mu)**2)
    return np.sqrt(variance)


def falloff_time(truth, pred, rms_ratio=.5):
    sig = np.sqrt(((truth - mean(truth))**2).mean())
    rms = rms_error(truth, pred)
    return np.searchsorted(rms / sig > rms_ratio, True)


def attractor_error(truth, pred):
    pass


def main():
    truth = sys.argv[1]
    pred = sys.argv[2]

    truth = load(truth)
    pred = load(pred)

    # pad pred to have same length in time as truth
    truth = np.take(truth, np.arange(pred.shape[1]), axis=1)

    print("Fall off index:", falloff_time(truth, pred))


if __name__ == '__main__':
   main()
