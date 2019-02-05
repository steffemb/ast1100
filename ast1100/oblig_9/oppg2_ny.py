from matplotlib.pyplot import *
from numpy import *

K = 1.3806488*10**(-23)
m = 2*1.66053892*10**(-27)

mean = 0
N = 10**6
dt = 10**(-9)

x = np.zeros(N)
y = np.zeros(N)
z = np.zeros(N)
vx = np.zeros(N)
vy = np.zeros(N)
vz = np.zeros(N)

for i in range(0, N):
   x[i] = random.uniform(0, 0.1)
   y[i] = random.uniform(0, 0.1)
   z[i] = random.uniform(0, 0.1)

def hayabusa(T):
   sigma = np.sqrt((K*T)/m)
   for i in range(0, N):
      vx[i] = random.normal(mean,sigma)
      vy[i] = random.normal(mean,sigma)
      vz[i] = random.normal(mean,sigma)

   n = 0
   F = 0
   for i in range(0, N):
      if x[i] + vx[i]*dt > 0.1 or x[i] + vx[i]*dt < 0:
         n += 1
         F += abs((m*vx[i])/dt)
      if y[i] + vy[i]*dt > 0.1 or y[i] + vy[i]*dt < 0:
         n += 1
         F += abs((m*vy[i])/dt)
      if z[i] + vz[i]*dt > 0.1 or z[i] + vz[i]*dt < 0:
         n += 1
         F += abs((m*vz[i])/dt)
      if x[i] - vx[i]*dt > 0.1 or x[i] - vx[i]*dt < 0:
         n += 1
         F += abs((m*vx[i])/dt)
      if y[i] - vy[i]*dt > 0.1 or y[i] - vy[i]*dt < 0:
         n += 1
         F += abs((m*vy[i])/dt)
      if z[i] - vz[i]*dt > 0.1 or z[i] - vz[i]*dt < 0:
         n += 1
         F += abs((m*vz[i])/dt)
   P = F/(6*(0.1)**2)
   P_analytical = float(N)/((0.1)**3)*K*T
   return float(P), float(P_analytical)

T_ = [6000, 50000, 15E6, 1E9]
P_ = []
P_analytical_ = []
for T__ in T_:
   A, B = hayabusa(T__)
   P_.append(A)
   P_analytical_.append(B)

loglog(T_, P_analytical_, 'r', label = 'P_analytical')
hold('on')
loglog(T_, P_, 'b', label = 'P')
legend()
savefig('oppg2.jpg')
show()
