import matplotlib.pyplot as mpl
import numpy as np
from math import *

#constants
star = 'spectrum_day0'
C = 299792458 # lightspeed
lamda0 = 656.3*10**(-9) #nm

#functions
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
        lamda = float(numbers[0])
        flux = float(numbers[1])
    
        lamdas.append(lamda)
        fluxs.append(flux)
    infile.close()

    return [lamdas, fluxs]

data = readfile(star)
lamda = np.asarray(data[0])
flux = np.asarray(data[1])

def F_model(lamda, Fmin, sigma, lamda_center):
    Fmax = 1
    temp = Fmax + (Fmin-Fmax)*(np.exp(-(lamda-lamda_center)**2/(2*sigma**2)))
    return temp


n = 20
Fmin_min = 0.7
Fmin_max = 0.9
Fmin_list = np.linspace(Fmin_min, Fmin_max, n)

# sigma expressed by the FWHM:
sigma_min =(656.41 - 656.38) / (sqrt(8*log(2)))
sigma_max =-(656.37 - 656.422) / (sqrt(8*log(2)))
sigma_list = np.linspace(sigma_min, sigma_max, n)

lamda_center_min = 656.37
lamda_center_max = 656.42
lamda_center_list = np.linspace(lamda_center_min, lamda_center_max, n)

#delta func:
best_approx = 23**1000
for i in range(len(Fmin_list)):
    for j in range(len(sigma_list)):
        for k in range(len(lamda_center_list)):
            #temp = []
            #for m in range(0, len(lamda), len(lamda)):
                #temp.append(F_model(lamda[m], Fmin_list[i], sigma_list[j], lamda_center_list[k]))
            temp = F_model(lamda, Fmin_list[i], sigma_list[j], lamda_center_list[k])
            delta = sum((flux - temp)**2)
            if delta < best_approx:
                best_approx = delta
                best_Fmin = Fmin_list[i]
                best_sigma = sigma_list[j]
                best_lamda_center = lamda_center_list[k]


F_model_plot = F_model(lamda, best_Fmin, best_sigma, best_lamda_center)
print best_approx

mpl.plot(lamda, flux)
mpl.hold('on')
mpl.plot(lamda, F_model_plot, '-r')
mpl.show()


