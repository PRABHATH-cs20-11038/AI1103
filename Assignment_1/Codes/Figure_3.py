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

plt.bar(x1, y1, label="probability of no. of heads", color='r')
plt.plot()

plt.xlabel("number of heads")
plt.ylabel("Probality")
plt.title("Probability distribution of number of heads with four tossing coins")
plt.legend()
plt.show()