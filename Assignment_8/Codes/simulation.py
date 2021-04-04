import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
from scipy import special
from random import randint

#simlen
simlen=10000
#simulation practically
z=0 
count=0
while z<simlen:
  num=[]
  for i in range(0,2):
    num.append(randint(1,3))
  if num[0]**2 >= num[1]:
    count+=1
  z=z+1

#simulated probability
simprobability=count/simlen
print("Simulated Probability: ",simprobability)
print("Actual Probability: ",7/9)