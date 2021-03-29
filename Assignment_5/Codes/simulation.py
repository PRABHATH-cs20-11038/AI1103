# Import libraries
import matplotlib.pyplot as plt
import numpy as np

mu=0
sigma=np.sqrt(2)
# Creating histogram
samples = np.random.normal(mu, sigma, 100000)

#simulation
count=0
z=0
while z<100000:
  if samples[z]>=0:
    count+=1
  z+=1
print("Simulated Probability:",count/100000)
print("Actual probability:",1/2)