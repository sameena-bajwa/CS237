'''
Sameena Bajwa

Bloom Filter Class 
for Bloom Filter Lab
CS237, Sharon Goldberg
'''
from bloomFilterHash import bloomFilterHash 
import numpy.random as rnd
import matplotlib.pyplot as plt

class BloomFilter(object):
    #Class Variables
    numBits = 0
    bitArray = [0]
    numHashFunctions = 0
    
    '''Problem 9: Insert function, pass it a key and insert into bloom filter'''
    def insert(self, key):
        
        for i in range (1, self.numHashFunctions + 1):
            #additions for problem 16
            if (self.pairwise == True):
                  result = (self.hash.pairwiseHash_i(key, i))      
            else:
                result = (self.hash.hash_i(key, i)) 
            self.bitArray [result] = 1
    
    '''Problem 9:Lookup function, pass it a key and return true or false'''
    def lookup(self, key):
        
        for i in range (1, self.numHashFunctions + 1):
            #additions for problem 16
            if (self.pairwise == True):
                result = (self.hash.pairwiseHash_i(key, i))
            else:
                result = self.hash.hash_i(key, i) 
            if self.bitArray[result] == 0:
                return False
        return True
        
    '''Problem 10: Insert function, pass in randomly generated data into bloom filter'''
    def rand_inserts(self):
        #cast the random integer values as strings
        key = str(rnd.randint (0, 1 * (10**8)))
        self.insert(key)
             
    def __init__(self, numBits, numHashFunctions, pairwise):
        self.pairwise = pairwise #added for problem 16
        self.numBits = numBits
        self.bitArray = [0] * numBits
        self.numHashFunctions = numHashFunctions
        self.hash = bloomFilterHash(numBits, numHashFunctions)
     
    #code from adversial.py - used for questions 21 and 22
    badInserts = []
    badLookups = []

    def adversarialInserts(self):
        self.personalBF = [0]*self.numBits
        self.badInserts = []
        count = 0
        for i in range (16384):
            flag = True
            val = [0] * self.numHashFunctions
            for j in range (self.numHashFunctions):
                val[j] = self.hash.pairwiseHash_i(i, j)
                if self.personalBF[val[j]] != 0:
                    flag = False
            if flag:
                self.badInserts.append(val[j])
                for j in range (self.numHashFunctions):
                    count += 1
                    self.personalBF[val[j]] = 1
        for i in range(len(self.badInserts)):
            self.insert(self.badInserts[i])
        return self.badInserts

    def adversarialLookups(self):
        self.badLookups = []
        for i in range (16384):
            if i not in self.badInserts:
                if self.lookup(i):
                    self.badLookups.append(i)
        count = 0
     
        for i in range (len(self.badLookups)):
            if self.lookup(self.badLookups[i]):
                count += 1
        
        return count * 1.0 / len(self.badLookups)

    
'''Problem 12: Compute the average false positive probability''' 
def aveFalsePos():

    probability = []                    #array to hold each iterations false 
                                        #positive probability 
    
    for i in range (1000):              #repeat experiment 1000 times
        count = 0                       #stores amount of false positives found
        example = BloomFilter (4095, 10)
        
        for j in range (600):           #600 random insertions
            example.rand_inserts()
            
        for k in range (10000):         #call lookup 10000 times
            num = str(rnd.randint(0, 1 * (10**8)))
            result = example.lookup(num)
            if result == True:
                count += 1
                
        probability += [float (count) / 10000] 
        example.bitArray = [0] * example.numBits #clear bloom filter
    
    average = float (sum (probability)) / (len (probability)) 
    print average 
    
'''Problem 13: Vary the number of hash functions and plot the observable change
in false positive probabilities on a graph'''
def plotAverage():
    
    #generate the 10000 values for lookup()
    randints = []
    for y in range (10000):
        num = rnd.randint (0, 1 * (10 ** 8))
        randints += [num]
        
    yvalues = []
    xvalues = []
    for i in range(2, 31):              #numHashFunctions range
        xvalues += [i]                  #numHashFunction will be on x axis
        probability = []

        for x in range (1000):
    
            example = BloomFilter (4095, i)
            count = 0
            for j in range (600):
                example.rand_inserts()
            for k in (randints):
                result = example.lookup(k)
                if result == True:
                    count += 1
            probability += [float(count) / 10000]
            example.bitArray = [0] * example.numBits
        yvalues += [float (sum(probability)) / (len(probability))]
        
    plt.plot(xvalues, yvalues, 'ro')
    plt.show()
        
