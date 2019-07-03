# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 16:12:44 2018

@author: pablo
"""
############- Aula 1 - Introducao- #######################
'''
                                                |
-->Laco while
-->Usar função
-->Reusabilidade
--> Fazer graficos
'''
##################################################
"""
Calcula pi para N termos da série
Variáveis
Estrutura
"""

'''
pi = 4
n = 1000

#pi = pi + (4*pow(-1,n))/ (2*n +1)

for i  in range(1,n):
    pi = pi + (4*pow(-1,i))/float(2*i +1)
    
print(pi)

'''
#################################################
"""
Boas práticas de programação
Melhorar Eficiência do cálculo
Nomes com sentido (Robustez, Reusabilidade)
"""

'''
pi = 4
n = 1000

numerador = -4 #  (4*pow(-1,n)) p/ i =1
denominador = 3 # float(2*i +1) p/ i =1

for i in range(1,n):
    pi += numerador/denominador
    numerador*=-1 # cada interacao so muda o sinal
    denominador+=2 # cada interacao so vai acrescentar 2 unidades
print(pi)
'''
##################################################
"""
Calcular até atingir determinado erro
Laço while
Erro e tolerância
"""
'''
pi_new = 4
pi_velho = 4
tol = 0.01
erro = 10000
#i=1
numerador = -4
denominador =3.0

while erro > tol:
    pi_novo = pi_velho + numerador/denominador
    erro = abs(pi_novo - pi_velho) # pega o modulo erro 
    numerador *= -1
    denominador+=2
   # i+=1
    pi_velho = pi_novo
   
print(pi_novo)
'''
###################################################

"""
Usar função
Reusabilidade
"""

