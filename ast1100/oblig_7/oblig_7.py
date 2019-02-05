import matplotlib.pyplot as mpl
import numpy as np
from math import *

def readfile(read):
    infile = open('%s.txt' % read, 'r')
    column1 = []
    column2 = []
    column3 = []
    column4 = []

    while True:
        line = infile.readline()
        if not line:
            break
        numbers = line.split()
        data1 = float(numbers[0])
        data2 = float(numbers[1])
        data3 = float(numbers[2])
        data4 = float(numbers[3])
    
        column1.append(data1)
        column2.append(data2)
        column3.append(data3)
        column4.append(data4)
    infile.close()

    return [column1, column2, column3, column4]

def doppler(lamda):
    C = 299792458
    lamda0 = 0.212 #m
    if type(lamda) == float:
        return (((lamda - lamda0)/lamda0)*C )
    else:
        Vr_ = []
        i = 0
        for i in range(len(lamda)):
            Vr_.append(float((lamda[i] - lamda0)/lamda0)*C )
            i = i + 1
        return Vr_

data = readfile('galaxies')
arcmin_x = np.asarray(data[0])
arcmin_y = np.asarray(data[1])
distance = np.asarray(data[2]) #Mpc
spectra = np.asarray(data[3]) #m
Vr_gal = np.asarray(doppler(spectra))

V_cluster = sum(Vr_gal)/len(Vr_gal)
print 'the relative speed of the cluster is %d m/s' % V_cluster

mpl.plot(arcmin_x, arcmin_y, 'o', label="galaxies")
mpl.xlabel("x_arcmin",fontsize=26)
mpl.ylabel("y_arcmin",fontsize=26)
mpl.legend()
mpl.savefig('oppg_2_4b.jpg')
mpl.show()

def doublesum(arcmin_x, arcmin_y, distance):
    tot = 0
    G = 6.67384*10**(-11)
    for i in range(len(arcmin_x)):
        for j in range(0, i-1):
            Mpc = (3.08567758*10**22)
            P = sqrt((arcmin_x[i] - arcmin_x[j])**2 + (arcmin_y[i] - arcmin_y[j])**2)
            P_arc = P/((180/np.pi)*60)
            B = (distance[i]*(Mpc))*P_arc
            r = sqrt(B**2 + ((distance[i]*(Mpc) - distance[j]*(Mpc)))**2)
            tot += 1/r
    return G*tot

V_sum = 0
for k in range(len(Vr_gal)):  
    V_sum += Vr_gal[k]**2

m = (V_sum)/(doublesum(arcmin_x, arcmin_y, distance))
print 'the mass of a galaxy is %e kg' % m

"""

steffen@steffen-MS-7792:~/Main/ast1100/oblig_7$ python oblig_7.py 
the relative speed of the cluster is 1235929 m/s
the mass of a galaxy is 6.164245e+42 kg


"""

