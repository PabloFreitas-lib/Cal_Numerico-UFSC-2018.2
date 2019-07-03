''' 

Comentarios sobre a aula pratica de Interpolacao

Boas pratica de programacao:
###################################################################
EM C: 
+--------------------------------------------------------+
|                                                        |
|void func ( const float &x) << passagem por referencia  |
|{                                                       |
|                                                        |
|}                                                       |
|                                                        |
|float a = 0;                                            |
|func(a);                                                |
|                                                        |
+--------------------------------------------------------+
Em Python :

+---------------------------------------------------------------+
|                                                               |
| O "ponteiro do python aponta para um "valor" ,                |
| podendo ser uma matriz um grafico etc .    .     .            |
|                                                               |
|--> Variaveis imutaveis :                                      |
|   Se eu tenho A = 52 , mas eu faco A = A +1 o python cria uma |    
|   nova variavel e nao apaga o 52 , e agora A aponta para 53 e |
|   so apaga o 52 se for necessario.                            |
|--> Se eu faco B = A ( isso quer dizer que B agora vai apontar |
|   para o mesmo lugar em que o nome A esta apontando.          |
|                                                               |
|Comentarios sobre slide 7 aula de interpolacao.                |
+---------------------------------------------------------------+


Lista:

+---------------------------------------------------------------+
|Exemplo de variavel mutavel:                                   |
|porque ao mudar uma vc tambem mudara a outra                   |
|                                                               |
|                                                               |
+---------------------------------------------------------------+
'''
'''
x = [1,2,3]
y = x
x.append(4)

print("Append 4 em X , Lista X",x)
#>>>[1,2,3,4]
print("Lista Y",y)
#>>>[1,2,3,4]
y.append(5)
print("Append 5 em Y , Lista X", x)
x.append(6)
print("Append 6 em X,Lista Y",y)


x = [0,1,2,3]
y = x
print(x is y)# True
print ( id(x))
print( id(y)) # endereco de memoria

'''
###########################################################################################################################################
# Para copiar conteudo e pode alterar sem modificar a original
'''
import copy as cpy
x = [1,2,3,4,5]
#y = x[:] # somente para lista
y = cpy.copy(x)
print(y is x ) # true
print("Id x",id(x))
print("Id y",id(y))
x.append('Essa lista eh a X')
y.append('Essa lista eh a Y')

print("Lista X",x)
print("Lista Y ",y)
'''

##########################################################################################################################################
'''
-->Se eu copiar so com o copy uma matrix m = [0,1][2,3] copia o objeto
'''

'''
import copy 
x = [ [1,2] ,[3,4] ]
y = copy.deepcopy(x) # return false , usado para copiar todas as linhas , mas tem o intuito de copiar todos os objetos dentro de onde esta apontado
#y = copy.copy(x) # return true
print( y[0] is x [0])

y[0].append("Tito")
y[1].append("Falador")
print(x)
print(y)
'''
#######################################################################################################################################
'''
def func(x,y):
    x= x+1
    y.append(4)
    
x = 1
y = [1,2,3]
func(x,y)
print('x: ', x)
print('y: ',y)

'''

'''
Estudar a biblioteca numpy 
'''
####################################################################################################################################
