import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
from scipy import special

#parameter
q=1/2

#no of tossed coins
n=3

#probabilty
probabilityhead_0=special.binom(n, 0)*(q)**n
probabilityhead_1=special.binom(n, 1)*(q)**n
probabilityhead_2=special.binom(n, 2)*(q)**n
probabilityhead_3=special.binom(n, 3)*(q)**n

x1 = [0, 1, 2,3]
y1 = [probabilityhead_0, probabilityhead_1, probabilityhead_2, probabilityhead_3]

#simulation practically
z=0
tails0=0
tails1=0
tails2=0
tails3=0
 
while z<100000: #simlen
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

y2 = [tails0/z,tails1/z,tails2/z,tails3/z]
#plotting of graph
plt.bar(x1, y1, label="Theoretical solution", color='g')
plt.plot(x1, y2, label="Practical soltion")
plt.plot()

plt.xlabel("number of tails")
plt.ylabel("Probality")
plt.title("Probability distribution of number of tails with three tossing coins")
plt.legend()
plt.show()
