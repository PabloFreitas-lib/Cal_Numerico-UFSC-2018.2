def raizes(a,b,tol,fun):
    
    """
  Encontra a raiz de F (em [A,B]) com um erro
  menor que TOL usando o algoritmo da Bissecção
  
  Recebe:
    F   => Função para encontrar a raiz
    A,B => Intervalo de busca da raiz
    TOL => Valor máximo do Erro (tolerância)
  
  Retorna:
    p   => Raiz encontrada
    E   => Erro  
  """
    E = (b - a)/2.0
    P = (b + a)/2.0
    
    while E > tol:
        if fun(a)* fun(P) < 0:
            b = P
        else:
            a = P
        
        E = (b - a)/2.0
        P = (b + a)/2.0
    
    return(P,E)
