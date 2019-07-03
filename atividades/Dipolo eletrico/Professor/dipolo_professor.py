import math as mt #Utilizacao da biblio matematica
import numpy as np
#def eqdipolo(r,angulo,potencial): # procurar evitar usra dois parametros (angulo e r ) pois dificulta a generalizacao
def eqdipolo(r,parametros):
'''
Calcula o valor da diferenca de potencial eletrico num dipolo.(ref.:slides da aula pratica de bisseccao).
----------------------------------------------------------------+
Recebe:                                                         |
                                                                |
    *Coordenadas polares do ponto onde calcular:                |
                                                                |
        + r --> Raio da equacao.                                |     
        + angulo --> Theta.                                     |
        + potencial.                                            |
----------------------------------------------------------------|
    *new:                                                       |
        + r --> Distancia a origem(coord. polares)              |
        parametro:                                              |
            + angulo --> Angulo(coord. polares)                 |
            + potencial = Potencial                             |
----------------------------------------------------------------+
'''
    #c = mt.cos(angulo)
    #v = 1/mt.sqrt(r*r +2*r*c + 1) - 1/float(r)
    #y  = 1/mt.sqrt(r*r + 2*r*mt.cos(angulo) +1 - 1/float(r) - potencial
    #return( v - potencial)
    angulo = parametros[0]
    potencial = parametros[1]
    
    c = np.cos(angulo)
    v = 1/np.sqrt(r*r +2*r*c +1 ) - 1/r
    
    return(v-potencial)
