N=1000000
pi = 4.0

for i in range(1,N):
  pi = pi + 4*(-1)**(-i)/float(2*i+1) 
  
  print(i,pi)
