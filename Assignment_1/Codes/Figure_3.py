import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
from scipy import special

#parameter
p=1/2

#no of tossed coins
n=4

#probabilty
probabilityhead_0=special.binom(n, 0)*(p)**n
probabilityhead_1=special.binom(n, 1)*(p)**n
probabilityhead_2=special.binom(n, 2)*(p)**n
probabilityhead_3=special.binom(n, 3)*(p)**n
probabilityhead_4=special.binom(n, 4)*(p)**n

x1 = [0, 1, 2, 3, 4]
y1 = [probabilityhead_0, probabilityhead_1, probabilityhead_2, probabilityhead_3, probabilityhead_4]



#simulation practically
z=0
heads0=0
heads1=0
heads2=0
heads3=0
heads4=0
 
while z<100000: #simlen
     num=[]
     for i in range(0,4):
           num.append(randint(0,1))
     value=num.count(1)
     if value==0:
          heads0+=1
     elif value==1:
          heads1+=1
     elif value==2:
          heads2+=1
     elif value==3:
          heads3+=1
     elif value==4:
          heads4+=1
     z=z+1

y2 = [heads0/z,heads1/z,heads2/z,heads3/z,heads4/z]
#plotting of graph
plt.bar(x1, y1, label="Theoretical solution", color='r')
plt.plot(x1, y2, label="Practical soltion")
plt.plot()

plt.xlabel("number of heads")
plt.ylabel("Probality")
plt.title("Probability distribution of number of heads with four tossing coins")
plt.legend()
plt.show()
