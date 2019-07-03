N=1000
pi = 4.0

numerador = -4
denominador = 3.0


for i in range(1,N):
  pi +=  numerador/denominador
  numerador   *= -1
  denominador += 2.0
  
  
  print(i,pi)
