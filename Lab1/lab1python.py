#Sameena Bajwa
#CS237
#Lab 1 Python Code

#Problem 1

from matplotlib import pyplot as plt

def ex1():
    
    #plot red dotted line
    plt.plot ([1, 2, 3 ,4], [1, 2, 3, 4], 'r:')

    plt.draw()
    
    #plot blue triangles
    plt.plot ([1, 2, 3 ,4], [1, 2, 3, 4], 'bv')
    
    plt.draw()
    plt.show()
    
#Problem 2
    
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


#Problem 3

from matplotlib import pyplot as plt
import random 

def pi_Estimate(): 
    plt.figure(1)
    
    
    axes = plt.axes(aspect = 1)
    plt.xlim (-1,1)
    plt.ylim (-1,1)
    
    plt.axvspan(-1, 1, facecolor = "none")
    circle = plt.Circle((0,0), radius = 1, facecolor = 'none')
    
    axes.add_patch(circle)
    plt.draw()
    
    
    plotx = []
    ploty = []
    
    inCircle = 0.0
    total = 0.0
    
    i = True
    
    while (i == True):
        
        randx = random.uniform(-1,1)
        plotx += [randx]
        randy = random.uniform(-1,1)
        ploty += [randy]
        
        #equation to determine distance the point is from the center of the circle
        check = randx ** 2 + randy ** 2
        
        if check < 1:
            
            inCircle += 1.0
        total += 1.0
        
        if (round (4 * (inCircle / total), 2) == 3.14):
            i = False
            
    
    print total
    
    plt.plot (plotx, ploty, 'b:')   
    
    plt.show()


#Problems 4 and 6 

from random import random
from matplotlib import pyplot as plt
import numpy 

def expt (p):
    
    heads = False
    count = 0
    
    while (heads == False):
        
        #if the random number is greater than p, then the flip was tails
        if (random() > p):
            count += 1
        else: 
            count += 1
            heads = True
    
    return count

def coin_flip_test (n, p):

    for i in range (0, n):
        return expt (p)


def plot_pmf(n, p):
    
    count = []
    for i in range (0, n):
        count += [coin_flip_test(n,p)]
   
    plt.figure(1)
    
    plt.hist(numpy.asarray(count), bins = 10, rwidth = .7, align = 'mid', 
             
    weights = numpy.zeros_like (count) + 1./len(count))
    
    plt.xlim(0, max(count))
    
    #Start of add-ons for question 6
    plt.ylim (0, 1)
    function = []
    x_coords = []
    
    for i in range (n + 1):
        x_coords += [i]
    
    
    for i in range (n + 1):
        function += [i / (10/p)]
    #End of question 6 add-ons
    
    plt.title ("Flipping a p-biased coin")
    plt.xlabel ("Amount of Flips")
    plt.ylabel ("Probability")
    
    plt.plot(x_coords, function, 'r:') 
    
    plt.draw()