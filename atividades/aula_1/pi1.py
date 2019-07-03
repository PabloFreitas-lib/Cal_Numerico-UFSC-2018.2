import matplotlib.pyplot as plt


N=1000
pi = 4.0
vetor_pi = [0]*N
vetor_pi[0] = pi
numerador = -4
denominador = 3.0


for i in range(1,N):
  pi +=  numerador/denominador
  numerador   *= -1
  denominador += 2.0
  
  vetor_pi[i] = pi
  
  #print(i,pi)
  plt.plot(vetor_pi)
  plt.show()
