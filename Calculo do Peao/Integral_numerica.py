# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 08:47:52 2018

@author: pablo
"""

'''
Utilizar o metodo spline para calcular o volume do peão simetrico

1- Dados em arquivo ( Duas colunas, X e Y)
    1.75    2.37
    1.87    3.63
    ...
            ...
A partir disso calcular a spline:
    Função 1 : Metodo de Thomas
    Função 2 : Spline ( Ac = B)

Sequencia surgerida :

1- Implementar o método de Thomas ( forma de biblioteca), Testar o metodo com casos simples.
2 - Implementar a Spline natural ( forma de biblioteca ), testar funcionabilidade com casos simples ( fazer gráficos).        
'''
import Thomas
import numpy as np
#               line 1   | line 2    |  line 3   | line 4
A = np.array([[10,-2,0,0],[1,11,3,0],[0,-1,10,5],[0,0,-1,8]],dtype=float)   
#print(A)
        
a = np.array([1.,-1,-1])#a1 a2 a3
b = np.array([10.,11.,10.,8.]) #b0 b1 b2 b3
c = np.array([-2.,3.,5.]) #c0 c1 c2
d = np.array([6,25,-11,15.]) #d0 d1 d2 d3

print (Thomas.thsolver(a, b, c, d))
#[ 0.14877589  0.75612053 -1.00188324  2.25141243]
#compare against numpy linear algebra library
print (np.linalg.solve(A, d))
#[ 0.14877589  0.75612053 -1.00188324  2.25141243]


'''
|b0     c0  ...     |  d0 |
|a1     b1  c1      |  d1 |
|0      a2  b2  c2  |  d2 |
|0          a3  b3  |  d3 |

Matriz 4x4
'''