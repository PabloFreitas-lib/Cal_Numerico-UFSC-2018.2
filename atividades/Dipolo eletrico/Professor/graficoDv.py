from dipolo import eqdipolo
import matplotlib.pylab as plt
import numpy as np
from raizes import bisseccao

#r , E = bisseccao(eqdipolo ,0.1, 2.0, 0.01,[0,-1]) #, [0,-1]


angulo = np.linspace(0,2*np.py,100)

for a in angulo:
    r,E = bisseccao(eqdipolo,0.1,0.9,0.01,[a,-1])
    
plt.margin(0.1)
plt.grind()
plt.show()
