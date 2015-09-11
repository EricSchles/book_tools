#http://www.walkingrandomly.com/?p=5215 - this code was influenced by this
import numpy as np
from scipy.optimize import curve_fit
import random


xdata = np.array([5,6,7,3,4,8,9,12,17,4,14,9,25,12,24,15])
ydata = np.array([12,11,11,30,27,9,8,8,14,30,10,8,10,10,10,10])

def func(x,p1,p2):
    return p2*x**2+ p1*x 

popt, pcov = curve_fit(func, xdata,ydata,p0=(7.0,9.0))
p1 = popt[0]
p2 = popt[1]
residuals = ydata - func(xdata,p1,p2)
f_residuals = sum(residuals**2)
print f_residuals

