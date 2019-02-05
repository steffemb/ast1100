import matplotlib.pyplot as mpl
from math import *
from numpy import*

star = 'star0'
C = 299792458 # lightspeed
lamda0 = 656.3 #nm
G = 6.67384*10**(-11) 
Ms = 0.8*1.9891*10**30 # star mass*solar masses = kg

def readfile(star):
    infile = open('%s.txt' % star, 'r')
    times = []
    lamdas = []
    fluxs = []

    while True:
        line = infile.readline()
        if not line:
            break
        numbers = line.split()
        time = float(numbers[0])
        lamda = float(numbers[1])
        flux = float(numbers[2])
    
        times.append(time)
        lamdas.append(lamda)
        fluxs.append(flux)
    infile.close()
    
    return [times, lamdas, fluxs]
    
#plot(x, lamdas)

def Vr(lamda):
    Vr_ = []
    i = 0
    for i in range(len(lamda)):
        Vr_.append( float((lamda[i] - lamda0)/lamda0)*C )
        i = i + 1
    return Vr_

data = readfile(star)
VrStar = asarray(Vr(data[1]))
VrStarP = asarray(sum(VrStar)/len(VrStar))
VrStarR = asarray((VrStar - VrStarP)) # relative
t = data[0]
 
fluxs = data[2]
mpl.plot(t, fluxs)
mpl.savefig('%s_flux.jpg' % star)
mpl.show()
   
mpl.plot(t, VrStarR)
mpl.hold('on')



#by eye
Vr_eye = 225
period_eye =350000
Mp_eye = ((period_eye**(1./3))*Vr_eye*(Ms**(2./3)))/((2*pi*G)**(1./3))/(5.97219*10**24)

def VrModel(t, t0, P, Vr):
    return Vr*cos((2*pi/P)*(t-t0))

n = 20
    
min_t0 = 280000
max_t0 = 300000
t0_list = linspace(min_t0, max_t0, n) # theoretical points

min_Vr = 200 
max_Vr = 260
Vr_list = linspace(min_Vr, max_Vr, n)

min_period =320000
max_period =390000
period_list = linspace(min_period, max_period, n)

best_approx = 23**100
for i in range(len(t0_list)):
    for j in range(len(Vr_list)):
        for k in range(len(period_list)):
            Vr_Model = VrModel(t, t0_list[i], period_list[k], Vr_list[j])
            delta = sum(((VrStarR) - (Vr_Model))**2)
            if delta < best_approx:
                best_approx = delta
                best_t0 = t0_list[i]
                best_Vr = Vr_list[k]
                best_P = period_list[j]

Vr_model_plot = VrModel(t, best_t0, best_P, best_Vr)

mpl.plot(t, Vr_model_plot)
mpl.savefig('%s_modelvsdata.jpg' % star)
mpl.show()
print "best_approx = %g" % best_approx
print "best_t0 = %g" % best_t0 
print "best_Vr = %g" % best_Vr 
print "best_P = %g" % best_P 

bestMp = ((best_P**(1./3))*best_Vr*(Ms**(2./3)))/((2*pi*G)**(1./3))/(5.97219*10**24)
print "bestMp = %g earth masses" % (bestMp)
print "by-eye Mp = %g" % (Mp_eye)


"""
star0:

min_t0 = 280000
max_t0 = 300000

min_Vr = 200 
max_Vr = 260

min_period =320000
max_period =390000

Vr_eye = 225
period_eye =350000

-------
steffen@steffen-MS-7792:~/Main/ast1100/oblig_2$ python oblig_2.py
best_approx = 113861
best_t0 = 288421
best_Vr = 222.105
best_P = 345789
bestMp = 475.344 earth masses
by-eye Mp = 483.486
--------

star3:

min_t0 = 120000
max_t0 = 140000

min_Vr = 700 
max_Vr = 800

min_period =200000-45000
max_period =230000-45000

Vr_eye = 750
period_eye =175000

--------
steffen@steffen-MS-7792:~/Main/ast1100/oblig_2$ python oblig_2.py
best_approx = 114017
best_t0 = 129474
best_Vr = 763.158
best_P = 173947
bestMp = 949.553 earth masses
by-eye Mp = 935.06
--------

star4:

min_t0 = 500000
max_t0 = 700000

min_Vr = 300
max_Vr = 400

min_period =1000000
max_period =1100000

Vr_eye = 330
period_eye =1100000

--------
steffen@steffen-MS-7792:~/Main/ast1100/oblig_2$ python oblig_2.py
best_approx = 391865
best_t0 = 521053
best_Vr = 336.842
best_P = 1.02632e+06
bestMp = 1778.91 earth masses
by-eye Mp = 1783.52
---------

"""



