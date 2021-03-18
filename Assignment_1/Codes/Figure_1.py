import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
from scipy import special
from random import randint

#sample size
simlen=10000

#Posible outcomes
n=(0,3)

#simulation
z=0
heads0=0
heads1=0
heads2=0
 
while z<simlen:
     num=[]
     for i in range(0,2):
           num.append(randint(0,1))
     value=num.count(1)
     if value==0:
          heads0+=1
     elif value==1:
          heads1+=1
     elif value==2:
          heads2+=1
     z=z+1

#Simulated probability
psim=[heads0/simlen,heads1/simlen,heads2/simlen]

#Theoretical probability
n = range(0,3)
probabilityhead_0=special.binom(2, 0)*(1/2)**2
probabilityhead_1=special.binom(2, 1)*(1/2)**2
probabilityhead_2=special.binom(2, 2)*(1/2)**2
panal = np.concatenate((probabilityhead_0,probabilityhead_1,probabilityhead_2),axis=None)

#Plotting
plt.stem(n,psim, markerfmt='o', use_line_collection=True, label='Simulation')
plt.stem(n,panal, markerfmt='o',use_line_collection=True, label='Analysis')
plt.xlabel('number of heads')
plt.ylabel('Probabilty')
plt.title("Probability distribution of number of heads with two tosses of a coin")
plt.legend()
plt.grid()
