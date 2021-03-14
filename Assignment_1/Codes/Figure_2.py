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

plt.bar(x1, y1, label="probability of no. of tails", color='g')
plt.plot()

plt.xlabel("number of tails")
plt.ylabel("Probality")
plt.title("Probability distribution of number of tails with three tossing coins")
plt.legend()
plt.show()