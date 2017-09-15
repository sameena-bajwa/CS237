#Sameena Bajwa
#CS237
#Lab 1, Problem 3

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
        