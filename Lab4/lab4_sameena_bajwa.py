# -*- coding: utf-8 -*-
"""
Sameena Bajwa
CS237
Lab 4

"""
import numpy as np
import random as rnd
import matplotlib.pyplot as plt

#Problem 1
def deterministicLoadBalancer(n):
    
    array = [0] * n
    for i in range(len(array)):
        if array[i] == min(array):
            array[i] += 1


#Problem 3/8
def loadBalancer(n, d):
    
    aisles = [0] * n   
    #code for problem 3
#    for i in aisles:
#        
#        line = rnd.randint(0, n -1)
#        aisles[line] += 1
    
    #additions for problem 8
    for i in range(n):
        #holds the d lines that were randomly chosen
        lines = []
        for j in range(d):
            #get the d random lines
            lines += [rnd.randint(0, n-1)]
            
        #will hold the amount of customers in the d random lines chosen
        lineCount = []
        
        #k acts as the index to the aisle array
        for k in lines:
            lineCount += [aisles[k]]
            
        #holds shorter line's count
        short = min(lineCount)
        #holds the location of the line (within lineCount) that will be added to
        shortLoc = lineCount.index(short)
        #uses index to of shortest line count to match up with shortest line number
        lineAdd = lines[shortLoc]
        aisles[lineAdd] += 1
    
    return max(aisles)

#Problem 7
def plotMaxLength():
    
    nvalues = list(range(3, 501))
    averageMax = []
    
    mitzenmacherData = []
    for k in nvalues:
        num = 3 * np.log(k)
        dem = np.log(np.log(k))
        mitzenmacherData += [num/dem]
        
    
    for i in nvalues:
        print "on iteration ", i
        #resets before each 1000 iterations of n 
        averagePerCall = []
        for j in range(1000):
            result = loadBalancer(i)
            averagePerCall += [result]
 
        #add average of the results for a particular nvalue
        averageMax += [np.mean(averagePerCall)]
                       
    plt.plot(nvalues, averageMax, label = "empirical", color = 'r')
    plt.plot(nvalues, mitzenmacherData, label = "theoretical", color = 'b')
    plt.xlabel("Number of lines and customers")
    plt.ylabel("Average maximum line length")
    plt.title("Maximum Line Length Simulations")
    plt.legend()
    plt.show()
    
#problem 10
def plotDChoice():
    
    xvalues = list(range(2, 11))
    averageMax = []
    
    for i in xvalues:
        print "on iteration ", i
        #resets before each 1000 calls to loadBalancer
        averagePerCall = []
        for j in range(1000):
            result = loadBalancer(1000, i)
            averagePerCall += [result]
        
        #add average of the results for a particular value of d
        averageMax += [np.mean(averagePerCall)]
        
    mitzenmacherData = []
    for d in xvalues:
        num = np.log(np.log(1000))
        dem = np.log(d)
        mitzenmacherData += [(num/dem) + 2]
        
    plt.plot(xvalues, mitzenmacherData, label = "theoretical", color = 'b')    
    plt.plot(xvalues, averageMax, label = "empirical", color = 'r')
    plt.xlabel("Number of lines chosen for comparison")    
    plt.ylabel("Average maximum line length")
    plt.title("Randomized D-Choice Algorithm")
    plt.legend()
    plt.show()