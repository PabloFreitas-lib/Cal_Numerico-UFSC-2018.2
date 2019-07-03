import math
import raizes


def funcao(x):
  y = pow(x,3)+ 4*pow(x,2)-10
  return y


def funcao2(x):
  y = math.pow(2,x) - x*x
  return y

p,E = raizes.bisseccao( funcao, 0.0, 3.0, 1e-10 )
print("Solução 1: p ~= ",p," +- ",E)

p,E = raizes.bisseccao( funcao2, -1.0, 0.0, 1e-10 )
print("Solução 2: p ~= ",p," +- ",E)







