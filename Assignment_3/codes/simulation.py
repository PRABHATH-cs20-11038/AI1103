import numpy as np

#simlen
simlen=100000

#Given f(x,y)=2 and 0<x+y<1,x>0,y>0
#implies f(x,y) independent of y and x.
#as y is given to be 1/2 (y=1/2)
# therefore f(x,y)=2 and 0<x<1/2, which is a constant
# As 0 < x < 1/2 and the probability density function is constant,
# then x has equal chance of taking any value between 0 and 1/2
x=1/2*np.random.random_sample(simlen)
sum=np.sum(x)

exp_value=sum/simlen
print("E=",exp_value)