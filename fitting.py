import math
import numpy as np
from scipy import optimize

def func_autocorr(x, a):
    return np.exp(-x/a)


def calc_param(filename, norm_time):
    x_data = []
    y_data = []

    with open(filename, "r") as input:
        for line in input:
            x_data.append(float(line.split()[0])/norm_time)
            y_data.append(float(line.split()[1]))

    param, param_cov = optimize.curve_fit(func_autocorr, x_data, y_data)

    return(param)

print(calc_param("protein_result.txt", 100))