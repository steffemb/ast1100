import numpy as np
import random
from matplotlib.pyplot import *


K = 1.3806488*10**(-23)
T = 6000
m = 1.66053892*10**(-27)
sigma = np.sqrt((K*T)/m)
mean = 0
N = 10*10**6
dt = 10**(-9)

z = np.zeros(N)
x = y = z 
vz = np.zeros(N)
vx = vy = vz 

for i in range(0, N):
   vx[i] = random.gauss(mean,sigma)
   #vy[i] = random.gauss(mean,sigma)
   #vz[i] = random.gauss(mean,sigma)
   x[i] = random.uniform(0, 0.1)
   #y[i] = random.uniform(0, 0.1)
   #z[i] = random.uniform(0, 0.1)

n = 0
P = 0
for i in range(0, N):
   if x[i] + vx[i]*dt >= 0.1:
      n += 1
      P += (2*m*vx[i])/dt

print P*6
P_analytical = (N*K*T)
print P_analytical
