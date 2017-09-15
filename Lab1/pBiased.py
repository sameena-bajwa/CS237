#Sameena Bajwa
#CS237
#Lab 1, Problem 4

#function generating a random number between 0 and 1
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
    
    

    
    
    
    
    