import matplotlib.pylab as plt
import numpy as np
import math as mt


def P2(x,a):
  """
  Calcula um polinômio de ordem 2
  P2(x) = a0 + a1*x + a2*x**2
  
  Recebe:
    x => Escalar ou vetor onde calcular P2
    a => Vetor com coeficientes
  
  Retorna:
    Polinômio calculado em x
  """
  return ( a[0] + a[1]*x + a[2]*x*x )


x = np.linspace(0,mt.pi,10)  #sequencia utilizada numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
a = (2,1,2)
b= 2

#y = P2.(x,a) # parabola em pe
#y=b*np.cos(x) # F(x)
y = pow(np.cos(x),2) + pow(np.sin(x),2)
#x=a*np.sin(x)

plt.plot(x,y)

#plt.plot( x, P2(x,[0,0,1] ), "b-", label="$P_2(x) = x^2$" )
#plt.plot( x, P2(x,[2,-1,3]), "r-", label="$P_2(x) = 2 - x + 3x^2$" )


plt.grid()
plt.margins(0.1)
plt.legend()
plt.show()