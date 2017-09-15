'''

Edited by: Sameena Bajwa
CS237 Lab 5
Original: Sharon Goldberg
'''
import numpy as np
import math
import scipy.stats
from matplotlib import pyplot as plt

class SecondMomentEstimator(object):
#    counterArray = [0] 
#    m = 0
#    actualDataArray = [0] 
    #Generate a random Packet
    def packetGenerator(self):
        return np.random.randint(math.pow(2,14)) 
    #Generates hash functions to use
    def generateHashFunction(self):
        a = np.random.randint(0, 100000, 4)
        return (a[0], a[1], a[2], a[3])
    #Use this for a 4-wise independent hash
    def hash_4i(self, key):
        (a,b,c,d) = self.generateHashFunction()
        val = a * math.pow(key, 3) + b * math.pow(key, 2) + c * key + d
        ret = int(val % len(self.counterArray))
        return ret
    
    def dataStream(self, numPackets):
        for i in range(numPackets):
            packet = self.packetGenerator()
            binNum = self.hash_4i(packet)
            self.counterArray[binNum] += 1
            self.actualDataArray[packet] += 1
    #Finds actual second moment   
    def actualF2(self):     
        actualSum = 0
        #Calculates summation of all the counts squared
        for i in range(len(self.actualDataArray)):
            actualSum += (math.pow(self.actualDataArray[i], 2))
        return actualSum   
        
   #Finds estimated second moment
    def estimateF2(self):
        #two different summations required
        firstSum = 0
        secondSum = 0
        for i in range(len(self.counterArray)):
            firstSum += math.pow(self.counterArray[i], 2)
            secondSum += self.counterArray[i]

        secondSum = math.pow(secondSum, 2)   
        #m/(m-1)
        firstFrac = (float(self.m) / (self.m - 1))
        #1/(m-1)
        secondFrac = (1.0 / (self.m - 1))

        result = (firstFrac * firstSum) - (secondFrac * secondSum)
        return result            
        
    def __init__(self, m):
        self.m = m
        self.counterArray = [0] * m
        self.actualDataArray = [0] * int(math.pow(2, 14))


#Plots X estimate and actual F2 for various values of m
def plotF2():        
    
    #creates list of m values for the range 50, 100, ... 2500
    mvalues = [x for x in range (50, 2501) if ((x % 50) == 0)]
    estimateVals = []
    actualVals = []
    
    for m in mvalues:   
        a = SecondMomentEstimator(m)
        a.dataStream(1000)
        estimateVals += [a.estimateF2()]
        actualVals += [a.actualF2()]

        
    plt.plot(mvalues, estimateVals, label = 'estimate', color = 'r')
    plt.plot(mvalues, actualVals, label = 'actual', color = 'b')
    plt.xlabel("Amount of Buckets in the Counter Array")
    plt.ylabel("Second Moment Values")
    plt.title("Estimate vs Actual Second Moment Values")
    plt.legend()
    plt.show()
        