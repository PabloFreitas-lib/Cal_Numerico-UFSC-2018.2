''' f(x) = x^3 + 4x^2 - 10 
raizes em [1,2] , com tolerancia de 10^-4
'''
def fun(x):
    return(x**3+ 4*x**2 - 10)

def bissecao_fun(a,b,tol,fun):
           
            E = (b - a)/2
            p = (b + a)/2
            
            if (fun(p) == 0): 
                print("Achou sua raiz")
            
            elif ((fun(a)) * (fun(p)) > 0 ):                 # sinais iguais
                a_f = p
                b_f = b
            
            else:                                           # sinais diferentes
                a_f = a
                b_f = p
                

            while E > tol:
                E = (b_f - a_f)/2
                p = (b_f + a_f)/2
                print(a_f,b_f,p)
                

                if (fun(p) == 0):
                    print("Achou sua raiz")
                elif fun(a_f) * fun(p) > 0:                 # sinais iguais
                    a_f = p
                    #b_f = b_f
                else:
                    #a_f = a
                    b_f = p
            
            return(p,E)
print(bissecao_fun(1.0,2.0,10**(-4),fun))
#print(fun(1),fun(1.5))
