import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
from scipy import special
from random import randint


#actual probability
actual=13/27

#Sample size
simlen = 100000

#on the die
#let getting outcomes {2,4,5,6} be random variable 1 and
# 0 be getting outcome as {1,3}
probbox=2/3
#Generating sample data using Bernoulli r.v.
data_bern = bernoulli.rvs(size=simlen,p=probbox)

#taking two balls after getting outcome from die
z=0
count=0

#generating sample data to each data_bern
#let random variable 1 be getting red ball and 0 be getting white ball
while(z<simlen):
  if data_bern[z]==1:
    probball=1/2 
    num=bernoulli.rvs(size=2,p=probball)
  elif data_bern[z]==0:
    probball=2/3
    num=bernoulli.rvs(size=2,p=probball)
  if num[0]!=num[1]:
    count+=1
  z+=1

#simulated probabilty
Probability=count/simlen
  
  
print("Probability-simulation,actual:",Probability,",",actual)