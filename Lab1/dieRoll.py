#Sameena Bajwa
#CS237
#Lab 1, Problem 2

from matplotlib import pyplot as plt
from random import randint
import numpy 

def dieRoll(m):
    
    high = m * 6
    y_series = numpy.random.randint (1, high + 1, (1, 10000))
    
    y_series = y_series[0]
    print y_series
    plt.figure(1)
    plt.hist(y_series, 
    
    bins = 6,
    rwidth = .5,
    
    align = 'mid',
    
    weights = numpy.zeros_like (y_series) + 1. / y_series.size)

    plt.xlim(1, high)
    plt.title ("Rolling a die")
    plt.xlabel ("Value")
    plt.ylabel ("Probability")
    
    plt.show()

