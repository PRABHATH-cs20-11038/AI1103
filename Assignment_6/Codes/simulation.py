import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
from scipy import special
from random import randint


#actual probability
actual=special.binom(10,2) * (1/10)**2 * (9/10)**8

#Sample size
simlen = 100000

#Simulation
z=0
count=0
prob=1/10 #probability of getting a defective item
while z<simlen:
  data=bernoulli.rvs(size=10,p=prob)
  item=0
  for i in range(0,10):
    if data[i]==1:
      item+=1
  if item==2:
    count+=1
  z+=1

#simulated probabilty
Probability=count/simlen

print("Probability-simulation,actual:",Probability,",",actual)