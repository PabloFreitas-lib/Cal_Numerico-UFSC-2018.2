import raizes

def fun(x):
  y = x*x - 5.0
  return y


p,E = raizes.bisseccao( a,b,tol,fun )

print("Solução: p ~= ",p," +- ",E)






