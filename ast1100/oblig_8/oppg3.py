#from random import gauss
from numpy import *
import random


K = 1.3806488*10**(-23)
T = 6000
m = 1.66053892*10**(-27)
n = 100000
sigma = sqrt((K*T)/m)
mean = 0

v = []
for i in range(0, n):
   temp = random.gauss(mean,sigma)
   v.append(temp**2)

Ek = 0.5*m*(sum(v))/n
print 'numerical Ek = %e' % Ek

analytical = (3/2)*K*T
print 'analytical Ek = %e' % analytical

"""
steffen@steffen-MS-7792:~/Main/ast1100/oblig_8$ python oppg3.py 
numerical Ek = 4.177923e-20
analytical Ek = 8.283893e-20

det virker som det er en faktor 2 som er fursvunnet her, men jeg finner ikke
ut hvor. hvis jeg setter sigma = sqrt(2*(K*T)/m) blir print:

steffen@steffen-MS-7792:~/Main/ast1100/oblig_8$ python oppg3.py 
numerical Ek = 8.305724e-20
analytical Ek = 8.283893e-20

men jeg finner ikke ut hvorfor dette skjer..

"""
