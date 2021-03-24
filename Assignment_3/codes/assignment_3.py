# importing the required modules
import matplotlib.pyplot as plt
import numpy as np

def fun (x, y): 
    if 0 < x + y < 1:
      if x>0:
        if y>0:
          return 2.0
    else:
        return 0 
    return 0.0 

vfun=np.vectorize(fun)

# setting the x - coordinates
x = np.arange(0, 1, 0.000001)
# setting the corresponding y - coordinates
y = vfun(x,1/2)

plt.xlabel("X value")
plt.ylabel("Probality at Y=1/2")
plt.title("Probability distribution of (X,Y=1/2)")
# potting the points
plt.plot(x, y)
  
# function to show the plot
plt.grid()