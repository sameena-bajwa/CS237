#Sameena Bajwa
#CS237
#Lab 3

from numpy import random as rnd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import binom
import hashlib, binascii
import string
import random

#Problem 1
def Bernoulli_trial(p):
    '''returns true if outcome of a single Bernoulli trial with parameter p
    is a "success" and false otherwise'''
    
    outcome = rnd.binomial(1, p)
    if outcome == 1:
        return True
    else:
        return False

#Problem 2
def Bernoulli_hist(p, m):
    '''Estimates the PMF of a Bernoulli random variable with parameter p
    and m independent trials'''
    
    outcomes = []
    for i in range (m):
        trial = Bernoulli_trial(p)
        if trial == True:
            outcomes += [1]
        else:
            outcomes += [0]

    plt.figure(1)
    plt.hist (outcomes, bins = 2, range = (0, 1))
    tick_locs = [0.25, 0.75]
    tick_lbls = ['False','True']
    plt.xticks(tick_locs, tick_lbls)
    plt.title ("Bernoulli Histogram")
    plt.xlabel ("Outcome")
    plt.ylabel ("Frequency")
    plt.show()
    
#Problem 5
def binomial_draw(n, p):
    '''simulates running n Bernoulli trials with parameter p, outputs
    number of successes'''
    
    count = 0
    
    for i in range (n):
        outcome = Bernoulli_trial(p)
        if outcome == True:
            count += 1
    
    return count
    
#Problem 6
def binom_trials(n, p, numExpts):
    '''returns a list of length numExpts, where each entry of the list is a draw
    of an independent binomial random variable with n trials and parameter p'''
 
    binom_outcomes = []

    for i in range (numExpts):
        binom_outcomes += [binomial_draw(n, p)]
                           
    return binom_outcomes
    
#Problem 7
def binom_hist(n, p, numExpts):
    ''' plots PMF of binomial distribution with numExpts draws of a binomial
    random variable with n trials and parameter p '''
    
    data = binom_trials(n, p, numExpts)
    weights = np.zeros_like(data) + 1./len(data)
    plt.figure(1)
    plt.hist (data, bins = n, range = (0, max(data)), align = "mid", 
              weights = weights)
    
    
    plt.title ("Binomial Histogram")
    plt.xlabel ("Outcome")
    plt.ylabel ("Probability")
    plt.show()
    
#Problem 8 and 9
def PDF_s():
    '''plots PDF of random variable S'''
    
    y_values = [1/8.0, 3/8.0, 3/8.0, 1/8.0]
    x_values = [-3, -1, 1, 3]
    plt.figure(1)
    plt.bar (x_values, y_values, color = 'r', tick_label = x_values, 
             align = "center")
    plt.title("Probability Distribution Function of S and J")
    plt.xlabel("Range")
    plt.ylabel("Probability")
    
    #Begin problem 9 code for random variable J        
    y_values = [1/256.0, 1/32.0, 7/64.0, 7/32.0, 70/256.0, 
                    7/32.0, 7/64.0, 1/32.0, 1/256.0]
    x_values = [-8, -6, -4, -2, 0, 2, 4, 6, 8]
    plt.figure(1)
    plt.bar(x_values, y_values, color = 'b', tick_label = x_values, 
                align = "center")
    plt.show()
        
#Problem 14
def newPDFs():
    '''new PDF for S and J when Scarface takes 100 steps and Diamond Jim 
    takes 200 steps'''
    
    S_xvalues = []
    S_yvalues = []
    
    for i in range (0, 101):
        new_i = 100 - 2*i
        S_xvalues += [new_i]
        S_yvalues += [binom.pmf(i, 100, .1)]
    plt.figure(1)
    plt.bar(S_xvalues, S_yvalues, edgecolor = "r")
    plt.draw()
    
    J_xvalues = []
    J_yvalues = []
    
    for j in range (1, 201):
        new_j = 200 - 2*j
        J_xvalues += [new_j]
        J_yvalues += [binom.pmf(j, 200, .1)]

    plt.figure(1)
    plt.bar(J_xvalues, J_yvalues, edgecolor = "b")
    plt.draw()
    plt.show()
    
    Pr_D = 0
    #calculate new Pr[D], following total law of probability 
    for x in S_xvalues:
        #calculate Pr[D|S = x]
        #find two appropriate J values for given value of S
        j_val = 0
        
        #use J as a function of L formula to find number to plug into binomial
        first = ((x - 1)- 200) / -2
        j_val += binom.pmf(first, 200, .5)
        second = ((x + 1)- 200) / -2
        j_val += binom.pmf (second, 200, .5)
        
        #use S as a function of L formula to find number to plug into binomial
        Pr_D += (j_val * (binom.pmf (((x-100)/-2), 100, .5)))
    print "The new probability of D is", Pr_D
    
         
        
