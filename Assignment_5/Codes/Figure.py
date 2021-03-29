# Import libraries
import matplotlib.pyplot as plt
import numpy as np

mu=0
sigma=np.sqrt(2)
# Creating histogram
samples = np.random.normal(mu, sigma, 100000)
plt.hist(samples, bins = 50, density = True,
         alpha = 1, color =(0.9, 0.1, 0.1))
  
# Add a title
plt.title('Random Samples - Normal Distribution')
  
# Add X and y Label
plt.xlabel('Z value')
plt.ylabel('Frequency')
  
# Creating vectors X and Y
x = np.linspace(-6, 6, 10000)
y = (1/(4 * np.pi)**0.5) * (np.exp(-x**2 / 4))
  
# Creating plot
plt.plot(x, y, 'b', alpha = 1)

# Show plot
plt.grid()