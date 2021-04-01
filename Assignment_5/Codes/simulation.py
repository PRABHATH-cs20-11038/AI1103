# Import libraries
import matplotlib.pyplot as plt
import numpy as np

# simlen
simlen=100000
# mean
mu=0
#variance
sigma=np.sqrt(2)
# creating sample list
samples = np.random.normal(mu, sigma, simlen)

# simulation
count=0
z=0
while z<simlen:
  if samples[z]>=0:
    count+=1
  z+=1

print("Simulated Probability:",count/simlen)
print("Actual probability:",1/2)
