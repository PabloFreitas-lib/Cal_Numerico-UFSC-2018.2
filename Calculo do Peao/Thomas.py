# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 08:58:00 2018

@author: pablo
"""

import numpy as np

## Tri Diagonal Matrix Algorithm(a.k.a Thomas algorithm) solver
def metodo_thomas(a,b,c,d):
    """
    Encontra a solucao de um Sistema Linear com matriz e coeficientes Tridiagonal pelo metodo de Thomas.
    Hipotese: Assume que a matriz de coeficientes e diagonalmente dominante.
    
    Ref.:Aula de Calculo Numerico
    
    Recebe:   
        Vetores com elementos da matriz
        Tridiagonal aumentada
        Seja um sistema linear NxN
        
        a=> Diagonal Inferior ( n-1 elem)
        b=> Diagonal Principal ( n elem)
        c=> Diagonal Superior ( n -1 elem)
        d=> Termos Independentes ( n elem)
    
    Retorna :
        Vetor solução
    """
    n = len(b)
    
    assert len(a)== n-1 , "Vetor a com tamanho errado"
    assert len(c)== n-1 , " Vetor c com tamanho errado"
    assert len(d)== n, "Vetor d com tamanho errado"
    
    a.insert(0,0,0)
    c.append(0.0)
    #Passo Progressivo
    c[0]/=float(b[0])
    d[0]/=float(b[0])

    for i in range(1,n):
        den = float(b[i] - a[i] * c[i-1])
        c[i] /= den
        d[i] = (d[i] - a[i] *d[i-1])/den
        
    #Passo regressivo
    for i in range(n-2,-1,-1):
        d[i]-= c[i]*d[i+1]

    '''
         x = d
         for i in range(n-2,-1,-1)
             x[i] = d[i] - c[i]*x[i+1]
    '''
    return(d)
'''
|b0     c0  ...     |  d0 |
|a0     b1  c1      |  d1 |
|0      a2  b2  c2  |  d2 |
|0          a3  b3  |  d3 |

Matriz 4x4
'''