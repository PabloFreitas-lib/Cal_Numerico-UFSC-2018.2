import numpy as np
from scipy.optimize import bisect
import matplotlib.pylab as plt

def dipolo(theta):
    def raio(r):
        return 1./np.sqrt(r**2+2*r*np.cos(theta)+1)-1./r
    return raio

theta = np.linspace(np.pi*0.5,np.pi,1000)
V = np.zeros(len(theta))
for i in range(len(theta)):
    dip = dipolo(theta[i])
    V[i] = bisect(dip,0.3,0.6)

plt.plot(V,theta)
plt.show()
