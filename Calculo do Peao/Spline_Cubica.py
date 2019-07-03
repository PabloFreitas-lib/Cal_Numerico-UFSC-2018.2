# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 09:48:12 2018

@author: pablo
"""

def coeficientes_spline(x,y):
    """
    Encontra os coeficientes da Spline Cubica com conficoes de contorno livres
    
        Recebe:
            x,y => Dados. Vetores com n elementos
            
        Retorna:
            Coeficientes da Spline em vetores a,b,c,d com n-1 elementos:
                
            Seja:
                hi = x -xi
                Si = ai + bi*hi +ci*hi^2 _ di*hi^3
    """

    n = len(x)
    
    assert len(y)== n , "Vetores com tamanhos diferentes"
    a = y
    h = [0]*(n-1)
    for i in range(n-1):
        h[i] = x[i+1] - x[i]
        
    #Monta o Sistema Linear Tridiagonal
    
    diagInf = [0]*(n-1)
    for i in range(n-2):
        diagInf[i] = h[i]
    
    diagPrin = [1.0]*n
    for i in range(1,n-1):
        diagPrin = 2*( h[i-1]+  h[i])
    
    diagSup= [0]*(n-1)
    for i in range(1,n-1):
        