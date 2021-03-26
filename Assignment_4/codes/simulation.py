from scipy.stats import poisson
import matplotlib.pyplot as plt
import math

# mean of poison distribution
mu = 3

# finding probabilty using theory
# defining poison probabilty 
def prob(p):
  return mu**p/(math.factorial(p)*math.exp(mu))

# theoretical probabilty
theo_probability= prob(0)+prob(1)+prob(2)

# finding probability using simulation
# total of no of trails
simlen=100000

# assigning values to 100000 trails
r = poisson.rvs(mu, size=simlen)

# checking for values <3
z=0
count=0
while z<simlen:
  if r[z]<3:
    count+=1
  z+=1

# simulated probability
sim_probability=count/simlen

print("simulated probabilty:",sim_probability)
print("theoretical probability:",theo_probability)