'''Problem 18: Modification of code used for problem 12'''
def aveAndMaxFalsePos():

    probability = []                    #array to hold each iterations false 
                                        #positive probability 
    maxFalse = 0                        #variable to hold the max 
    
    for i in range (1000):              #repeat experiment 1000 times
        count = 0                       #stores amount of false positives 
        example = BloomFilter (4095, 6, False)
        
        for j in range (600):           #600 random insertions
            example.rand_inserts()
            
        for k in range (10000):         #call lookup 10000 times
            num = str(rnd.randint(0, 1 * (10**8)))
            result = example.lookup(num)
            if result == True:
                count += 1
                
        nextValue = float (count) / 10000
        probability += [nextValue]
        
        if nextValue > maxFalse:        #update the max variable if necessary
            maxFalse = nextValue
            
        example.bitArray = [0] * example.numBits #clear bloom filter
    
    average = float (sum (probability)) / (len (probability)) 
    print "average false positive probability", average   
    print "maximum false positive probability", maxFalse

'''Problem 19: Same as problem 18, except use pairwise independent hash functions'''
def falsePosPairwise():

    probability = []                    #array to hold each iterations false 
                                        #positive probability 
    maxFalse = 0                        #variable to hold the max 
    
    for i in range (1000):              #repeat experiment 1000 times
        count = 0                       #stores amount of false positives
        example = BloomFilter (4095, 6, True)
        
        for j in range (600):           #600 random insertions
            example.rand_inserts()
            
        for k in range (10000):         #call lookup 10000 times
            num = str(rnd.randint(0, 1 * (10**8)))
            result = example.lookup(num)
            if result == True:
                count += 1
                
        nextValue = float (count) / 10000
        probability += [nextValue]
        
        if nextValue > maxFalse:        #update the max variable if necessary
            maxFalse = nextValue
            
        example.bitArray = [0] * example.numBits #clear bloom filter
    
    average = float (sum (probability)) / (len (probability)) 
    print "average false positive probability", average   
    print "maximum false positive probability", maxFalse
        
'''Problem 21: Modification of code for problem 18, use adversarialInserts()
instead of randInserts()'''
def adversarialTests():
    probability = []                    #array to hold each iterations false 
                                        #positive probability 
    
    #generate the 10000 values for lookup
    randints = []
    for x in range (10000):             
        num = str(rnd.randint(0, 1 * (10**8)))
        randints += [num]

    maxFalse = 0                        #variable to hold the max 
    
    for i in range (1000):              #repeat experiment 1000 times
    
        count = 0                       #stores amount of false positives
        example = BloomFilter (4095, 6, True)
        
        #for j in range (600):           #600 adversarial insertions
        example.adversarialInserts()
            
        for k in (randints):
            result = example.lookup(k)
            if result == True:
                count += 1
                
        nextValue = float (count) / 10000
        probability += [nextValue]
        
        if nextValue > maxFalse:        #update the max variable if necessary
            maxFalse = nextValue
            
        example.bitArray = [0] * example.numBits #clear bloom filter
    
    average = float (sum (probability)) / (len (probability)) 
    print "average false positive probability", average   
    print "maximum false positive probability", maxFalse

'''Problem 22: Modification of code for problem 21, use adversarialInserts()
instead of randInserts() and adversarialLookups() instead of lookup()'''
def adversarialTestsPart2():
    probability = []                    #array to hold each iterations false 
                                        #positive probability 
 
    maxFalse = 0.0                      #variable to hold the max 
    
    for i in range (1000):              #repeat experiment 1000 times

        example = BloomFilter (4095, 6, True)
        
        for j in range (600):           #600 adversarial insertions
            example.adversarialInserts()
            
        
        result = example.adversarialLookups()
        print result

        probability += [result]
        
        if result > maxFalse:        #update the max variable if necessary
            maxFalse = result
            
        example.bitArray = [0] * example.numBits #clear bloom filter
    
    average = float (sum (probability)) / (len (probability)) 
    print "average false positive probability", average   
    print "maximum false positive probability", maxFalse        
            
            


