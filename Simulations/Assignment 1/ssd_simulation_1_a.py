import numpy as np
from math import *
import matplotlib.pyplot as plt

q=1.6e-19   #electronic charge
un = 1500  #mobility of electron in cm^2/V-s
up = 500  #mobility of hole
Nc = 2.8e19
Nv = 1e19
Eg = 1.12  #band gap energy difference
k  = 1.38e-23  #Boltzmann constant
V=1 #voltage
A=1 #area in m^2
l=10 #length in m

T=np.linspace(200,2000,5000)
x_1000_by_T=np.linspace(0.5,5,5000)
T_1=np.array([(element/300)**1.5 for element in T])
e=np.array([np.exp((-Eg*q)/(2*k*element)) for element in T])
I=V*A*10/l*(un+up)*sqrt(Nc*Nv)*T_1*(e)
plt.semilogy(x_1000_by_T,I)
plt.title('Plot of $\log(I)$ vs 1000/T')
plt.xlabel('1000/T')
plt.ylabel('log of current')
plt.show()