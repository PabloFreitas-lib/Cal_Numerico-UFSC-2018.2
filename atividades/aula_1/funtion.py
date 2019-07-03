'''
--------Boas praticas para programar:---------------

    -->Robustez(programa nao ter bugs)
    -->Reusabilidade(genérico)
    -->Eficiencia
----------------------------------------------------
'''
def calcula_pi(tol):
    """
    Comentario para funcoes
    O que ela faz:
    
    O que ela recebe:
    
    O que ela retorna:
    """
    erro = 1000
    pi_velho = 4.0
    pi_novo = 4.0
    
    
    numerador = -4
    denominador = 3.0
    
    while erro > tol:
        pi_novo = pi_velho + numerador/denominador
        erro = abs(pi_novo * pi_velho)
        numerador *=-1
        denominador+=2.0
        pi_velho = pi_novo
        
    return pi_novo,erro


pi,e = calcula_pi(1e-3)
print(pi,e)
print(calcula_pi(1e-3)
      
