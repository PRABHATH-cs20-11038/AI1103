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
n=(0,4)

#simulation
z=0
tails0=0
tails1=0
tails2=0
tails3=0
 
while z<simlen:
     num=[]
     for i in range(0,3):
           num.append(randint(0,1))
     value=num.count(1)
     if value==0:
          tails0+=1
     elif value==1:
          tails1+=1
     elif value==2:
          tails2+=1
     elif value==3:
          tails3+=1
     z=z+1

#Simulated probability
psim=[tails0/simlen,tails1/simlen,tails2/simlen,tails3/simlen]

#Theoretical probability
n = range(0,4)
probabilitytails_0=special.binom(3, 0)*(1/2)**3
probabilitytails_1=special.binom(3, 1)*(1/2)**3
probabilitytails_2=special.binom(3, 2)*(1/2)**3
probabilitytails_3=special.binom(3, 3)*(1/2)**3
panal = np.concatenate((probabilitytails_0,probabilitytails_1,probabilitytails_2,probabilitytails_3),axis=None)

#Plotting
plt.stem(n,psim, markerfmt='o', use_line_collection=True, label='Simulation')
plt.stem(n,panal, markerfmt='o',use_line_collection=True, label='Analysis')
plt.xlabel('number of tails')
plt.ylabel('Probabilty')
plt.title("Probability distribution of number of tails with three tossing coins")
plt.legend()
plt.grid()
