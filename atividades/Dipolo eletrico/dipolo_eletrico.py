import biblio_bisseccesao as bib
import math as mt
import numpy as np

'''
    def fun(teta):
    def raio(r):
    return(1.0 / (r**(2) + 2*r*mt.cos(teta) + 1 )**(0.5)) - r**(-1)
    return(raio)
'''


def dipolo(theta):
    def raio(r):
        return (1./np.sqrt(r**2+2*r*np.cos(theta)+1)-1./r)
    return (raio)

theta = np.linspace(np.pi*0.5,np.pi,1000)
V = np.zeros(len(theta))
for i in range(len(theta)):
    dip = dipolo(theta[i])
    V[i] = bib.raizes(0.3,2,10**(-10),dip)

plt.plot(V,theta)
plt.show()