#Problem 19
def bitcoinHist():
    '''plots scaled histogram showing the number of blocks confirmed per day'''
    
    #configure CSV so that data in columns are accessible
    columns = ['date', 'amount']
    data = pd.read_csv ('real_bitcoin.csv', delimiter = ' ', names = columns,
                        header = None)
    
    block = []
    
    for i in range (len(data) -1):
        #get each amount of bitcoins mined      
        number = data['amount'][i]
        number2 = data['amount'][i+1]

        #'number' and 'number2' being accessed should be in string form
        if (type(number) != str or type(number2) != str):
            break
        
        #strip away the string containing the number of all unnecessary chars
        number = number.strip ('0:00 \t')
        number2 = number2.strip ('0:00 \t')
        
        #print "number and number 2: ", number, number2
        #difference shows how many bitcoins were mined each day
        difference = float(number2) - float(number)

        #each mined block creates exactly 12.5 bitcoins
        block += [difference / 12.5]
        
    #print block
    
    #lambda is the average amount of blocks confirmed each day
    lambdaval = sum(block) / len(block)
      
    poissonDist = rnd.poisson(lambdaval, 60)
    weights = np.zeros_like(poissonDist) + 1./len(poissonDist)
    plt.figure(1)
    plt.hist (poissonDist, bins = 6, weights = weights,
               width = 10, align = 'mid')
    plt.title("Poisson Distribution with Calculated Lambda")
    plt.show()
    
    weights = np.zeros_like(block) + 1./len(block)
    plt.figure(2)
    plt.hist (block, bins = 6, align = 'mid', weights = weights, 
              width = 10, color = 'r')
    plt.title ("Number of Blocks per Day")
    plt.xlabel ("Block amounts")
    plt.ylabel ("Probability")
    plt.show()
    
    print "the lambda value was calculated by finding the average of " \
    "blocks confirmed each day:", lambdaval
    
#Problem 20
def hash_exp(num_zeroes):
    ''' finds a nonce such that SHA256(Bj-1 || Bj | s) has at least 
        num_zeroes leading zeroes'''
    
    #converts hexdecimal to binary
    binary = lambda x: "".join(reversed( [i+j for i,j in 
    zip( *[ ["{0:04b}".format(int(c,16)) for c in reversed("0"+x)][n::2] 
    for n in [1,0] ] ) ] ))
        
    while(True):
        
        nonce = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
        
        block = hashlib.sha256(b'wubba lubba dub dub ' + str(nonce)).hexdigest()
        #converts newly concatenated block to binary
        block_binary = binary(block)

        #iterates through each character of the string
        for i in range(num_zeroes):
            if block_binary[i] != '0':
                break
            
            if (block_binary[i] == '0' and i < (num_zeroes - 1)):
                continue
               
            #if the string has at least 'num_zeroes' leading zeroes,
            #return the nonce and string
            if (block_binary[i] == '0' and i == (num_zeroes - 1)):
               
                return nonce, block_binary
            
#Problem 21
def fake_hash_exp (num_zeros):        
    ''' simulates confirming a new bitcoin block and checking if there are at 
        least num_zeros leading zeros'''
        
    #converts hexdecimal to binary
    binary = lambda x: "".join(reversed( [i+j for i,j in
    zip( *[ ["{0:04b}".format(int(c,16)) for c in reversed("0"+x)][n::2] for 
    n in [1,0] ] ) ] ))
     
    
    number = random.randint (0, 2**256-1)
   
    #convert number to hex, removes unnecessary characters
    hexnumber = hex(number).rstrip("L").lstrip("0x")
    
    #converts hex to binary
    newNumber = binary(hexnumber)
    
    for i in range (num_zeros):
        if newNumber[i] != '0':
            break
        if (newNumber[i] == '0' and i == (num_zeros -1)):
            return True

#Problem 21
def fake_hash_trials(n, num_zeros):
    '''using above function to run n trials mining the bitcoin for blocks with 
        num_zeros leading zeros and generating a vector based on the results''' 
    
    vector = []
    for i in range (n):
        result = fake_hash_exp(num_zeros)
        if result == True:
            vector.append(1)
        else:
            vector.append(0)
    return vector
    
#Problem 22
def calc_times(n, num_zeros):
    '''use vector created in fake_hash_trials() to create a vector of interarrival
        times between each successful mine'''
    
    #create vector to calculate times based off of
    vector = fake_hash_trials(n, num_zeros)
    
    #create vector for results to be stored in 
    final = []
    
    count = 0
    for i in vector:
        if i == 0:
            count += 1
        else:
            final.append(count)
            count = 0
    return final
        
#Problem 23
def plot_times(n, num_zeros):
    '''plots histogram of arrival times using vector created from calc_times()'''
    
    #create vector to plot histogram with
    vector = calc_times(n, num_zeros)
    
    plt.figure(1)
    plt.hist(vector, bins = 20, color = 'r', normed = False, align = 'mid')
    plt.title("Interarrival Times between Successful Mines")
    plt.xlabel("Times")
    plt.ylabel("Frequency")
    plt.show()
    
#Problems 24 and 25
def successCount (n, num_zeros):
    '''count the number of times a successful mining occurs every 10 minutes
        assume that 1000 trials = 10 minutes, plot histogram of results'''
    
    #create vector to count success amounts from
    vector = fake_hash_trials(n, num_zeros)
    
    results = []
    
    #counts which trial we are on
    count = 0
    #counts how many successes occur in each 10 minute interval
    success = 0
    
    for i in vector:
        if i == 1:
            success += 1
        count += 1
        if count == 1000:
            results.append(success)
            #reset count and success every 1000 trials
            count = 0
            success = 0
    #print results
    
    weights = np.zeros_like(results) + 1./len(results)
    plt.figure(1)
    plt.hist(results, bins = 10, weights = weights, color = 'r', width = 1.5,
             alpha = 0.5, align = "mid", label = "vector")
    plt.title("Mining Success Rate, 10 Minute Intervals")
    plt.xlabel("Success Count")
    plt.ylabel("Probability")
    plt.draw()
            
    #Additional code for problem 25 - find a lambda value where a Poisson 
    #distribution would fit the above histogram
    lambdaval = float(sum(results)) / len(results)
    poissonDist = rnd.poisson(lambdaval, len(results))
    weights = np.zeros_like(poissonDist) + 1./len(poissonDist)
    
    #print lambdaval
    
    plt.figure(1)
    plt.hist (poissonDist, bins = 10, weights = weights, color = 'b', width = 1.5,
              alpha = 0.8, label = "poisson")
    plt.legend(loc = 'upper right')

    plt.show()
