numerador = -1.0 #sempre será um numero impar e como é expoente do numero 1 nao importa qual seja o numero
denominador = pow(1,-1) # primeiro numero do laco for eh 1 e foi utilizado a funcao potencia nao pensando em otimizar espaco computacional
sum = 1.0

for i in range(1,173):
    sum *= numerador/denominador 
    denominador = pow(i,-1)
    print(i,sum)
