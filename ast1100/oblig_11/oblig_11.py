
from matplotlib.pyplot import *
from numpy import *

# oppg 1
M = 1.
r0 = 20. # r0/M
vshell0 = 0.993 # C
theta = (167./360)*(2.*pi)
Lm = r0*(1./sqrt(1.-vshell0**2))*vshell0*sin(theta)  # (L/m)/M
Em =  sqrt(1.-(2.*M)/r0)*(1./sqrt(1.-vshell0**2)) # E/m
n = 1000
phi = zeros(n)
dtau = 0.01

# oppg 2
r = zeros(n)
r[0] = r0

# oppg 3
for i in range(len(r)-1):
   dr = - (sqrt((Em)**2 - (.1+ (Lm/r[i])**2)*(1.-(2.*M/r[i])))*dtau)
   r[i+1] = r[i] + dr
   dphi = (Lm/r[i]**2)*dtau 
   phi[i+1] = phi[i] + dphi
   lastphi = phi[i+1]
   if r[i+1]/M < 2:
      break

# oppg4
x = r*cos(phi)
y = r*sin(phi)

# oppg5
hr = 2
hphi = linspace(0,2*pi,100)
hx = hr*cos(hphi)
hy = hr*sin(hphi)

plot(x, y, "x", label = "trajectory")
axis("equal")
plot(hx, hy, label = "horizon")
legend()
savefig("blackhole.png")
show()

#oppg6
print "the last angle is %1.2f (in radians)" % lastphi


"""
steffen@steffen-MS-7792:~/Main/ast1100/oblig_11$ python oblig_11.py 
the last angle is 3.42 (in radians)
"""
