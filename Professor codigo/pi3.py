def calcula_pi(tol):
  """
  Calcula o número pi com a série de Gregory-Leibnitz
  
  Recebe: a tolerância
  
  Retorna: o pi e o erro  
  """
 


  # Inicializo com valor alto, para entrar no laco
  erro = 10000
  pi_velho = 4.0  # comentario
  pi_novo  = 4.0

  numerador   = -4
  denominador = 3.0

  while erro>tol:
    pi_novo = pi_velho + numerador/denominador
    erro    = abs( pi_novo - pi_velho )
    
    numerador   *= -1
    denominador += 2.0
    pi_velho = pi_novo
  
  return pi_novo, erro



pi,e = calcula_pi(1e-3)
print(pi,e)

print( calcula_pi(1e-6) )






  




