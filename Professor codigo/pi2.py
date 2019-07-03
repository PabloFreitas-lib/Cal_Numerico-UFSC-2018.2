i=1
tol=0.01
erro = 10000

pi_velho = 4.0
pi_novo  = 4.0

numerador   = -4
denominador = 3.0

while erro>tol:

  pi_novo = pi_velho + numerador/denominador
  erro    = abs( pi_novo - pi_velho )

  print(i,pi_novo,erro)
    
  numerador   *= -1
  denominador += 2.0
  i += 1
  pi_velho = pi_novo
print("estou fora")




  




